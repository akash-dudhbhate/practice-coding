"""
LESSON 13 — Iterators & Generators
EASY P01 — count_up_to Generator
============================================

CONCEPT:
  A generator function uses `yield` instead of `return`. Each `yield`
  produces one value and pauses, so values are computed lazily — one at
  a time — instead of building a whole list in memory.

PROBLEM:
  Write a generator function `count_up_to(n)` that yields the numbers
  1, 2, 3, ... n in order. `count_up_to(0)` should yield nothing.

TRY THIS INPUT:
  ```python
  print(list(count_up_to(5)))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3, 4, 5]
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
