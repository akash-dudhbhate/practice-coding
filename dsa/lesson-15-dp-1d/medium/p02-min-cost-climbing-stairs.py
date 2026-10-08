"""
LESSON 15 — 1D Dynamic Programming
MEDIUM P02 — Min Cost Climbing Stairs
============================================

CONCEPT:
  "Minimize" phrasing + the answer-location trap: the TOP of the
  stairs is one step past the last element, so the answer is
  min(dp[n-1], dp[n-2]), NOT dp[n-1]. Base cases are also special:
  starting at stair 0 or 1 is free — you only pay cost[i] for
  stepping ON stair i.

PROBLEM:
  Write `min_cost(cost: list[int]) -> int` returning the minimum
  toll to reach the top of the stairs. You may start at index 0 or
  index 1; from any stair you may climb 1 or 2. len(cost) >= 2.

TRY THIS INPUT:
  ```python
  print(min_cost([10, 15, 20]))
  print(min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
  print(min_cost([0, 0, 1]))
  ```

EXPECTED OUTPUT:
  ```
  15
  6
  0
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
