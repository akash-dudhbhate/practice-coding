"""
LESSON 09 — Binary Search
EASY P01 — Classic Binary Search
============================================

CONCEPT:
  On a SORTED array, compare the middle element to the target.
  Too big? Throw away the right half. Too small? Throw away the
  left half. Each step halves the search space → O(log n).

PROBLEM:
  Write a function `binary_search(nums: list, target: int) -> int`
  that returns the index of `target` in the sorted array `nums`,
  or -1 if it is not present.

TRY THIS INPUT:
  ```python
  print(binary_search([-1, 0, 3, 5, 9, 12], 9))
  print(binary_search([-1, 0, 3, 5, 9, 12], 2))
  print(binary_search([5], 5))
  ```

EXPECTED OUTPUT:
  ```
  4
  -1
  0
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
