"""
LESSON 15 — 1D Dynamic Programming
MEDIUM P01 — House Robber
============================================

CONCEPT:
  "Maximize" phrasing + a choice at each step: rob house i or skip it.
  dp[i] = max money from houses 0..i. At house i: rob it and take
  nums[i] + dp[i-2], or skip and take dp[i-1]. The take-or-skip
  recurrence is THE core 1D-DP move.

PROBLEM:
  Write `rob(nums: list[int]) -> int` returning the maximum money
  robbing houses where robbing two ADJACENT houses trips the alarm.
  nums may be empty (return 0). All values >= 0.

TRY THIS INPUT:
  ```python
  print(rob([1, 2, 3, 1]))
  print(rob([2, 7, 9, 3, 1]))
  print(rob([2, 1, 1, 2]))
  ```

EXPECTED OUTPUT:
  ```
  4
  12
  4
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
