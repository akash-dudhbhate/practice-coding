"""
LESSON 11 — Modules & Packages
HARD P01 — Calculator Package
============================================

CONCEPT:
  A real package splits code into modules (e.g. `basic_ops.py`,
  `advanced_ops.py`) and uses `__init__.py` with `__all__` to expose a
  clean public API at the package level. For this exercise, simulate
  the whole package in ONE file.

PROBLEM:
  Define these functions in this file:
    - Basic: `add(a, b)`, `sub(a, b)`, `mul(a, b)`, `div(a, b)`
      (`div` raises ZeroDivisionError when b == 0)
    - Advanced: `power(a, b)`, `sqrt(a)`, `factorial(n)`
  Set `__all__` to the list of all 7 names, and add a `__main__` block
  that asserts each one works.

TRY THIS INPUT:
  ```python
  print(add(2, 3), sub(5, 2), mul(3, 4), div(10, 2))
  print(power(2, 3), sqrt(16), factorial(5))
  ```

EXPECTED OUTPUT:
  ```
  5 3 12 5.0
  8 4.0 120
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
