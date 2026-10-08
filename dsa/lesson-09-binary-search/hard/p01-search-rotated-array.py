"""
LESSON 09 — Binary Search
HARD P01 — Search in Rotated Sorted Array
============================================

CONCEPT:
  A rotated sorted array is two sorted halves glued together. At
  any mid, AT LEAST ONE side of [lo, hi] is still fully sorted —
  check which, then ask "is target inside that sorted side's
  range?" If yes, search it; if no, it must be in the other half.

PROBLEM:
  Write `search_rotated(nums: list, target: int) -> int`: the array
  was sorted ascending, then rotated at an unknown pivot
  (e.g. [0,1,2,4,5,6,7] → [4,5,6,7,0,1,2]). All values are unique.
  Return the index of target, or -1. Must be O(log n).

TRY THIS INPUT:
  ```python
  print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))
  print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))
  print(search_rotated([1], 0))
  ```

EXPECTED OUTPUT:
  ```
  4
  -1
  -1
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
