"""
LESSON 20 — Pandas & Data
HARD P03 — Time-Series Pivot
============================================

CONCEPT:
  `pivot_table` reshapes long data into a matrix; `pct_change`
  across columns gives month-over-month growth per product.

PROBLEM:
  Write a `main()` that builds a time-series DataFrame (date monthly
  over 12 months, product A/B/C, sales — seed 42), creates a
  product x month pivot_table of sales, computes month-over-month
  growth with pct_change(axis=1), and prints which products are
  trending (3+ consecutive months of positive growth).

TRY THIS INPUT:
  ```python
  main()
  ```

EXPECTED OUTPUT:
  ```
  Pivot table:
  product   January  February  ...
  ...
  Trending products (3+ consecutive positive growth): [...]
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
