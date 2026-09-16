"""
LESSON 19 — FastAPI Server
HARD P01 — Books CRUD with SQLite
============================================

CONCEPT:
  Everything together: Pydantic in/out models, a `get_db` dependency
  yielding a SQLite connection, query-param filtering and
  pagination, and HTTPException for 404s.

PROBLEM:
  Build a FastAPI `app` for books backed by SQLite (module-level
  DB_PATH + `init_db()`):
    - GET /books — list with skip/limit pagination and optional
      ?author= filter (LIKE match)
    - POST /books — create from {title, author, year} → 201
    - GET /books/{id} — one book, 404 if missing
    - DELETE /books/{id} — delete, 404 if missing

TRY THIS INPUT:
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  client.post("/books", json={"title": "Dune", "author": "Herbert", "year": 1965})
  print(client.get("/books?author=Herbert").json())
  ```

EXPECTED OUTPUT:
  ```
  [{'id': 1, 'title': 'Dune', 'author': 'Herbert', 'year': 1965}]
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
