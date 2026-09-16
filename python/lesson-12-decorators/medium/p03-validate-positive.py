"""
LESSON 12 — Decorators
MEDIUM P03 — @validate_positive Decorator
============================================

CONCEPT:
  Decorators can enforce preconditions — checking arguments before the
  real function ever runs. Raising inside the wrapper stops the call,
  which is how input validation stays out of business logic.

PROBLEM:
  Write a decorator `validate_positive(func)` that raises ValueError if
  ANY positional argument that is an int/float is <= 0; otherwise it
  calls the function normally. Apply it to `calculate_area(width, height)`
  returning width * height.

TRY THIS INPUT:
  ```python
  print(calculate_area(4, 5))
  try:
      calculate_area(-1, 5)
  except ValueError as e:
      print("ValueError:", e)
  ```

EXPECTED OUTPUT:
  ```
  20
  ValueError: Argument must be positive, got -1
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
