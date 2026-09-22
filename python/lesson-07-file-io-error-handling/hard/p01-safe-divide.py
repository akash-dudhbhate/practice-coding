"""
LESSON 07 — File I/O & Error Handling
HARD P01 — Safe Divide with Custom Error
============================================

CONCEPT:
  You can define your own exception with `class MyError(Exception)`.
  Raising specific errors makes bugs easier to diagnose than
  returning magic values like -1.

PROBLEM:
  Define `class DivideByZeroError(Exception)` and a function
  `safe_divide(a, b)` that:
    - returns a / b for numeric inputs,
    - raises DivideByZeroError if b == 0,
    - raises TypeError if a or b is not an int/float.

TRY THIS INPUT:
  ```python
  print(safe_divide(10, 2))
  try:
      safe_divide(1, 0)
  except DivideByZeroError as e:
      print("caught:", e)
  ```

EXPECTED OUTPUT:
  ```
  5.0
  caught: Cannot divide by zero
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
