"""
LESSON 16 — 2D DP & Knapsack
MEDIUM P01 — 0/1 Knapsack
============================================

CONCEPT:
  THE 2D DP: dp[i][w] = max value using items 0..i-1 with capacity
  w. For each item, take-or-skip: dp[i][w] = max(dp[i-1][w],
  values[i-1] + dp[i-1][w - weights[i-1]]). Fill row by row;
  every row reads only the row above. Answer: dp[n][capacity].

PROBLEM:
  Write `knapsack(weights: list[int], values: list[int],
  capacity: int) -> int` returning the maximum total value with
  total weight <= capacity. Each item may be taken AT MOST ONCE.
  len(weights) == len(values). capacity >= 0.

TRY THIS INPUT:
  ```python
  print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))
  print(knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5))
  print(knapsack([4, 5, 6], [1, 2, 3], 3))
  ```

EXPECTED OUTPUT:
  ```
  9
  7
  0
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
