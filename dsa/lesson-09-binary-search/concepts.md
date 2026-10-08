# Lesson 09 — Concepts Explained (Binary Search)

> Read this before solving the problems. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** · **What goes wrong** without it.
> Then a worked example with real numbers, code, and expected output.

---

## What Binary Search Is — Halving the Search Space

**What it is:** On a SORTED collection, don't scan left to right — probe the
middle. If `nums[mid]` is too small, everything at or before mid is dead;
search only the right half. Too big? Search only the left half. Each
comparison throws away HALF the remaining candidates.

```
nums = [1, 3, 5, 7, 9, 11, 13], target = 7
        lo      mid       hi       mid=5 <7 -> throw away left half
                    [7, 9, 11, 13]  mid=9 >7 -> throw away right half
                    [7]             found, 3 probes instead of 4 scans
```

**Why it exists:** Linear scan is O(n) — a billion-element array costs a
billion comparisons. Halving gives O(log n): log2(10⁹) ≈ 30 probes. It's the
same reason you open a dictionary near the middle for "M", not page 1 — and
the guess-a-number game ("higher/lower") children play.

**Where it's used:** Every sorted-container lookup (Python's `bisect`, C++'s
`lower_bound`, database B-tree indexes), version bisection (`git bisect`),
numeric root-finding, and the "binary search the answer" interview pattern.

**What goes wrong without it:**
- Scanning a sorted array: 10⁷ elements → ~10⁷ comparisons instead of ~24 →
  timeouts on "find in sorted" problems.
- Trying to binary search UNSORTED data — the "too small → go right" logic
  has no basis; you get silent wrong answers, not errors.

**Worked example (real numbers):** `binary_search([1,3,5,7,9], 3)`

```
lo=0 hi=4  mid=2  nums[2]=5 > 3  -> hi=1
lo=0 hi=1  mid=0  nums[0]=1 < 3  -> lo=1
lo=1 hi=1  mid=1  nums[1]=3 ==   -> return 1
```

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 3))
print(binary_search([1, 3, 5, 7, 9], 4))
```

Expected output:
```
1
-1
```

---

## The Canonical Template — and the Infinite-Loop Traps

**What it is:** Binary search has exactly three moving parts. Get any one
wrong and the loop either hangs forever or misses edge elements:

```python
lo, hi = 0, len(nums) - 1     # [lo, hi] = candidates still alive, INCLUSIVE
while lo <= hi:               # a range that exists (lo==hi is one element)
    mid = (lo + hi) // 2      # rounds DOWN toward lo
    if nums[mid] == target: return mid
    if nums[mid] < target: lo = mid + 1   # exclude mid itself
    else: hi = mid - 1                    # exclude mid itself
```

The invariant: the answer, if it exists, is always inside `[lo, hi]`. Every
update must SHRINK the range — `lo = mid + 1` / `hi = mid - 1`, never
`lo = mid` or `hi = mid` in this template.

**Why it exists:** `mid` rounds toward `lo`. If you wrote `lo = mid` while
`lo < hi`, then `lo=3, hi=4` gives `mid=3` → `lo=3` forever — infinite loop.
That's why the inclusive template pairs `<=` with `mid ± 1`.

**Where it's used:** Every binary-search variant is this template with a
different "which side is dead" rule. Memorize the shape, derive the rule.

**What goes wrong without it:**
- `lo = mid` (or `hi = mid`) in the inclusive template → infinite loop on
  two-element ranges. THE most common binary search bug.
- `while lo < hi` combined with `hi = mid - 1` → skips the last candidate;
  "target at the only remaining index" is never checked.
- Off-by-one on `hi = len(nums)` instead of `len(nums) - 1` in the classic
  template → IndexError on the first probe of an edge-case array.

**Worked example (real numbers):** two-element trap, `[1, 3]`, target `3`.

```
WRONG:  lo=0 hi=1 mid=0 nums[0]=1<3 -> lo=mid=0   <- lo never moves, hangs
RIGHT:  lo=0 hi=1 mid=0 nums[0]=1<3 -> lo=1
        lo=1 hi=1 mid=1 nums[1]=3   -> return 1
```

Expected output: `1`

---

## Lower Bound & Upper Bound — Searching a Boundary, Not a Value

**What it is:** Two variants that always return a POSITION, found or not:

- **Lower bound** = first index `i` where `nums[i] >= target`. If target
  exists, it's the first occurrence; if not, it's the insertion slot.
- **Upper bound** = first index `i` where `nums[i] > target` — one past the
  last occurrence.

```python
def lower_bound(nums, target):       # first i: nums[i] >= target
    lo, hi = 0, len(nums)            # hi can be len(nums) — a valid answer
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid                 # mid might be the answer — keep it
    return lo
```

Note the DIFFERENT loop contract: `lo < hi` + `hi = mid` is safe here
precisely because `mid` rounds toward `lo` and `lo < hi` guarantees
`mid != lo` can't stall (when lo+1 == hi, mid == lo, so `lo` moves to hi).

**Why it exists:** "Where does this value belong?" matters more than "does it
exist" — for duplicate runs, insertion slots, and counting (`upper - lower`
= frequency of target). Python ships this as `bisect.bisect_left` /
`bisect_right`.

**Where it's used:** First/last occurrence, search-insert-position, counting
occurrences of a value, "smallest element >= x" lookups, and the entire
"binary search the answer" family (lower bound on a predicate).

**What goes wrong without it:**
- Mixing templates — `lo <= hi` together with `hi = mid` → infinite loop
  when `lo == hi` (mid = lo = hi, and `hi = mid` moves nothing).
- Returning `nums[lo]` without checking `lo < len(nums)` — lower bound can
  legally return `len(nums)` ("target goes past the end").
- `bisect_right` vs `bisect_left` confusion: `bisect_left` = first >= ,
  `bisect_right` = first > .

**Worked example (real numbers):** `lower_bound([1,2,2,2,4], 2)`

```
lo=0 hi=5  mid=2  nums[2]=2 >= 2  -> hi=2
lo=0 hi=2  mid=1  nums[1]=2 >= 2  -> hi=1
lo=0 hi=1  mid=0  nums[0]=1 < 2   -> lo=1
lo=1 hi=1 -> return 1  (first index holding 2)
```

```python
from bisect import bisect_left, bisect_right

nums = [1, 2, 2, 2, 4]
print(bisect_left(nums, 2))              # lower bound
print(bisect_right(nums, 2))             # upper bound
print(bisect_right(nums, 2) - bisect_left(nums, 2))  # count of 2s
print(bisect_left(nums, 3))              # insert slot for missing 3
```

Expected output:
```
1
4
3
4
```

---

## Binary Search the Answer — When the Search Space Isn't an Array

**What it is:** Sometimes there's no array at all — the "search space" is a
range of possible ANSWERS: a capacity, a speed, a minimum feasible value.
If you can write a monotone feasibility check — `feasible(x)` that's
false...false true...true (or the mirror image) — you can binary search x.

```python
lo, hi = LOWEST_POSSIBLE, HIGHEST_POSSIBLE   # answer range, not indices!
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid             # works — try something smaller
    else:
        lo = mid + 1         # fails — need more
return lo                    # smallest feasible answer
```

Three steps, every time:
1. **Bound the answer** — e.g. capacity ∈ [max(weights), sum(weights)].
2. **Write `feasible(x)`** — simulate/greedy-check if x works. This is an
   O(n) subroutine inside the search.
3. **Confirm monotonicity** — bigger x can never flip the answer back to
   infeasible. No monotone predicate, no binary search.

**Why it exists:** Brute force tries every candidate answer — O(range·n) with
range up to 10⁹ → hopeless. Feasibility is monotone, so log(range) checks
suffice: ~30 simulation passes instead of billions.

**Where it's used:** Minimum ship capacity, Koko's bananas, minimum time to
complete tasks, "split array largest sum", aggressive cows / magnetic force —
any "find the smallest x such that condition holds" phrasing.

**What goes wrong without it:**
- Wrong bounds: `lo = 1` when the answer must be ≥ `max(weights)` — the ship
  can't carry the heaviest box at any capacity below it. `feasible` may also
  crash or lie about small capacities.
- `feasible` not monotone: e.g., a check that accidentally gets HARDER as x
  grows — binary search then narrows the wrong way, wrong answer, no error.
- Integer vs float confusion: these problems want integer answers; use
  integer mid and `lo < hi` convergence, not epsilon loops.

**Worked example (real numbers):** `min_ship_capacity([1..10], days=5)`

```
lo=10 hi=55
mid=32: feasible? loads [1..10] greedy -> needs 2 days <= 5 -> hi=32
mid=21: needs 3 days -> hi=21
mid=15: loads [1,2,3,4,5]=15 [6,7]=13 [8]=8 [9]=9 [10]=10 -> 5 days -> hi=15
mid=12: needs 6 days -> lo=13
mid=14: needs 6 days -> lo=15
lo==hi==15 -> return 15
```

Expected output: `15`

---

## Rotated Sorted Array — Sortedness with a Scar

**What it is:** `[0,1,2,4,5,6,7]` rotated at index 3 → `[4,5,6,7,0,1,2]`.
Not sorted globally, BUT at every probe point at least one half of
`[lo, hi]` is fully sorted. Use that: identify the sorted half, check if
target is inside its value range — inside → search it, outside → the other
half must have it.

```python
if nums[lo] <= nums[mid]:                 # left half sorted
    if nums[lo] <= target < nums[mid]: hi = mid - 1
    else: lo = mid + 1
else:                                     # right half sorted
    if nums[mid] < target <= nums[hi]: lo = mid + 1
    else: hi = mid - 1
```

**Why it exists:** It looks like binary search should be impossible — the
precondition is broken. The rescue is that sortedness survives *locally*:
one half is always clean, and a clean half lets you decide direction with a
range check instead of a single comparison.

**Where it's used:** Find target in rotated array, find the rotation point
(= index of the minimum), search in "almost sorted" arrays. A favorite
because it tests whether you can adapt the invariant, not just recite it.

**What goes wrong without it:**
- Comparing `nums[mid]` to `target` only — rotation means "mid < target"
  doesn't tell you which side target is on. You need the sorted-half test.
- For the find-minimum variant: `nums[mid] > nums[hi]` → min is RIGHT of mid
  (`lo = mid + 1`); else min is AT mid or left (`hi = mid` — not `mid - 1`,
  or you'd skip the minimum itself).
- Using `nums[mid] < nums[lo]` vs `nums[mid] > nums[hi]` inconsistently —
  pick ONE anchor (comparing to `nums[hi]` is the common convention).

**Worked example (real numbers):** `search_rotated([4,5,6,7,0,1,2], 0)`

```
lo=0 hi=6 mid=3 nums[3]=7   left [4..7] sorted, 0 not in [4,7) -> lo=4
lo=4 hi=6 mid=5 nums[5]=1   right? nums[4]=0 <= nums[5]=1 left sorted,
                            0 in [0,1) -> hi=4
lo=4 hi=4 mid=4 nums[4]=0 == -> return 4
```

Expected output: `4`

---

## Binary Search Without Sortedness — Peaks and Slopes

**What it is:** Binary search needs a *monotone elimination rule*, not
literally a sorted array. In find-a-peak: if `nums[mid] < nums[mid+1]`
you're on an uphill slope and a peak MUST exist to the right (the array
falls off -inf at the end); otherwise a peak exists at mid or left. Either
way you can discard a half.

**Why it exists:** It breaks the mental model "binary search = sorted array"
and replaces it with the real rule: "binary search = a guaranteed way to
kill half the candidates each step."

**Where it's used:** Peak element, bitonic-array maximum, valley finding —
any problem where a local comparison implies global direction.

**What goes wrong without it:**
- Checking both neighbors of mid — you only need ONE (`nums[mid+1]`) because
  -inf boundaries plus `nums[i] != nums[i+1]` guarantee the slope argument.
- `while lo <= hi` style here goes out of bounds reading `nums[mid+1]`; the
  `lo < hi` contract keeps mid away from the last index.

---

## Quick Reference

| Problem shape | Search space | Monotone rule | Return |
|---|---|---|---|
| exact match (sorted) | indices [0, n-1] | nums[mid] vs target | index or -1 |
| first occurrence / insert slot | indices [0, n] | nums[mid] >= target → hi=mid | lower bound |
| search the answer | answer range [lo, hi] | feasible(mid) → hi=mid | smallest feasible |
| rotated find | indices [0, n-1] | which half is sorted + range check | index or -1 |
| rotated min | indices [0, n-1] | nums[mid] > nums[hi] → right | nums[lo] at lo==hi |
| peak element | indices [0, n-1] | nums[mid] < nums[mid+1] → right | any peak index |
