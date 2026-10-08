# Lesson 04 — Two Pointers

## What you'll learn
- The two-pointer pattern: two indices walking by rules, never restarting
- Opposite-end pointers: reversal, palindrome, sorted pair-sum
- Same-direction fast/slow pointers: in-place dedup and compaction
- Why sorted input unlocks O(n) time + O(1) space (vs hashing's O(n) space)
- When NOT to use two pointers (unsorted data, order-dependent answers)
- Scaling up: 3-sum, 4-sum, container, rain water, back-merge

## Lesson

A nested loop re-examines everything — O(n²). Two pointers exploit structure:
each comparison lets you discard a whole slice of the search space.

```python
L, R = 0, len(nums) - 1
while L < R:
    s = nums[L] + nums[R]
    if s == target:
        return [L, R]
    if s < target:
        L += 1        # sorted input: nums[L] too small for everyone
    else:
        R -= 1        # nums[R] too big for everyone
```

The other half of the lesson is read/write pointers — `fast` scans, `slow`
writes the next keeper — which powers every in-place compaction problem.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here)
1. `easy/p01-reverse-in-place.py` — Swap ends, walk inward; mutate the list.
   `[1,2,3,4]` → `[4,3,2,1]`
2. `easy/p02-palindrome-check.py` — Skip non-alphanumeric, compare ends.
   `"A man, a plan, a canal: Panama"` → `True`
3. `easy/p03-pair-sum-sorted.py` — Pair summing to target in sorted array.
   `pair_sum_sorted([2,7,11,15], 9)` → `[0,1]`

### Medium
4. `medium/p01-remove-duplicates.py` — In-place dedup of sorted array;
   return new length k with uniques in nums[:k]. `[1,1,2]` → `2`, `[1,2]`
5. `medium/p02-container-most-water.py` — Max min(h[i],h[j])·(j-i); move
   the shorter side. `[1,8,6,2,5,4,8,3,7]` → `49`
6. `medium/p03-three-sum.py` — All unique triplets summing to 0.
   `three_sum([-1,0,1,2,-1,-4])` → `[[-1,-1,2],[-1,0,1]]`

### Hard
7. `hard/p01-trapping-rain-water.py` — Water = min(maxL,maxR)−h[i], carried
   by two pointers. `[0,1,0,2,1,0,1,3,2,1,2,1]` → `6`
8. `hard/p02-merge-sorted-in-place.py` — Merge nums2 into nums1's back-buffer,
   writing from the end. `[1,2,3,0,0,0]+[2,5,6]` → `[1,2,2,3,5,6]`
9. `hard/p03-four-sum.py` — All unique quadruplets summing to target.
   `four_sum([1,0,-1,0,-2,2], 0)` → `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python3 check.py easy/p01` to verify; `python3 check.py all` for all.
- `coding-check.md` has the manual checklist; `EXTRA-PRACTICE.md` has drills.
