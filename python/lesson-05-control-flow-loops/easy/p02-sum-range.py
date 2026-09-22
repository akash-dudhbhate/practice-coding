"""
LESSON 05 — Control Flow & Loops
EASY P02 — Sum Range
============================================

CONCEPT:
  range(start, stop) generates integers but EXCLUDES the stop value —
  so range(start, stop + 1) is the trick for an inclusive range.
  Adding each value to a running total is the accumulator pattern.

PROBLEM:
  Write a function `sum_range(start: int, stop: int) -> int` that
  returns the sum of all integers from `start` to `stop` INCLUSIVE,
  using a for loop with range.

TRY THIS INPUT:
  ```python
  print(sum_range(1, 5))
  print(sum_range(0, 0))
  print(sum_range(-2, 2))
  ```

EXPECTED OUTPUT:
  ```
  15
  0
  0
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
