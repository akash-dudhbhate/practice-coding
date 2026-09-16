"""
LESSON 12 — Decorators
EASY P01 — @shout Decorator
============================================

CONCEPT:
  A decorator is a function that takes a function and returns a new
  function that wraps it — adding behavior before/after the call without
  changing the original code. `@shout` is shorthand for
  `greet = shout(greet)`.

PROBLEM:
  Write a decorator `shout(func)` whose wrapper calls the function and
  returns its result in UPPERCASE (only if the result is a string).
  Apply it to `greet(name)` returning f"hello {name}".

TRY THIS INPUT:
  ```python
  print(greet("world"))
  ```

EXPECTED OUTPUT:
  ```
  HELLO WORLD
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
