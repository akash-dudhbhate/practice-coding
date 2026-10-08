"""
LESSON 02 — Arrays & Strings
HARD P02 — Max Subarray (Kadane)
============================================

CONCEPT:
  Kadane's algorithm: carry `cur` = best subarray sum that must END at
  this index. At each element either extend (cur + x) or restart (x).
  A negative prefix can only hurt — dropping it is always free.
  O(n) time, O(1) space — your first taste of DP.

PROBLEM:
  Write a function `max_subarray(nums: list) -> int` returning the
  maximum sum of any contiguous non-empty subarray. Must handle
  all-negative input correctly (return the largest element, not 0).

TRY THIS INPUT:
  ```python
  print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
  print(max_subarray([5, 4, -1, 7, 8]))
  print(max_subarray([-3, -1, -2]))
  ```

EXPECTED OUTPUT:
  ```
  6
  23
  -1
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
