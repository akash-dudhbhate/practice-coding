"""
LESSON 09 — Binary Search
EASY P02 — First Occurrence (Lower Bound)
============================================

CONCEPT:
  When the array has duplicates, "find the target" isn't enough —
  you want the FIRST index holding it. When nums[mid] >= target,
  the answer is mid or somewhere left, so record mid as a
  candidate and keep searching left (hi = mid - 1).

PROBLEM:
  Write a function `first_occurrence(nums: list, target: int) -> int`
  that returns the FIRST index where `target` appears in the sorted
  array `nums`, or -1 if it never appears.

TRY THIS INPUT:
  ```python
  print(first_occurrence([1, 2, 2, 2, 3, 4], 2))
  print(first_occurrence([1, 2, 2, 2, 3, 4], 9))
  print(first_occurrence([2, 2, 2], 2))
  ```

EXPECTED OUTPUT:
  ```
  1
  -1
  0
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
