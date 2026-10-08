# 39 — Why `list.append` is amortized O(1) (over-allocation)

> **Interview question:** "Why is `list.append` O(1) if the list sometimes has to grow?"
> **What the interviewer is really testing:** Whether you understand amortized analysis — occasional expensive operations averaged over many cheap ones.

## Theory — what it is

A Python `list` is a **dynamic array** — a contiguous block of memory holding pointers to objects. "Contiguous" means the slots sit side-by-side in memory, which is why indexing `a[i]` is O(1): Python computes `base + i * slot_size` and jumps straight there. But memory after the array might already be used by something else, so you can't always just extend it.

To grow, CPython **over-allocates**: it always reserves more slots than the list currently uses. `append` usually just writes into a spare slot — O(1). Only when the spare slots run out does Python do the expensive thing: allocate a bigger block (growing by roughly 1.125x plus a small amount), **copy every pointer** into it, and free the old block. That copy is O(n) — but it happens rarely.

**"Amortized O(1)"** means: if you do N appends, the *total* cost is proportional to N, so the *average* cost per append is constant — even though a few individual appends trigger a big copy. Think of paying $100 rent once a month: some days cost $100, most cost $0, but the average is ~$3.30/day.

## Why it was needed

If the array grew by exactly one slot per append, **every** append would copy the whole list — building a list of N items would cost `1 + 2 + ... + N = O(N^2)`. A million-item loop would do ~500 billion pointer copies. With geometric over-allocation (each new block a bit bigger than the last), the number of copies grows only linearly: a million appends trigger only ~30 resizes, and each element gets copied only a handful of times total.

The key insight for interviews: growing by a *constant* amount (e.g., +10 slots each time) still gives O(N^2) total. Growing by a *multiplicative* factor is what makes the copies geometric and the total linear. Python's actual formula (`new_allocated = newsize + (newsize >> 3) + 6`) grows ~12.5% per resize — small factor, still amortized O(1), wastes less memory than doubling.

## Where it's used in a real project

- **Building results in a loop:** `results.append(row)` inside ETL/parse loops — the reason this idiom is fast and `results = results + [row]` is a performance bug.
- **Streaming data:** reading lines and appending, then processing — memory stays ~1x the data size, not quadratic time.
- **`list` comprehension:** CPython knows the trick too — comprehensions build lists efficiently under the same model.
- **Why `insert(0, x)` / `pop(0)` are bad:** every element must shift — O(n) each. Use `collections.deque` for both-ends work.

## Diagram

```
capacity = slots allocated, size = items actually stored

append x1..x4:   [x1 x2 x3 x4 | _ _ _ _]     cheap writes into spare slots
                 size=4  capacity=8

append x5..x8:   [x1 x2 x3 x4 x5 x6 x7 x8]   still cheap... no spares left

append x9:       resize! copy all 8 pointers into new, bigger block
                 [x1 x2 x3 x4 x5 x6 x7 x8 x9 | _ _ _ ...]
                 (one O(n) step, then many cheap steps again)

Total copies for N appends ~ O(N)  =>  average cost per append = O(1)
```

## Code — explained

```python
import sys

a = []
print(sys.getsizeof(a))      # 56 — empty list, no slot storage yet

for i in range(9):
    a.append(i)
    print(len(a), sys.getsizeof(a))
# 1 88   <- capacity jumped to 4   (56 + 4*8)
# 4 88   <- still fits
# 5 120  <- resized to capacity 8
# 9 184  <- resized to capacity 16
```

1. `getsizeof` shows raw allocated bytes — each pointer slot is 8 bytes on a 64-bit system.
2. Sizes jump in steps (88, 120, 184...), not one slot at a time — visible proof of over-allocation.
3. `len` grows smoothly while capacity grows in geometric jumps; `capacity >= size` always.
4. Try it: appending beyond a boundary spikes cost once, then subsequent appends are cheap again.

## Problems

### Easy — amortized reasoning
**Problem:** How many pointer copies (resizes) does this loop trigger, and what's the per-append average? Just predict, then verify mentally.
**Try this input:** `n = 16` appends starting from empty
**Expected output:** capacity goes 4 -> 8 -> 16; only ~3 resize events; average work per append stays small
**Solution:**
```python
import sys

a = []
prev = sys.getsizeof(a)
resizes = 0
for i in range(16):
    a.append(i)
    cur = sys.getsizeof(a)
    if cur != prev:
        resizes += 1
        prev = cur
print(resizes)   # 3
```
**Logic explained:**
1. A resize is the only time allocation changes — watching `getsizeof` counts them.
2. 16 appends cause only 3 resizes — the expensive O(n) copies are rare.
3. Rare expensive + frequent cheap = amortized O(1) per append.

### Medium — the O(n^2) trap to avoid
**Problem:** Two ways to build a list — which is O(n) and which is O(n^2), and why?
**Try this input:** `n = 5`
**Expected output:** both produce `[0, 1, 2, 3, 4]`, but method B copies the whole list every iteration
**Solution:**
```python
def good(n):
    a = []
    for i in range(n):
        a.append(i)          # amortized O(1)
    return a

def bad(n):
    a = []
    for i in range(n):
        a = a + [i]          # NEW list + full copy every time -> O(n) each
    return a

print(good(5))   # [0, 1, 2, 3, 4]
print(bad(5))    # [0, 1, 2, 3, 4]
```
**Logic explained:**
1. `a.append(i)` writes into spare capacity — amortized O(1), total O(n).
2. `a + [i]` creates a brand-new list and copies all existing pointers — O(n) every iteration, O(n^2) total.
3. Same output, wildly different cost — this is the classic production bug this question is really about.

### Hard — implement append yourself
**Problem:** Implement a mini dynamic array class with `append`, showing resize logic. Capacity grows by doubling.
**Try this input:** append 1,2,3,4,5 to capacity-2 array
**Expected output:** internal capacity ends at 8; `len` is 5; elements preserved
**Solution:**
```python
class DynArray:
    def __init__(self):
        self.data = [None] * 2   # capacity 2
        self.size = 0

    def append(self, x):
        if self.size == len(self.data):          # out of spare slots
            new = [None] * (len(self.data) * 2)  # double capacity
            for i in range(self.size):           # O(n) copy — rare
                new[i] = self.data[i]
            self.data = new
        self.data[self.size] = x                 # O(1) write
        self.size += 1

d = DynArray()
for i in [1, 2, 3, 4, 5]:
    d.append(i)
print(d.data[:d.size], len(d.data))   # [1, 2, 3, 4, 5] 8
```
**Logic explained:**
1. `size` tracks used slots; `len(self.data)` is allocated capacity — same split as CPython.
2. When `size == capacity`, allocate a bigger block and copy — the rare O(n) step.
3. Otherwise just write into a free slot — the common O(1) step.
4. Doubling means each element is copied O(log n) times total across all appends — total work O(n), hence amortized O(1) each.

## The 30-second interview answer

"A Python list is a dynamic array — contiguous memory for O(1) indexing. `append` is amortized O(1) because Python over-allocates: it keeps spare slots, so most appends just write into free space. When the array fills, it allocates a bigger block and copies everything — an O(n) operation — but the growth is multiplicative, so resizes get exponentially rarer. Total work for n appends is O(n), so the average is O(1). The flip side: `insert(0)` or `pop(0)` are O(n) because every element shifts — use `deque` for that."

## Follow-up trap

**"So is every single append O(1)?"** No — that's exactly what "amortized" means: the resize append is O(n). If they push further — *"why not grow by a fixed +100 slots?"* — because linear growth still gives O(n^2) total; multiplicative growth is required. And *"what about shrinking?"* — `pop()` from the end is cheap; Python may shrink the allocation when the list gets very empty, but it deliberately doesn't shrink on every pop (that would thrash: append/pop around a boundary would resize every time — hysteresis).
