"""
LESSON 17 — Database with SQLite
MEDIUM P03 — Bulk Insert
============================================

CONCEPT:
  `executemany(sql, rows)` sends a whole batch in one call — far
  faster than looping `execute` per row.

PROBLEM:
  Write `bulk_insert(conn, users_list)` that inserts all users
  (tuples of name, email, age) with a single executemany call.
  Optionally add `individual_insert` for timing comparison.

TRY THIS INPUT:
  ```python
  users = [(f"User{i}", f"u{i}@e.com", 20 + i % 50) for i in range(100)]
  bulk_insert(conn, users)
  print(conn.execute("SELECT COUNT(*) FROM users").fetchone())
  ```

EXPECTED OUTPUT:
  ```
  (100,)
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
