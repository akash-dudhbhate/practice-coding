"""
LESSON 07 — File I/O & Error Handling
EASY P03 — Safe Int
============================================

CONCEPT:
  `try / except` lets you catch an error instead of crashing.
  `int("abc")` raises ValueError — catch it and return a fallback.

PROBLEM:
  Write a function `safe_int(s)` that converts `s` to an int and
  returns it. If conversion fails, return None.

TRY THIS INPUT:
  ```python
  print(safe_int("42"))
  print(safe_int("abc"))
  print(safe_int(""))
  ```

EXPECTED OUTPUT:
  ```
  42
  None
  None
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
