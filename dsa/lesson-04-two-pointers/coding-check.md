# Lesson 04 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01 — Reverse in place
- [ ] `reverse_in_place([1,2,3,4])` mutates the list to `[4,3,2,1]` and returns it
- [ ] `reverse_in_place([1,2,3])` → `[3,2,1]` (odd length ok)
- [ ] `reverse_in_place([])` → `[]`, `reverse_in_place([5])` → `[5]`
- [ ] No `arr[::-1]`, `reversed()`, or new list — swaps only

### p02 — Palindrome check
- [ ] `is_palindrome("A man, a plan, a canal: Panama")` returns `True`
- [ ] `is_palindrome("race a car")` returns `False`
- [ ] `is_palindrome(" ")` returns `True`
- [ ] `is_palindrome("0P")` returns `False` ('0' is alnum, '0' != 'p')
- [ ] Ignores case and skips non-alphanumeric from BOTH ends

### p03 — Pair sum sorted
- [ ] `pair_sum_sorted([2,7,11,15], 9)` returns `[0,1]`
- [ ] `pair_sum_sorted([1,2,4,7,11], 9)` returns `[1,3]`
- [ ] `pair_sum_sorted([1,3,5], 10)` returns `[]`
- [ ] Move L when sum too small, R when too big — not both

## Medium

### p01 — Remove duplicates (in place)
- [ ] `[1,1,2]` → returns `2`, prefix `[1,2]`
- [ ] `[0,0,1,1,1,2,2,3,3,4]` → returns `5`, prefix `[0,1,2,3,4]`
- [ ] `[]` → `0`; `[1,2,3]` → `3`
- [ ] Writes into `nums` itself — no second list

### p02 — Container with most water
- [ ] `max_area([1,8,6,2,5,4,8,3,7])` returns `49`
- [ ] `max_area([1,1])` returns `1`
- [ ] `max_area([4,3,2,1,4])` returns `16`
- [ ] Always moves the SHORTER side's pointer

### p03 — 3-sum
- [ ] `three_sum([-1,0,1,2,-1,-4])` returns `[[-1,-1,2],[-1,0,1]]`
- [ ] `three_sum([0,1,1])` returns `[]`
- [ ] `three_sum([0,0,0,0])` returns `[[0,0,0]]` — no duplicate triplets
- [ ] Sorted first; duplicate i values and duplicate pairs skipped

## Hard

### p01 — Trapping rain water
- [ ] `trap([0,1,0,2,1,0,1,3,2,1,2,1])` returns `6`
- [ ] `trap([4,2,0,3,2,5])` returns `9`
- [ ] `trap([])` returns `0`; `trap([2,0,2])` returns `2`
- [ ] Process the side with the SMALLER running max

### p02 — Merge sorted in place
- [ ] `[1,2,3,0,0,0] m=3` + `[2,5,6] n=3` → nums1 becomes `[1,2,2,3,5,6]`
- [ ] `[0] m=0` + `[1] n=1` → `[1]`
- [ ] `[4,5,6,0,0,0] m=3` + `[1,2,3] n=3` → `[1,2,3,4,5,6]`
- [ ] Fills from the back — no forward overwrite of unread values

### p03 — 4-sum
- [ ] `four_sum([1,0,-1,0,-2,2], 0)` returns `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`
- [ ] `four_sum([2,2,2,2,2], 8)` returns `[[2,2,2,2]]`
- [ ] `four_sum([], 0)` returns `[]`
- [ ] Duplicate i, j, and pair values skipped — no repeated quadruplets

## How to verify

```bash
python3 check.py all          # your files
python3 check.py solutions    # reference solutions (should be 9/9)
```
