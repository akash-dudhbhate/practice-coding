"""
LESSON 16 — 2D DP & Knapsack
EASY P01 — Unique Paths
============================================

CONCEPT:
  Grid DP: dp[r][c] = number of ways to reach cell (r, c). You can
  only arrive from the top or the left, so dp[r][c] = dp[r-1][c] +
  dp[r][c-1]. First row and first column are all 1s — only one way
  to reach any cell on an edge.

PROBLEM:
  Write `unique_paths(m: int, n: int) -> int` returning the number
  of distinct paths from the top-left to bottom-right corner of an
  m x n grid, moving only RIGHT or DOWN. m, n >= 1.

TRY THIS INPUT:
  ```python
  print(unique_paths(3, 2))
  print(unique_paths(3, 7))
  print(unique_paths(1, 1))
  ```

EXPECTED OUTPUT:
  ```
  3
  28
  1
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
