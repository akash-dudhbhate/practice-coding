"""
LESSON 10 — Sorting
HARD P02 — Count Inversions via Merge Sort
============================================

CONCEPT:
  An inversion is a pair i < j with arr[i] > arr[j] — "how far is
  this from sorted?" During merge sort, when the merge step takes
  an element from the RIGHT half while elements remain in the
  LEFT, every leftover left element forms an inversion with it.
  Count those mid-merge: O(n log n) instead of O(n^2) pair checks.

PROBLEM:
  Write `count_inversions(arr: list) -> int`: the number of pairs
  (i, j) with i < j and arr[i] > arr[j]. Must be O(n log n) —
  adapt merge sort so the merge step also counts.

TRY THIS INPUT:
  ```python
  print(count_inversions([2, 4, 1, 3, 5]))   # (2,1) (4,1) (4,3)
  print(count_inversions([1, 2, 3]))
  print(count_inversions([5, 4, 3, 2, 1]))   # every pair
  ```

EXPECTED OUTPUT:
  ```
  3
  0
  10
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
