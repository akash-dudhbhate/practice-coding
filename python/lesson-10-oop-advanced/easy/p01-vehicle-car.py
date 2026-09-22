"""
LESSON 10 — OOP Advanced
EASY P01 — Vehicle and Car Inheritance
============================================

CONCEPT:
  A subclass inherits everything from its parent and can extend it.
  `super().__init__(...)` reuses the parent's setup; overriding a
  method replaces the parent's version.

PROBLEM:
  Write a `Vehicle` class with `__init__(make, model, year)` and a
  `display()` method returning "year make model". Then a `Car`
  subclass that adds `num_doors` and overrides `display()` to append
  " (N doors)".

TRY THIS INPUT:
  ```python
  c = Car("Toyota", "Camry", 2020, 4)
  print(c.display())
  ```

EXPECTED OUTPUT:
  ```
  2020 Toyota Camry (4 doors)
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
