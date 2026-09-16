"""
LESSON 12 — Decorators
MEDIUM P01 — @repeat(n) Decorator with Arguments
============================================

CONCEPT:
  A decorator that takes arguments needs THREE nested levels:
  `repeat(n)` returns `decorator`, which takes the function and returns
  `wrapper`. The outer call configures the decoration; the inner two do
  the actual wrapping.

PROBLEM:
  Write `repeat(n)` — a decorator factory — so `@repeat(3)` calls the
  decorated function 3 times and returns the LAST result. Apply it to a
  `greet()` that prints "hi" and returns "done".

TRY THIS INPUT:
  ```python
  @repeat(3)
  def greet():
      print("hi")
      return "done"

  print(greet())
  ```

EXPECTED OUTPUT:
  ```
  hi
  hi
  hi
  done
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
