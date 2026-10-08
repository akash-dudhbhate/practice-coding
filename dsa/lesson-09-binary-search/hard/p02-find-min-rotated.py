"""
LESSON 09 — Binary Search
HARD P02 — Find Minimum in Rotated Sorted Array
============================================

CONCEPT:
  The minimum is the ONE element smaller than its left neighbor —
  the pivot point. Compare nums[mid] to nums[hi]: if mid > hi,
  the dip is strictly right of mid (lo = mid + 1); otherwise the
  minimum is at mid or to its left (hi = mid). Loop until lo == hi.

PROBLEM:
  Write `find_min_rotated(nums: list) -> int`: a sorted-ascending
  array of UNIQUE values, rotated at an unknown pivot (possibly
  rotated 0 times — already sorted). Return the minimum element.
  Must be O(log n).

TRY THIS INPUT:
  ```python
  print(find_min_rotated([3, 4, 5, 1, 2]))
  print(find_min_rotated([4, 5, 6, 7, 0, 1, 2]))
  print(find_min_rotated([11, 13, 15, 17]))
  ```

EXPECTED OUTPUT:
  ```
  1
  0
  11
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
