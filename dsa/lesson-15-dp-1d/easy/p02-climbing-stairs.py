"""
LESSON 15 — 1D Dynamic Programming
EASY P02 — Climbing Stairs
============================================

CONCEPT:
  "Count the number of ways" — the count-ways phrasing. To arrive at
  step i, your last move was a 1-step (from i-1) or a 2-step (from
  i-2), so ways(i) = ways(i-1) + ways(i-2). It's Fibonacci shifted
  by one — recognizing shared recurrences is the DP skill.

PROBLEM:
  Write `climb_stairs(n: int) -> int` returning the number of
  distinct ways to climb n stairs when each move climbs 1 or 2.
  n >= 1. climb_stairs(1) = 1, climb_stairs(2) = 2.

TRY THIS INPUT:
  ```python
  print(climb_stairs(2))
  print(climb_stairs(5))
  print(climb_stairs(45))
  ```

EXPECTED OUTPUT:
  ```
  2
  8
  1836311903
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
