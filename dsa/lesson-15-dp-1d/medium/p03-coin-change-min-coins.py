"""
LESSON 15 — 1D Dynamic Programming
MEDIUM P03 — Coin Change (Fewest Coins)
============================================

CONCEPT:
  "Minimize" over a set of choices: dp[a] = fewest coins making
  amount a, and dp[a] = 1 + min(dp[a - c]) over coins c <= a.
  The critical detail: unreachable amounts must stay at INF,
  never 0 — otherwise min() treats impossible as free and every
  answer collapses to 0.

PROBLEM:
  Write `coin_change(coins: list[int], amount: int) -> int`
  returning the FEWEST coins needed to sum to `amount` (unlimited
  coins of each denomination). Return -1 if impossible.
  coin_change(coins, 0) == 0.

TRY THIS INPUT:
  ```python
  print(coin_change([1, 2, 5], 11))
  print(coin_change([2], 3))
  print(coin_change([1], 0))
  ```

EXPECTED OUTPUT:
  ```
  3
  -1
  0
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
