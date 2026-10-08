"""
LESSON 04 — Two Pointers
MEDIUM P02 — Container With Most Water
============================================

CONCEPT:
  Opposite-end pointers + greedy elimination. Area between L and R is
  min(h[L], h[R]) * (R - L). The SHORTER side caps the height — moving
  the taller pointer inward can only shrink width with no chance of
  more height, so it's a dead end. Always move the shorter side.

PROBLEM:
  Write a function `max_area(height: list) -> int` returning the
  maximum water a container formed by two vertical lines at indices
  i, j can hold: min(height[i], height[j]) * (j - i).

TRY THIS INPUT:
  ```python
  print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
  print(max_area([1, 1]))
  print(max_area([4, 3, 2, 1, 4]))
  ```

EXPECTED OUTPUT:
  ```
  49
  1
  16
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
