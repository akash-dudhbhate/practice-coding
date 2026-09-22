"""
LESSON 17 — Database with SQLite
EASY P03 — Find User by Email
============================================

CONCEPT:
  `cursor.fetchone()` returns one row (a tuple) or None. Convert it
  to a dict so callers access fields by name, not position.

PROBLEM:
  Write `find_user_by_email(conn, email)` that returns the matching
  user as a dict {"id","name","email","age"}, or None if not found.

TRY THIS INPUT:
  ```python
  print(find_user_by_email(conn, "alice@example.com"))
  print(find_user_by_email(conn, "nobody@example.com"))
  ```

EXPECTED OUTPUT:
  ```
  {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': 30}
  None
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
