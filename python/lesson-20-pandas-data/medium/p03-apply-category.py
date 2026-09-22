"""
LESSON 20 — Pandas & Data
MEDIUM P03 — Apply + Export
============================================

CONCEPT:
  `df["col"].apply(func)` transforms every value with your own
  function. `to_csv(path, index=False)` writes the result out.

PROBLEM:
  Write a `categorize(age)` function (<20 "teen", 20-60 "adult",
  >60 "senior") and a `main()` that loads a people CSV (create
  people.csv if missing), adds a "category" column via apply(),
  prints the DataFrame, and exports to people_categorized.csv.

TRY THIS INPUT:
  ```python
  print(categorize(18), categorize(35), categorize(70))
  main()
  ```

EXPECTED OUTPUT:
  ```
  teen adult senior
       name  age category
  0   Alice   18     teen
  ...
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
