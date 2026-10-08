# Lesson 09 — Binary Search

## What you'll learn
- The halving intuition: O(log n) means ~30 probes in a billion elements
- The canonical `lo <= hi` + `mid ± 1` template and its infinite-loop traps
- Lower bound / upper bound — searching a boundary instead of a value
- "Binary search the answer": capacity, speed, and feasibility problems
- Sortedness-free variants: rotated arrays, peak elements

## Lesson

Sorted input turns a linear scan into a halving machine — every comparison
deletes half the remaining candidates:

```python
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        lo = mid + 1        # left half is dead
    else:
        hi = mid - 1        # right half is dead
```

The deeper skill: the "array" doesn't have to be an array. Any monotone
predicate over a bounded range — "is capacity C enough?", "does speed k
finish in time?" — is a binary-searchable space.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here)
1. `easy/p01-classic-binary-search.py` — Index of target or -1.
   `binary_search([-1,0,3,5,9,12], 9)` → `4`
2. `easy/p02-first-occurrence.py` — First index of target (lower bound
   with a not-found case). `first_occurrence([1,2,2,2,3,4], 2)` → `1`
3. `easy/p03-search-insert-position.py` — Where target is or belongs.
   `search_insert([1,3,5,6], 2)` → `1`, `search_insert([1,3,5,6], 7)` → `4`

### Medium
4. `medium/p01-sqrt-binary-search.py` — floor(sqrt(x)) on the answer range
   [0, x], no math.sqrt. `my_sqrt(8)` → `2`
5. `medium/p02-min-ship-capacity.py` — Search capacity C in
   [max, sum]; simulate greedy loading.
   `min_ship_capacity([1..10], 5)` → `15`
6. `medium/p03-koko-eating-bananas.py` — Search speed k in [1, max];
   hours = sum(ceil(pile/k)). `min_eating_speed([3,6,7,11], 8)` → `4`

### Hard
7. `hard/p01-search-rotated-array.py` — One half is always sorted; check
   which contains target. `search_rotated([4,5,6,7,0,1,2], 0)` → `4`
8. `hard/p02-find-min-rotated.py` — The minimum is the rotation scar;
   compare mid to hi. `find_min_rotated([3,4,5,1,2])` → `1`
9. `hard/p03-find-peak-element.py` — No sortedness at all: uphill slope
   guarantees a peak on the right. `find_peak([1,2,3,1])` → `2`

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python3 check.py easy/p01` to verify; `python3 check.py all` for all.
- `coding-check.md` has the manual checklist; `EXTRA-PRACTICE.md` has drills.
