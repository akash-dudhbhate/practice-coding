"""
LESSON 06 — Stacks & Queues
MEDIUM P02 — Daily Temperatures
============================================

CONCEPT:
  Same monotonic stack as "next greater," but the answer is a DISTANCE,
  not a value — so the stack must store indices. When today's
  temperature pops a colder waiting day, the answer for that day is
  `today_index - that_day_index`.

PROBLEM:
  Write a function `daily_temperatures(temps: list[int]) -> list[int]`
  that returns a list where ans[i] is the number of days until a warmer
  temperature, or 0 if no warmer day comes.

TRY THIS INPUT:
  ```python
  print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
  print(daily_temperatures([30, 40, 50, 60]))
  print(daily_temperatures([90, 80, 70]))
  ```

EXPECTED OUTPUT:
  ```
  [1, 1, 4, 2, 1, 1, 0, 0]
  [1, 1, 1, 0]
  [0, 0, 0]
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
