"""
LESSON 20 — Pandas & Data
MEDIUM P02 — Merge & Top Users
============================================

CONCEPT:
  `df1.merge(df2, left_on=..., right_on=...)` joins two DataFrames
  like a SQL JOIN — then groupby + sort_values finds the leaders.

PROBLEM:
  Write a `main()` that creates a users DataFrame (id, name, city)
  and an orders DataFrame (id, user_id, amount, date), merges them
  on user_id, and prints the top 3 users by total order amount.

TRY THIS INPUT:
  ```python
  main()
  ```

EXPECTED OUTPUT:
  ```
  Top 3 users by total amount:
  name
  Alice      1200
  Bob         900
  Charlie     200
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
