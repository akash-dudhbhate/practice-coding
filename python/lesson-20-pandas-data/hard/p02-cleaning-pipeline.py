"""
LESSON 20 — Pandas & Data
HARD P02 — Data Cleaning Pipeline
============================================

CONCEPT:
  Cleaning is a fixed routine: strip whitespace on strings,
  `pd.to_numeric(..., errors="coerce")` fixes bad types,
  `drop_duplicates()`, then `fillna` the holes.

PROBLEM:
  Write a `main()` that loads a messy CSV (create messy.csv with
  spaces, "nan"/"abc" ages, empty emails, and a duplicate row if
  missing), cleans it — strip strings, numeric types, drop dups,
  fill missing values — prints before/after, and exports
  clean_data.csv.

TRY THIS INPUT:
  ```python
  main()
  ```

EXPECTED OUTPUT:
  ```
  Original:
  ...   (messy rows)
  Cleaned:
  ...   (clean rows, no NaN)
  Exported to clean_data.csv
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
