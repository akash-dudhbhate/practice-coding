# Lesson 10 — Sorting

## What you'll learn
- Why sorting unlocks everything (binary search, dedup, merge joins) and
  why comparison sorts can't beat O(n log n)
- The O(n²) trio — bubble, selection, insertion — and when insertion wins
- Merge sort: divide & conquer with a guaranteed O(n log n)
- Quick sort: partitioning, average vs worst case, why it's fast anyway
- Counting sort: linear time when keys are small ints (offset for negatives)
- Python's sorted()/sort(): key functions, tuple keys, stability tricks

## Lesson

Comparison sorting has a hard floor — n! possible orders, ~n log n bits
needed to pick one, so O(n log n) is the best a comparison sort can do.
The skill isn't memorizing Big-O tables; it's matching the algorithm to
the STRUCTURE of your input:

```python
# nearly sorted or tiny?       -> insertion sort wins
# need a guarantee?            -> merge sort (O(n log n) always)
# small integer keys?          -> counting sort (O(n + k))
# production code in Python?   -> sorted() / .sort() — Timsort
```

The two subroutines worth memorizing cold: the two-pointer MERGE (powers
merge sort and inversion counting) and Lomuto PARTITION (powers quicksort
and quickselect).

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here)
1. `easy/p01-insertion-sort.py` — Hand-roll insertion sort in place.
   `[5,2,4,1,3]` → `[1,2,3,4,5]`
2. `easy/p02-sort-custom-key.py` — sorted() with a tuple key: length then
   alpha. `["banana","kiwi","apple","fig","cherry"]` →
   `["fig","kiwi","apple","banana","cherry"]`
3. `easy/p03-merge-two-sorted.py` — Two-pointer merge, the merge-sort
   engine. `[1,3,5]+[2,4,6]` → `[1,2,3,4,5,6]`

### Medium
4. `medium/p01-merge-sort.py` — Split, recurse, merge. O(n log n)
   guaranteed. `merge_sort([5,2,4,1,3])` → `[1,2,3,4,5]`
5. `medium/p02-lomuto-partition.py` — Partition arr[lo..hi] around pivot
   arr[hi] in place; return the pivot's final index.
   `[4,1,3,9,7]` → pivot 7 lands at `3`
6. `medium/p03-sort-multiple-keys.py` — Score desc + name asc: negate the
   number or use stability. `[("bob",75),("amy",90),("cal",90)]` →
   `[("amy",90),("cal",90),("bob",75)]`

### Hard
7. `hard/p01-counting-sort.py` — Count occurrences indexed by
   value−min; emit in order. `[-3,1,-1,2]` → `[-3,-1,1,2]`
8. `hard/p02-count-inversions.py` — Merge-sort augmented to count
   i<j with a[i]>a[j]. `[2,4,1,3,5]` → `3`
9. `hard/p03-sort-nearly-sorted.py` — Each element ≤ k from its spot:
   heap of size k+1, O(n log k). `[6,5,3,2,8,10,9],k=3` → sorted

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python3 check.py easy/p01` to verify; `python3 check.py all` for all.
- `coding-check.md` has the manual checklist; `EXTRA-PRACTICE.md` has drills.
