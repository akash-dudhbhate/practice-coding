"""
LESSON 11 — Modules & Packages
EASY P01 — Module with __main__ Guard
============================================

CONCEPT:
  Any .py file is a "module" — you can import it into other files.
  The `if __name__ == "__main__":` guard lets a file act BOTH as an
  importable module AND as a runnable script: code inside the guard
  only runs when you execute the file directly, not when it is imported.

PROBLEM:
  Create a module with a function `greet(name)` that returns
  f"Hello, {name}!" and a constant `PI = 3.14159`. Add an
  `if __name__ == "__main__":` block that prints a greeting and PI.

TRY THIS INPUT:
  ```python
  print(greet("World"))
  print(f"PI = {PI}")
  ```

EXPECTED OUTPUT:
  ```
  Hello, World!
  PI = 3.14159
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
