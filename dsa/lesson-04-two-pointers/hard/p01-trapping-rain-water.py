"""
LESSON 04 — Two Pointers
HARD P01 — Trapping Rain Water
============================================

CONCEPT:
  Water trapped above index i = min(max_height_left, max_height_right)
  - height[i]. Two pointers carry running maxima from both ends: keep
  left_max and right_max; process whichever side's max is SMALLER —
  that side's bound is already known, so its water is final. Move that
  pointer inward. O(n) time, O(1) space (vs O(n) prefix arrays).

PROBLEM:
  Write a function `trap(height: list) -> int` returning the total
  water trapped between the bars after rain.

TRY THIS INPUT:
  ```python
  print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
  print(trap([4, 2, 0, 3, 2, 5]))
  print(trap([]))
  ```

EXPECTED OUTPUT:
  ```
  6
  9
  0
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
