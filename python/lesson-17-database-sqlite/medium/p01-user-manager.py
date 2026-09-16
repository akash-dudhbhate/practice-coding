"""
LESSON 17 — Database with SQLite
MEDIUM P01 — UserManager Class
============================================

CONCEPT:
  Wrapping a connection in a class groups related queries behind
  clean method names — the rest of the app never writes raw SQL.

PROBLEM:
  Write a `UserManager(conn)` class that creates the users table and
  exposes: `add(name, email, age)`, `get_by_id(user_id)` (dict or
  None), `update_email(user_id, new_email)`, `delete(user_id)`, and
  `list_all()` (list of dicts). All queries parameterized.

TRY THIS INPUT:
  ```python
  mgr = UserManager(sqlite3.connect(":memory:"))
  mgr.add("Alice", "alice@example.com", 30)
  print(mgr.get_by_id(1))
  ```

EXPECTED OUTPUT:
  ```
  {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': 30}
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
