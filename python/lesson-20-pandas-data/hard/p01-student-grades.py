"""
LESSON 20 — Pandas & Data
HARD P01 — Student Grades Analysis
============================================

CONCEPT:
  Column math is vectorized: `df[[...]].mean(axis=1)` averages each
  row. `nlargest`, `apply` for letter grades, and boolean .sum()
  count pass/fail.

PROBLEM:
  Write a `get_grade(avg)` function (A >=90, B >=80, C >=70,
  D >=60, else F) and a `main()` that builds 100 students with
  random scores in 3 subjects (seed 42), then computes per-student
  average + grade, class average per subject, top 5 students, and
  pass/fail counts (pass = avg >= 60). Export to
  student_results.csv.

TRY THIS INPUT:
  ```python
  print(get_grade(95), get_grade(65), get_grade(40))
  main()
  ```

EXPECTED OUTPUT:
  ```
  A D F
  Class average per subject:
  ...
  Pass: NN, Fail: NN
  Exported to student_results.csv
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
