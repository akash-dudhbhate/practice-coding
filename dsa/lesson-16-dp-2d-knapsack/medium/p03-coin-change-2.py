"""
LESSON 16 — 2D DP & Knapsack
MEDIUM P03 — Coin Change 2 (Count Combinations)
============================================

CONCEPT:
  Count the WAYS, but combinations not permutations: {1,2,2} is the
  same combination as {2,1,2}. The loop order is the whole trick:
  COINS outer, AMOUNT inner — each coin is fully processed before
  the next, so orderings can't multiply. (Amount-outer counts
  permutations and overcounts.)

PROBLEM:
  Write `coin_change_count(amount: int, coins: list[int]) -> int`
  returning the number of combinations of coins summing to
  `amount` (unlimited supply of each). coin_change_count(0, ...)
  == 1 — there is one way to make nothing.

TRY THIS INPUT:
  ```python
  print(coin_change_count(5, [1, 2, 5]))
  print(coin_change_count(3, [2]))
  print(coin_change_count(10, [10]))
  ```

EXPECTED OUTPUT:
  ```
  4
  0
  1
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
