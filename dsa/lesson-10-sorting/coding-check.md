# Lesson 10 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01 — Insertion sort
- [ ] `insertion_sort([5,2,4,1,3])` mutates to `[1,2,3,4,5]` and returns it
- [ ] `insertion_sort([])` → `[]`; `insertion_sort([1])` → `[1]`
- [ ] `insertion_sort([1,2,3])` → `[1,2,3]` (early exits on sorted input)
- [ ] `insertion_sort([3,-1,0])` → `[-1,0,3]` — handles negatives
- [ ] No `sorted()`/`.sort()` — you implemented shift-and-insert yourself

### p02 — Sort with custom key
- [ ] `sort_by_length(["banana","kiwi","apple","fig","cherry"])` →
      `["fig","kiwi","apple","banana","cherry"]`
- [ ] `sort_by_length(["bb","aa","c"])` → `["c","aa","bb"]` — alpha tiebreak
- [ ] `sort_by_length([])` → `[]`; returns a NEW list (input unchanged)
- [ ] Done with a key function (e.g. `lambda w: (len(w), w)`), not manual loops

### p03 — Merge two sorted arrays
- [ ] `merge_two_sorted([1,3,5],[2,4,6])` → `[1,2,3,4,5,6]`
- [ ] `merge_two_sorted([],[1])` → `[1]`; `([1,2],[])` → `[1,2]`
- [ ] `merge_two_sorted([1,4],[2,3])` → `[1,2,3,4]`; `([1,1],[1])` → `[1,1,1]`
- [ ] Two pointers + one pass — no `sorted(a + b)` shortcut

## Medium

### p01 — Merge sort
- [ ] `merge_sort([5,2,4,1,3])` → `[1,2,3,4,5]`
- [ ] `merge_sort([])` → `[]`; `merge_sort([1])` → `[1]`
- [ ] `merge_sort([3,-1,0,-7])` → `[-7,-1,0,3]`
- [ ] Recursion + the two-pointer merge — no built-in sort anywhere

### p02 — Lomuto partition
- [ ] `lomuto_partition([4,1,3,9,7], 0, 4)` returns `3` with array `[4,1,3,7,9]`
- [ ] `lomuto_partition([3,1,2], 0, 2)` returns `1` with `[1,2,3]`
- [ ] `lomuto_partition([5], 0, 0)` returns `0`
- [ ] `lomuto_partition([2,8,7,1], 0, 3)` → pivot 1 lands at index 0
- [ ] Works on a SUBRANGE (`lo, hi` ≠ whole array) — boundary `i` starts at `lo - 1`

### p03 — Sort by multiple keys
- [ ] `[("bob",75),("amy",90),("cal",90),("dan",60)]` →
      `[("amy",90),("cal",90),("bob",75),("dan",60)]`
- [ ] Equal scores sort by name ASC: `[("zed",50),("ann",50)]` → `[("ann",50),("zed",50)]`
- [ ] `sort_students([])` → `[]`
- [ ] Score DESC + name ASC in one key via negation `(-score, name)`, or two stable passes

## Hard

### p01 — Counting sort
- [ ] `counting_sort([4,2,2,8,3,3,1])` → `[1,2,2,3,3,4,8]` — duplicates kept
- [ ] `counting_sort([-3,1,-1,2])` → `[-3,-1,1,2]` — the value−min offset handles negatives
- [ ] `counting_sort([])` → `[]`; `counting_sort([5])` → `[5]`
- [ ] `counting_sort([-5,-5,-5])` → `[-5,-5,-5]` — all-negative input safe
- [ ] No comparisons / no `sorted()` — counts array + emit loop only

### p02 — Count inversions
- [ ] `count_inversions([2,4,1,3,5])` → `3`
- [ ] `count_inversions([1,2,3])` → `0`; `count_inversions([3,2,1])` → `3`
- [ ] `count_inversions([5,4,3,2,1])` → `10`; `count_inversions([])` → `0`
- [ ] `count_inversions([1,1,1])` → `0` — equal elements are NOT inversions
- [ ] O(n log n) merge-sort adaptation, not O(n²) double loop

### p03 — Sort nearly sorted
- [ ] `sort_nearly_sorted([6,5,3,2,8,10,9], 3)` → `[2,3,5,6,8,9,10]`
- [ ] `sort_nearly_sorted([2,1,3], 1)` → `[1,2,3]`
- [ ] `sort_nearly_sorted([], 3)` → `[]`; `([1], 1)` → `[1]`
- [ ] `sort_nearly_sorted([10,9,8,7,6], 4)` → `[6,7,8,9,10]`
- [ ] Uses a bounded heap of size ≤ k+1 — O(n log k), not a blind full sort

## How to verify

```bash
python3 check.py all          # your files
python3 check.py solutions    # reference solutions (should be 9/9)
```
