"""
LESSON 06 — Functions Deep Dive
HARD P01 — Make Counter Closure
============================================

CONCEPT:
  A closure is an inner function that remembers variables from the
  enclosing function. `nonlocal` lets the inner function update them.

PROBLEM:
  Write a function `make_counter(start=0)` that returns a function.
  Each call to the returned function increments the count by 1 and
  returns the new value, starting from `start`.

TRY THIS INPUT:
  ```python
  c = make_counter()
  print(c())
  print(c())
  c2 = make_counter(10)
  print(c2())
  ```

EXPECTED OUTPUT:
  ```
  1
  2
  11
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
