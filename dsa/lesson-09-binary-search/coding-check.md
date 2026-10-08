# Lesson 09 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01 — Classic binary search
- [ ] `binary_search([-1,0,3,5,9,12], 9)` returns `4`
- [ ] `binary_search([-1,0,3,5,9,12], 2)` returns `-1`
- [ ] `binary_search([5], 5)` returns `0`; `binary_search([], 1)` returns `-1`
- [ ] `binary_search([1,2,3], 1)` returns `0` — first index reachable
- [ ] Uses `while lo <= hi` with `lo = mid + 1` / `hi = mid - 1` — no `mid` update that can stall

### p02 — First occurrence
- [ ] `first_occurrence([1,2,2,2,3,4], 2)` returns `1`, not 2 or 3
- [ ] `first_occurrence([1,2,2,2,3,4], 9)` returns `-1`
- [ ] `first_occurrence([2,2,2], 2)` returns `0`; `first_occurrence([], 3)` returns `-1`
- [ ] On a match you record mid AND keep searching left (`hi = mid - 1`)

### p03 — Search insert position
- [ ] `search_insert([1,3,5,6], 5)` returns `2` (found case)
- [ ] `search_insert([1,3,5,6], 2)` returns `1`; `...7` → `4`; `...0` → `0`
- [ ] `search_insert([1], 0)` returns `0`
- [ ] `hi` starts at `len(nums)` (past-the-end is a legal answer), loop is `lo < hi` with `hi = mid`

## Medium

### p01 — Integer sqrt
- [ ] `my_sqrt(4)` → `2`; `my_sqrt(8)` → `2`; `my_sqrt(15)` → `3`
- [ ] `my_sqrt(0)` → `0`; `my_sqrt(1)` → `1`
- [ ] `my_sqrt(2147395599)` → `46339` — no float math, no `** 0.5`
- [ ] Searches the RANGE [0, x] for the last `mid` with `mid*mid <= x`

### p02 — Min ship capacity
- [ ] `min_ship_capacity([1,2,3,4,5,6,7,8,9,10], 5)` returns `15`
- [ ] `min_ship_capacity([3,2,2,4,1,4], 3)` returns `6`
- [ ] `min_ship_capacity([1,2,3,1,1], 4)` returns `3`; `([5], 1)` → `5`
- [ ] Bounds are `lo = max(weights)`, `hi = sum(weights)` — not 0/1
- [ ] `feasible(cap)` greedily fills days in ORDER — no sorting, no reordering packages

### p03 — Koko eating bananas
- [ ] `min_eating_speed([3,6,7,11], 8)` returns `4`
- [ ] `min_eating_speed([30,11,23,4,20], 5)` returns `30`; `(..., 6)` → `23`
- [ ] `min_eating_speed([1], 1)` returns `1`
- [ ] Hours computed as `ceil(p/k)` = `(p + k - 1) // k`, and the predicate is monotone in k

## Hard

### p01 — Search rotated sorted array
- [ ] `search_rotated([4,5,6,7,0,1,2], 0)` returns `4`; `(..., 3)` → `-1`
- [ ] `search_rotated([1], 0)` → `-1`; `([1,3], 3)` → `1`; `([5,1,3], 5)` → `0`
- [ ] Each step identifies the sorted half and checks target against its RANGE
- [ ] O(log n) — no `nums.index`, no linear scan

### p02 — Find min in rotated
- [ ] `find_min_rotated([3,4,5,1,2])` → `1`; `([4,5,6,7,0,1,2])` → `0`
- [ ] `find_min_rotated([11,13,15,17])` → `11` (zero rotation works)
- [ ] `find_min_rotated([2,1])` → `1`; `([1])` → `1`
- [ ] Uses `hi = mid` (NOT `mid - 1`) when `nums[mid] <= nums[hi]` — mid might BE the min

### p03 — Find a peak element
- [ ] `find_peak([1,2,3,1])` returns `2`
- [ ] `find_peak([1,2,1,3,5,6,4])` returns `1` or `5` (either peak accepted)
- [ ] `find_peak([1])` → `0`; `([1,2])` → `1`; `([3,2,1])` → `0`
- [ ] Compares `nums[mid]` to `nums[mid+1]` only; loop is `lo < hi` so `mid+1` never overflows

## How to verify

```bash
python3 check.py all          # your files
python3 check.py solutions    # reference solutions (should be 9/9)
```
