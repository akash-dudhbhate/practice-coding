"""
LESSON 16 — 2D DP & Knapsack
HARD P03 — Burst Balloons
============================================

CONCEPT:
  Interval DP — the smart move is choosing the LAST balloon to
  burst, not the first. Pad nums with 1s: A = [1] + nums + [1].
  dp[i][j] = max coins bursting balloons STRICTLY between walls
  i and j. Try each k in (i, j) as the last burst:
    dp[i][j] = max(A[i]*A[k]*A[j] + dp[i][k] + dp[k][j])
  Choosing k LAST freezes its neighbors at i and j, which decouples
  the two subproblems. Fill by increasing interval length.

PROBLEM:
  Write `max_coins(nums: list[int]) -> int`. Bursting balloon i
  yields nums[i-1] * nums[i] * nums[i+1] coins (out-of-bounds
  neighbors count as 1). Return the max total. [] -> 0.

TRY THIS INPUT:
  ```python
  print(max_coins([3, 1, 5, 8]))
  print(max_coins([1, 5]))
  print(max_coins([9]))
  ```

EXPECTED OUTPUT:
  ```
  167
  10
  9
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
