"""
LESSON 05 — Sliding Window
EASY P01 — Max Sum of a Fixed Window
============================================

CONCEPT:
  A FIXED-size window: the length k never changes. Build the first
  window's sum once, then slide — each slide adds the element entering
  on the right and subtracts the element leaving on the left. No
  re-summing, so each step costs O(1).

PROBLEM:
  Write a function `max_sum_k(nums: list[int], k: int) -> int` that
  returns the maximum sum of any contiguous subarray of length k.
  You may assume 1 <= k <= len(nums).

TRY THIS INPUT:
  ```python
  print(max_sum_k([2, 1, 5, 1, 3, 2], 3))
  print(max_sum_k([1, 2, 3, 4, 5], 2))
  print(max_sum_k([5], 1))
  ```

EXPECTED OUTPUT:
  ```
  9
  9
  5
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
