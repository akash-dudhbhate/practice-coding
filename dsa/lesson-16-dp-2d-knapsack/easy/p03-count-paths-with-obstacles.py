"""
LESSON 16 — 2D DP & Knapsack
EASY P03 — Unique Paths with Obstacles
============================================

CONCEPT:
  Unique paths + walls. dp[r][c] = 0 when grid[r][c] is a wall (1).
  The subtle part is the BORDERS: a wall in the first row or column
  zeroes out everything after it in that border — you can't walk
  through a wall to reach the cells beyond it.

PROBLEM:
  Write `unique_paths_with_obstacles(grid: list[list[int]]) -> int`
  where 0 = open, 1 = wall. Count right/down paths from [0][0] to
  [m-1][n-1]. If either endpoint is a wall, the answer is 0.

TRY THIS INPUT:
  ```python
  print(unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
  print(unique_paths_with_obstacles([[0, 1], [0, 0]]))
  print(unique_paths_with_obstacles([[1]]))
  ```

EXPECTED OUTPUT:
  ```
  2
  1
  0
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
