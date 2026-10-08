"""
LESSON 16 — 2D DP & Knapsack
EASY P02 — Min Path Sum
============================================

CONCEPT:
  Same grid shape, MIN phrasing: dp[r][c] = grid[r][c] +
  min(dp[r-1][c], dp[r][c-1]) — add this cell's cost to the cheaper
  of the two ways in. Borders are forced: first row accumulates
  from the left, first column from above. No choice on edges.

PROBLEM:
  Write `min_path_sum(grid: list[list[int]]) -> int` returning the
  minimum sum along any top-left → bottom-right path moving only
  RIGHT or DOWN. Grid is non-empty, values >= 0.

TRY THIS INPUT:
  ```python
  print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
  print(min_path_sum([[1, 2, 3], [4, 5, 6]]))
  print(min_path_sum([[7]]))
  ```

EXPECTED OUTPUT:
  ```
  7
  12
  7
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
