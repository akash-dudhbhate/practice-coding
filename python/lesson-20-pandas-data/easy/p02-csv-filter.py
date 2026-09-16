"""
LESSON 20 — Pandas & Data
EASY P02 — Load CSV and Filter
============================================

CONCEPT:
  `pd.read_csv(path)` loads a file into a DataFrame. Boolean masks
  like `df[(df.age > 25) & (df.city == "Mumbai")]` select matching
  rows (use & not `and`).

PROBLEM:
  Write a `main()` that loads a CSV of people (create sample.csv if
  missing), filters to rows where age > 25 AND city == "Mumbai",
  and prints the result.

TRY THIS INPUT:
  ```python
  main()
  ```

EXPECTED OUTPUT:
  ```
     name  age    city
  3  Diana   28  Mumbai
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
