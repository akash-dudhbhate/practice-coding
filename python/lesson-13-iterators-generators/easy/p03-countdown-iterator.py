"""
LESSON 13 — Iterators & Generators
EASY P03 — CountDown Iterator Class
============================================

CONCEPT:
  The iterator protocol needs two methods: `__iter__` returns the
  iterator object (usually `self`), and `__next__` returns the next
  value or raises `StopIteration` when done. Any class implementing
  both works in a `for` loop and with `list()`.

PROBLEM:
  Write a class `CountDown` whose `__init__(self, n)` stores n.
  Iterating it should yield n, n-1, ... down to 1, then stop.
  `list(CountDown(0))` should be empty.

TRY THIS INPUT:
  ```python
  print(list(CountDown(3)))
  for x in CountDown(5):
      print(x, end=" ")
  ```

EXPECTED OUTPUT:
  ```
  [3, 2, 1]
  5 4 3 2 1
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
