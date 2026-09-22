"""
LESSON 10 — OOP Advanced
HARD P01 — Employee Hierarchy
============================================

CONCEPT:
  Inheritance shines when siblings share a base but specialize
  behavior. Each subclass calls super().__init__ then adds its own
  fields and overrides salary calculation.

PROBLEM:
  Write `Employee(name, salary)` with `calculate_salary()` returning
  the base salary. Then:
    - `Manager(name, salary, team=None)` — salary + 100 per team
      member.
    - `Developer(name, salary, languages=None)` — salary + 50 per
      programming language.

TRY THIS INPUT:
  ```python
  m = Manager("Alice", 80000, ["Bob", "Carol"])
  print(m.calculate_salary())
  d = Developer("Dave", 70000, ["Python", "JS"])
  print(d.calculate_salary())
  ```

EXPECTED OUTPUT:
  ```
  80200
  70100
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
