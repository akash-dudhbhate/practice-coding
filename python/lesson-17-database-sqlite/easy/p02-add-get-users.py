"""
LESSON 17 — Database with SQLite
EASY P02 — Add & Get Users
============================================

CONCEPT:
  Parameterized queries (`?` placeholders) keep data separate from
  SQL — this prevents SQL injection and handles quoting for you.

PROBLEM:
  Write `add_user(conn, name, email, age)` that INSERTs a user with
  a parameterized query, and `get_all_users(conn)` that SELECTs all
  users and returns the rows.

TRY THIS INPUT:
  ```python
  add_user(conn, "Alice", "alice@example.com", 30)
  add_user(conn, "Bob", "bob@example.com", 25)
  print(get_all_users(conn))
  ```

EXPECTED OUTPUT:
  ```
  [(1, 'Alice', 'alice@example.com', 30), (2, 'Bob', 'bob@example.com', 25)]
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
