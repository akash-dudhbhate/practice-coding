"""
LESSON 09 — OOP Basics
HARD P02 — Student with Class Counter
============================================

CONCEPT:
  A class attribute is shared by all instances — good for counting
  how many objects exist. Remember the mutable-default trap: use
  `grades=None`, never `grades=[]`.

PROBLEM:
  Write a class `Student` with a class attribute `count` tracking
  total students created, `__init__(self, name, grades=None)`,
  `add_grade(g)`, `average()` (0 when no grades), and a classmethod
  `get_count()`.

TRY THIS INPUT:
  ```python
  s1 = Student("Akash", [90, 80])
  s2 = Student("Dev")
  s2.add_grade(70)
  print(Student.get_count())
  print(s1.average(), s2.average())
  ```

EXPECTED OUTPUT:
  ```
  2
  85.0 70.0
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
