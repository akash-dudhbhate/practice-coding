"""
LESSON 05 — Sliding Window
MEDIUM P03 — Minimum Size Subarray Sum
============================================

CONCEPT:
  Variable window with the INVERTED loop: you want the SHORTEST valid
  window, so while the window satisfies `sum >= target`, record its
  length and shrink — squeeze it smaller. When the sum drops below
  target, go back to expanding right.

PROBLEM:
  Write a function `min_subarray_len(target: int, nums: list[int]) -> int`
  that returns the length of the smallest contiguous subarray whose
  sum is >= target. Return 0 if no such subarray exists.
  (All numbers are positive — that's what makes the window valid to shrink.)

TRY THIS INPUT:
  ```python
  print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))
  print(min_subarray_len(4, [1, 4, 4]))
  print(min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]))
  print(min_subarray_len(15, [1, 2, 3, 4, 5]))
  ```

EXPECTED OUTPUT:
  ```
  2
  1
  0
  5
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
