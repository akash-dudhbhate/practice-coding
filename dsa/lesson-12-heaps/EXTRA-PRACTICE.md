# lesson-12-heaps — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Is this array a valid min-heap?

Check each: `[1, 4, 3, 7, 8, 5]` and `[1, 3, 5, 2, 4]`.

<details><summary>Answer</summary>

`[1, 4, 3, 7, 8, 5]` — YES. Check `heap[i] <= heap[2i+1], heap[2i+2]`:
- i0=1: children 4,3 ✓ · i1=4: children 7,8 ✓ · i2=3: child 5 ✓ (index 6 out of range)

`[1, 3, 5, 2, 4]` — NO. i1=3 has left child index 3 = `2`, and `3 > 2`. Draw the tree:

```
        1
       / \
      3   5       <- 3 > its left child 2. Not a heap.
     / \
    2   4
```

Heap check = parent-versus-children only. Note `[1,4,3,...]` has `3 < 4` as siblings — irrelevant.
</details>

---

## Check 02: What does heapify produce?

```python
import heapq
a = [5, 3, 8, 1, 9, 2]
heapq.heapify(a)
print(a[0], a)
```

Predict `a[0]` and whether `a` comes out sorted.

<details><summary>Answer</summary>
`a[0]` is **1** — guaranteed. `a` is **not sorted**: heapify yields `[1, 3, 2, 5, 9, 8]` (a valid heap — check the child indices). "Heapified" means the min sits on top and the parent≤children rule holds; "sorted" is a strictly stronger claim that only repeated `heappop` gives you.
</details>

---

## Check 03: Top-K direction

You want the **3 largest** numbers in a stream. Which heap do you keep — min-heap or max-heap — and what does its root represent?

<details><summary>Answer</summary>
**Min-heap of size 3.** The heap holds "the best 3 seen so far," and its root (`h[0]`) is the *smallest of the kept three* — the bar a newcomer must clear. When `x > h[0]`, `heapreplace` evicts the current worst. If you used a max-heap, the max would sit on top and you'd have no efficient way to drop the *worst* of your kept set.

Mnemonic: "kth LARGEST → keep the SMALLEST-on-top heap."
</details>

---

## Check 04: Complexity spot-check

```python
def k_largest(nums, k):
    nums.sort(reverse=True)
    return nums[:k]
```

vs a size-k heap. n = 10⁷, k = 10. What's the difference, and when does it not matter?

<details><summary>Answer</summary>
Sorting: **O(n log n)** time, and it destroys the input order (a side effect!). Size-k heap: **O(n log k)** time, O(k) extra space, input untouched, works on a stream. For k=10, `log k` vs `log n` is ~3× less work per element — and if nums arrives as a stream, sorting isn't even an option (you'd buffer everything). When k ≈ n, or the list is small and disposable, sorting is simpler and fine — the heap wins specifically when k << n or input is unbounded.
</details>

---

## Check 05: Two-heap median

Stream so far: `2, 8, 5`. `lo` (max-heap, stored negated) holds the lower half, `hi` (min-heap) the upper. Next value `4` arrives. Describe the insert + rebalance.

<details><summary>Answer</summary>
State before: `lo = [2]` (as `[-2]`), `hi = [5, 8]` — median = (2+5)/2 = 3.5.

Insert `4`: push to `lo` → `lo=[4,2]` (as negated `[-2,-4]`). Rebalance — `lo` has 2, `hi` has 2 but the rule is `max(lo) <= min(hi)` and sizes differ ≤ 1... more precisely we first compare: `lo`'s max is 4 ≤ `hi`'s min 5 — already ordered. Sizes equal → median = (4 + 5)/2 = **4.5**.

The point: medians live at the *boundary* between halves, so you only ever need each half's extreme — exactly the two roots, O(1) to read.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Kth largest — wrong heap direction

```python
import heapq

def kth_largest(nums, k):
    h = [-x for x in nums]      # max-heap of EVERYTHING
    heapq.heapify(h)
    for _ in range(k):
        ans = heapq.heappop(h)
    return -ans
```

**Hint:** It gives the right answer. What's wrong with it anyway?

<details><summary>Answer</summary>

**Bug:** not a correctness bug — a pattern bug. It heaps all n items (O(n) heapify, fine) but holds O(n) space and does k pops O(k log n). The top-K *pattern* — a size-k min-heap — costs O(n log k) and O(k) space, which matters exactly when k << n or the input is a stream. On a 10⁹-element stream this version can't even start.
**Fix:**
```python
h = nums[:k]
heapq.heapify(h)
for x in nums[k:]:
    if x > h[0]:
        heapq.heapreplace(h, x)
return h[0]
```
</details>

---

## Debug 02 (Medium): Merge-k-sorted — payload compare crash

```python
import heapq

def merge_k_sorted(lists):
    h = [(lst[0], lst) for lst in lists if lst]
    heapq.heapify(h)
    out = []
    while h:
        val, lst = heapq.heappop(h)
        out.append(val)
        # push next element of lst ... (details omitted)
    return out
```

**Hint:** two lists starting with the same value. What does Python do to break the tie?

<details><summary>Answer</summary>

**Bug:** tuple comparison falls through to the second element — `list < list` — when `lst[0]` values tie. Here it compares the lists, which happens to work for ints, but any non-comparable payload (nodes, dicts) crashes `TypeError: '<' not supported`. Even for lists it's fragile.
**Fix:** never let payloads compare — carry explicit indices:
```python
h = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
# on pop (v, i, j): out.append(v)
#   if j+1 < len(lists[i]): heappush(h, (lists[i][j+1], i, j+1))
```
The `(value, i, j)` triples never compare a list — `i` breaks every tie.
</details>

---

## Debug 03 (Medium): Last stone — forgetting the negation

```python
import heapq

def last_stone_weight(stones):
    h = [-s for s in stones]
    heapq.heapify(h)
    while len(h) >= 2:
        x = heapq.heappop(h)          # most negative = heaviest
        y = heapq.heappop(h)
        if x != y:
            heapq.heappush(h, x - y)  # BUG: pushes the NEGATED diff
    return -h[0] if h else 0
```

**Hint:** trace `[2, 8]` — the smash should leave a stone of weight 6.

<details><summary>Answer</summary>

**Bug:** signs flip on the way back in. `x=-8, y=-2` → `x - y = -6` pushed — that encodes weight **+6 correctly by accident**? Check: heap stores negatives; `-6` means stone weight 6. Hmm — actually `x - y = -8 - (-2) = -6`, pushing `-6` = weight 6 — correct!

So where's the real bug? `x != y` compares negated values — `-8 != -2` true, fine, and `x - y` vs `y - x`: the real smash is `|x| - |y|` = 8-2 = 6 → push `-6` = `x - y`? `-8-(-2) = -6` ✓. Actually this code is CORRECT.

The subtle version of the bug: pushing `y - x` instead → `-2 - (-8) = +6` — a positive number in a min-heap of negatives → it becomes the *max* of the heap (wrong), and `-h[0]` reads garbage. Moral: with negation tricks, trace one example end-to-end — sign errors hide until a specific input exposes them. Cleaner fix that avoids the mental gymnastics:
```python
x, y = -heapq.heappop(h), -heapq.heappop(h)   # un-negate at the door
if x != y:
    heapq.heappush(h, -(x - y))
```
</details>

---

## Debug 04 (Hard): Median-of-stream — unbalanced halves

```python
import heapq

def running_medians(nums):
    lo, hi, out = [], [], []          # lo = max-heap (negated), hi = min-heap
    for x in nums:
        heapq.heappush(lo, -x)
        heapq.heappush(hi, -heapq.heappop(lo))   # move lo's max to hi
        # BUG: no rebalance back — lo can end up EMPTYER than hi by 2+
        if len(lo) == len(hi):
            out.append((-lo[0] + hi[0]) / 2)
        else:
            out.append(float(hi[0]))
    return out
```

**Hint:** trace `[1, 2, 3]` — what's the reported median after `3`?

<details><summary>Answer</summary>

**Bug:** after pushing every element to `hi` (via `lo`), `hi` can exceed `lo` by more than 1. Trace `[1,2,3]`:
- x=1: lo=[-1], push 1→hi=[1]. sizes 0/1 → median hi[0]=1.0 ✓
- x=2: lo=[-2], push 2→hi=[1,2]. sizes 0/2 → `else` branch reads `hi[0]=1` → median **1.0** but true median of [1,2] is **1.5**. Also violates the balance invariant.
- x=3: median of [1,2,3] reported as hi[0]=1 — badly wrong.

**Fix:** keep `len(hi) <= len(lo)` (or diff ≤ 1) — after the push, if `len(hi) > len(lo)`, move `hi`'s min back:
```python
heapq.heappush(lo, -x)
heapq.heappush(hi, -heapq.heappop(lo))
if len(hi) > len(lo):
    heapq.heappush(lo, -heapq.heappop(hi))
median = float(-lo[0]) if len(lo) > len(hi) else (-lo[0] + hi[0]) / 2
```
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: Reading `h[1]` for "second smallest"
```python
# WRONG — heap order ≠ sorted order past index 0
second = h[1]
# CORRECT — pop twice (or nsmallest(2, h)[-1])
```
`h[0]` is the only position with a guarantee.

## Mistake 02: `sort()` inside the loop
```python
# WRONG — O(n log n) per iteration: a heap that isn't
while items:
    items.sort()
    take items[0]
# CORRECT — heapify once, heappop in O(log n)
```

## Mistake 03: Forgetting payloads need a tiebreaker
```python
heappush(h, (dist, node))            # dist tie → compares nodes → TypeError risk
heappush(h, (dist, counter, node))   # unique counter: ties never reach `node`
```

## Mistake 04: Max-heap without the double-negation discipline
Push `-x` but read `heappop(h)` as if it were the max → you're returning `-max`, a negative number. Rule: negate on the way in AND on the way out — or un-negate at pop (`x = -heappop(h)`).

## Mistake 05: Assuming `heapify` sorted the list
```python
h = [9, 4, 7, 1]
heapq.heapify(h)
print(h)     # [1, 4, 7, 9] — sorted?? NO, coincidence-free check:
```
`[9,4,7,1]` heapifies to `[1,4,7,9]` — looks sorted by luck. Try `[5,3,8,1,9,2]` → `[1,3,2,5,9,8]`: clearly not sorted. The invariant is `h[i] <= h[2i+1], h[2i+2]`, nothing more.

## Mistake 06: Reorganize-string — placing the same char twice in a row
Greedy "always most frequent" fails unless you HOLD BACK the char you just placed for one step (push it back next iteration). Otherwise `"aab"` → `"aab"`-style outputs with adjacent dupes.

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual min-tracking instead of heapify
### Before
```python
def run_heap_ops(nums, ops):
    h = sorted(nums)             # "heap" = sorted list
    out = []
    for op in ops:
        if op[0] == "push":
            h.append(op[1]); h.sort()      # re-sort every push: O(n log n) each
        elif op[0] == "pop":
            out.append(h.pop(0))           # O(n) pop from front!
        else:
            out.append(h[0])
    return out
```
### Problems
1. Works, but each op is O(n) or worse — the heap exists precisely to make these O(log n)/O(1).

### After
```python
def run_heap_ops(nums, ops):
    h = nums[:]
    heapq.heapify(h)
    out = []
    for op in ops:
        if op[0] == "push":    heapq.heappush(h, op[1])
        elif op[0] == "pop":   out.append(heapq.heappop(h))
        else:                  out.append(h[0])
    return out
```

---

## Refactor 02 (Medium): Merge-k-sorted via chain+sort
### Before
```python
def merge_k_sorted(lists):
    out = []
    for lst in lists:
        out.extend(lst)
    return sorted(out)           # O(N log N), ignores that inputs were sorted
```
### Problems
1. Throws away the gift: the inputs are ALREADY sorted. Merging should cost O(N log k), not O(N log N).

### After
```python
def merge_k_sorted(lists):
    h = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(h)
    out = []
    while h:
        v, i, j = heapq.heappop(h)
        out.append(v)
        if j + 1 < len(lists[i]):
            heapq.heappush(h, (lists[i][j + 1], i, j + 1))
    return out
    # or the one-liner: return list(heapq.merge(*lists))
```

---

## Refactor 03 (Hard): Median via re-sorting the window
### Before
```python
def running_medians(nums):
    out = []
    window = []
    for x in nums:
        window.append(x)
        window.sort()                    # O(k log k) every step
        m = len(window) // 2
        out.append(window[m] if len(window) % 2 else (window[m-1] + window[m]) / 2)
    return out
```
### Problems
1. O(n² log n) overall — a full sort per element when only the middle matters.
2. Copies/sorts a growing list: total memory churn.

### After — two heaps
```python
def running_medians(nums):
    lo, hi, out = [], [], []             # lo = max-heap (negated), hi = min-heap
    for x in nums:
        heapq.heappush(lo, -x)
        heapq.heappush(hi, -heapq.heappop(lo))
        if len(hi) > len(lo):
            heapq.heappush(lo, -heapq.heappop(hi))
        out.append(float(-lo[0]) if len(lo) > len(hi) else (-lo[0] + hi[0]) / 2)
    return out
```
O(n log n), O(1) extra state per step — and `lo`/`hi` are always balanced, so both medians live at the roots.

---

## Approach Comparison — different ways to solve it

## Problem: Kth largest element

### Approach 1: Size-k min-heap
```python
h = nums[:k]; heapq.heapify(h)
for x in nums[k:]:
    if x > h[0]: heapq.heapreplace(h, x)
return h[0]
```
**Time O(n log k), space O(k).** Pros: works on streams, doesn't mutate input. Cons: slightly more code.

### Approach 2: `heapq.nlargest(k, nums)[-1]`
**Time O(n log k).** Pros: one line, stdlib-correct. Cons: less control; interviewers may ask you to do it "by hand."

### Approach 3: `sorted(nums)[-k]`
**Time O(n log n), space O(n).** Pros: dead simple. Cons: over-sorts; can't stream; mutates or copies.

### Approach 4: Quickselect
**Average O(n), worst O(n²).** Pros: theoretically fastest, in-place. Cons: partition code is easy to botch under time pressure.

**Winner:** Approach 1 to demonstrate the pattern, Approach 2 in production code. Know quickselect exists; reach for it only if O(n) is demanded.

---

## Problem: Merge k sorted lists

### Approach 1: Heap frontier — `(value, list_i, elem_i)` (above)
**O(N log k), space O(k).** Pros: only k candidates in play; extends to generators/infinite streams.

### Approach 2: `heapq.merge(*lists)`
**O(N log k).** Pros: stdlib, lazy, correct. Cons: none for real code — but it hides the pattern, so know Approach 1 too.

### Approach 3: Pairwise merge (merge 1&2, then with 3, ...)
**O(N·k) naive; O(N log k) if merged tournament-style (divide & conquer).** Pros: no heap needed, cache-friendly. Cons: the naive sequential version degrades to O(N·k) — merging a 1-element list into a million-element list k times is the disaster case.

**Winner:** Approach 1 to learn, Approach 2 to ship.

---

## Problem: Median of a stream

### Approach 1: Two heaps (above)
**O(log n) per element, O(1) median read.** Pros: incremental, online, each median read is O(1). Cons: two-heap invariants take care to keep straight.

### Approach 2: Sorted insert into a list (`bisect.insort`)
**O(n) per insert (the shift), O(1) read.** Pros: five lines with `bisect`. Cons: O(n²) total on n elements — fine for small streams, dead at scale.

**Winner:** Approach 1 — the classic "two heaps" answer and a genuinely hard-to-improvise design; Approach 2 is the pragmatic small-n answer worth mentioning.
