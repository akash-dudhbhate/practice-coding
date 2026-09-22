"""
LESSON 13 — Iterators & Generators
HARD P02 — chunked Generator
============================================

CONCEPT:
  Batching is a common generator job: accumulate items into a small
  list, `yield` it when it reaches `size`, and remember to yield the
  leftover partial chunk after the loop ends.

PROBLEM:
  Write a generator `chunked(iterable, size)` that yields lists of up to
  `size` items each, in order. The final chunk may be smaller. Works on
  ANY iterable (lists, generators, ...). Empty input yields nothing.

TRY THIS INPUT:
  ```python
  print(list(chunked([1, 2, 3, 4, 5], 2)))
  print(list(chunked([1, 2, 3], 5)))
  ```

EXPECTED OUTPUT:
  ```
  [[1, 2], [3, 4], [5]]
  [[1, 2, 3]]
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
