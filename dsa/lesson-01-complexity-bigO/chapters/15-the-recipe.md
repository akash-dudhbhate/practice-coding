# 15 — The Recipe: analyze any code in 5 steps

> 5-minute read. Ties every chapter together.

## The 5 steps

When someone hands you code and asks "what's the complexity?":

1. **Find n** — what grows? (usually input size)
2. **Count the dominant work** — innermost loop, hidden scans (`in`,
   `count`, `index`, `max`, `sum` on a list), recursive calls.
3. **Nested? multiply. Side-by-side? add.** → combine the parts.
4. **Drop constants and small terms** → state worst case.
5. **State space too** — what new memory does it allocate?

## Watch the recipe work — three increasingly-tricky pieces

**Piece A:**
```python
def analyze(nums, k):
    seen = set()                 # O(1) setup
    for x in nums:               # n rounds
        if k - x in seen:        # O(1) — set lookup, not a scan
            return True
        seen.add(x)              # O(1) amortized
    return False
```
- Dominant work: the n-round loop, each round O(1).
- Time: **O(n)**. Space: `seen` up to n elements → **O(n)**.

**Piece B:**
```python
def find_dup(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return (i, j)
    return None
```
- Inner runs n−1, n−2, ... 1 → total n²/2 → drop constant → **O(n²)** time.
- Space: **O(1)** — no new structures, just two index variables.
- Worst case: no duplicates → full pair scan.

**Piece C — read it before checking the answer:**
```python
def mystery(nums):
    nums = sorted(nums)          # what class is this? (remember ch.10)
    for x in nums:
        print(x)
```
- `sorted` = O(n log n); loop = O(n). Add: n log n + n → keep bigger →
  **O(n log n)**. Space: `sorted` returns a new list → **O(n)**.

## Practice ladder (do these before moving on)

For each snippet, say Big-O out loud, then verify by reasoning:

1. `sum(nums)` → ?
2. `for x in nums: for y in nums:` → ?
3. `while lo <= hi: mid = (lo+hi)//2 ...` (binary search) → ?
4. `for x in nums: if x in some_set:` → ?
5. `for x in nums: if x in some_list:` → ?  ← trap!

<details><summary>Answers</summary>
1. O(n) — hidden pass. 2. O(n²). 3. O(log n) — halving.
4. O(n) — set `in` is O(1) inside the n-loop. 5. **O(n²)** — list `in`
scans the whole list per iteration. #4 vs #5 is THE classic interview trap.
</details>

## What you now know

You can: count steps by hand, name the growth shape (O(1)/O(n)/O(n²)/O(log n)/
O(n log n)/O(2ⁿ)), tell nested from sequential, spot hidden loops, state
worst case + space. **That's the whole lesson.** The problems in
`easy/`→`medium/`→`hard/` now drill exactly this.

---

**← Prev** [14 — Amortized](14-amortized-append.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01` next.
