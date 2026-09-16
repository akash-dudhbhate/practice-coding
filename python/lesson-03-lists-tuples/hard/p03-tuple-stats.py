"""
LESSON 03 — Lists & Tuples
HARD P03 — Tuple Stats
============================================

CONCEPT:
  Tuples are immutable lists — perfect for returning a fixed bundle of
  related values like (min, max, average). min(), max(), sum() and
  len() all work on tuples, and a tuple is "falsy" when empty.

PROBLEM:
  Write a function `tuple_stats(nums: tuple) -> tuple` that returns
  (min, max, average) where average is a float. For an empty tuple
  return (None, None, 0.0).

TRY THIS INPUT:
  ```python
  print(tuple_stats((1, 2, 3)))
  print(tuple_stats(()))
  print(tuple_stats((5,)))
  ```

EXPECTED OUTPUT:
  ```
  (1, 3, 2.0)
  (None, None, 0.0)
  (5, 5, 5.0)
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
