"""
LESSON 17 — Database with SQLite
MEDIUM P02 — Posts with Foreign Key + JOIN
============================================

CONCEPT:
  A FOREIGN KEY links tables (posts.user_id -> users.id). JOIN
  combines rows from both so you can show "who wrote what" in one
  query; GROUP BY + COUNT aggregates per user.

PROBLEM:
  Write four functions:
    - `setup_db(conn)` — create `users` (id, name, email) and
      `posts` (id, user_id FK, title) tables.
    - `create_post(conn, user_id, title)` — insert a post.
    - `get_posts_by_user(conn, user_id)` — JOIN query returning
      (name, title) rows for that user.
    - `count_posts_per_user(conn)` — (name, count) rows for every
      user (LEFT JOIN so zero-post users appear).

TRY THIS INPUT:
  ```python
  create_post(conn, 1, "Hello World")
  print(get_posts_by_user(conn, 1))
  print(count_posts_per_user(conn))
  ```

EXPECTED OUTPUT:
  ```
  [('Alice', 'Hello World')]
  [('Alice', 1), ('Bob', 0)]
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
