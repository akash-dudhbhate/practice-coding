"""
LESSON 12 — Decorators
HARD P01 — @CountCalls Class Decorator
============================================

CONCEPT:
  A class can be a decorator too: `__init__` receives the function and
  `__call__` makes instances callable, so the decorated "function" is
  actually an object — which means it can carry state like a counter.

PROBLEM:
  Write a class `CountCalls` usable as `@CountCalls`. It stores the
  function in `__init__`, and each call through `__call__` increments
  `self.count` then returns the function's result. After decorating
  `say_hi()`, the call count must be reachable as `say_hi.count`.

TRY THIS INPUT:
  ```python
  @CountCalls
  def say_hi():
      return "hi"

  say_hi(); say_hi(); say_hi()
  print(say_hi.count)
  ```

EXPECTED OUTPUT:
  ```
  3
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
