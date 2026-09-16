"""
LESSON 18 — Flask Server
HARD P01 — Blog API with SQLite
============================================

CONCEPT:
  Combine Flask + SQLite: open one connection per request (flask.g),
  create tables in an init function, and map errors to JSON with
  @app.errorhandler.

PROBLEM:
  Build a Flask `app` blog API backed by SQLite (module-level
  DB_PATH, an `init_db()` function):
    - GET /posts — list all posts; optional ?tag= filter
    - POST /posts — create {"title","content","tag"} → 201
    - DELETE /posts/<id> — delete → 204
    - POST /posts/<id>/comments — add {"text"} comment → 201
    - JSON error handlers for 404, 400, 500.

TRY THIS INPUT:
  ```python
  client = app.test_client()
  client.post("/posts", json={"title": "Hi", "content": "Body", "tag": "py"})
  print(client.get("/posts?tag=py").get_json())
  ```

EXPECTED OUTPUT:
  ```
  [{'id': 1, 'title': 'Hi', 'content': 'Body', 'tag': 'py'}]
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
