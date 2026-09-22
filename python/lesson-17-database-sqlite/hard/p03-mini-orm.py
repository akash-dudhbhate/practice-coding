"""
LESSON 17 — Database with SQLite
HARD P03 — Mini ORM
============================================

CONCEPT:
  A base `Model` class can auto-generate SQL from class metadata
  (table_name + fields). `save()` INSERTs when there's no id and
  UPDATEs when there is — that's the core of every ORM.

PROBLEM:
  Write a `Model` base class with class attrs `table_name` and
  `fields`, `__init__(**kwargs)` setting each field + `id`, a
  `set_connection(cls, conn)` classmethod, and `save()` that INSERTs
  (setting self.id from lastrowid) or UPDATEs when self.id exists.
  Demonstrate with a `User(Model)` class (users table, fields
  name/email/age).

TRY THIS INPUT:
  ```python
  conn = sqlite3.connect(":memory:")
  conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER)")
  Model.set_connection(conn)
  u = User(name="Alice", email="a@e.com", age=30)
  u.save()
  print(u.id)
  ```

EXPECTED OUTPUT:
  ```
  1
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
