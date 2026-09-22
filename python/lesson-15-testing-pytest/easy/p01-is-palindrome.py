"""
LESSON 15 — Testing with pytest
EASY P01 — is_palindrome with Tests
============================================

CONCEPT:
  pytest finds functions named test_* and runs each one, reporting
  failures individually. A plain `assert` is the whole assertion
  style — no unittest boilerplate.

PROBLEM:
  Write a function `is_palindrome(s)` (case-insensitive, ignoring
  spaces) AND three pytest test functions covering: a normal
  palindrome, an empty string, and a mixed-case palindrome.

TRY THIS INPUT:
  ```python
  print(is_palindrome("racecar"))
  print(is_palindrome("RaceCar"))
  ```

EXPECTED OUTPUT:
  ```
  True
  True
  ```

RUN TESTS: pytest <this file> -v
CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
