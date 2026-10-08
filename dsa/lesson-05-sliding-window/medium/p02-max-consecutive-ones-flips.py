"""
LESSON 05 — Sliding Window
MEDIUM P02 — Max Consecutive Ones With K Flips
============================================

CONCEPT:
  Reframe "flip up to k zeros" as a window problem: find the LONGEST
  window containing at most k zeros. The window state is a single
  counter — zeros inside the window. Expand right; while zeros > k,
  shrink left (decrementing the counter when a zero leaves).

PROBLEM:
  Write a function `longest_ones(nums: list[int], k: int) -> int` that
  returns the maximum number of consecutive 1s achievable after
  flipping at most k 0s to 1s. nums contains only 0s and 1s.

TRY THIS INPUT:
  ```python
  print(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2))
  print(longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
  print(longest_ones([1,1,1], 0))
  print(longest_ones([0,0,0], 1))
  ```

EXPECTED OUTPUT:
  ```
  6
  10
  3
  1
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
