"""
LESSON 17 — Database with SQLite
HARD P02 — Generate Report
============================================

CONCEPT:
  Aggregate SQL (COUNT, AVG, CASE WHEN inside SUM) computes
  summaries in the database instead of pulling all rows into Python.

PROBLEM:
  Write `generate_report(conn)` that returns a dict with:
    - "total_users": COUNT(*)
    - "average_age": AVG(age) rounded to 1 decimal
    - "age_groups": {"under_20": n, "20_to_30": n, "30_plus": n}
    - "most_common_domain": most frequent email domain

TRY THIS INPUT:
  ```python
  # users: Alice 18 gmail, Bob 25 yahoo, Charlie 35 gmail, Diana 28 gmail
  print(generate_report(conn))
  ```

EXPECTED OUTPUT:
  ```
  {'total_users': 4, 'average_age': 26.5, 'age_groups': {'under_20': 1, '20_to_30': 2, '30_plus': 1}, 'most_common_domain': ('gmail.com', 3)}
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
