"""
LESSON 11 — Modules & Packages
MEDIUM P01 — Building a Package
============================================

CONCEPT:
  A package is a folder of modules with an `__init__.py` file. It lets
  you organize code into a hierarchy: `myapp/utils.py`,
  `myapp/models/user.py`, imported as `from myapp.models.user import User`.
  For this exercise, simulate the package in ONE file (like the solution).

PROBLEM:
  Define in this file:
    - `format_date(dt=None, fmt="%Y-%m-%d")` — formats a datetime
      (defaults to now) using `dt.strftime(fmt)`
    - a `User` class whose `__init__(self, name, email)` stores both
      attributes, and `__str__` returns f"User({name}, {email})"
  Add an `if __name__ == "__main__":` block that tests both.

TRY THIS INPUT:
  ```python
  from datetime import datetime
  print(format_date(datetime(2024, 1, 15)))
  print(User("Akash", "akash@test.com"))
  ```

EXPECTED OUTPUT:
  ```
  2024-01-15
  User(Akash, akash@test.com)
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
