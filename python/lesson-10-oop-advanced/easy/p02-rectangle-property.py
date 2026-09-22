"""
LESSON 10 — OOP Advanced
EASY P02 — Rectangle with @property
============================================

CONCEPT:
  `@property` turns a method into an attribute — callers write
  `r.area` instead of `r.area()`, and the value stays computed
  on demand.

PROBLEM:
  Write a `Rectangle` class with `__init__(width, height)` and
  `area` and `perimeter` exposed as @property attributes
  (area = w*h, perimeter = 2*(w+h)).

TRY THIS INPUT:
  ```python
  r = Rectangle(4, 5)
  print(r.area)
  print(r.perimeter)
  ```

EXPECTED OUTPUT:
  ```
  20
  18
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
