"""
LESSON 17 — Database with SQLite
EASY P01 — Create DB
============================================

CONCEPT:
  `sqlite3.connect(path)` opens (creating if needed) a database.
  `conn.execute(sql)` runs SQL; `conn.commit()` saves changes.
  Use ":memory:" for a throwaway in-RAM database.

PROBLEM:
  Write a function `create_db(db_path)` that creates a SQLite
  database containing a `users` table with columns
  id (INTEGER PRIMARY KEY), name (TEXT), email (TEXT UNIQUE),
  age (INTEGER). Return the connection.

TRY THIS INPUT:
  ```python
  conn = create_db(":memory:")
  print(conn.execute("SELECT name FROM sqlite_master").fetchall())
  ```

EXPECTED OUTPUT:
  ```
  [('users',)]
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
