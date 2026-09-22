"""
LESSON 19 — FastAPI Server
MEDIUM P01 — Todo CRUD
============================================

CONCEPT:
  Full CRUD = list, create, update, delete. Separate the input model
  (TodoCreate) from the stored model (Todo with id), and use
  HTTPException for 404s.

PROBLEM:
  Create a FastAPI `app` with in-memory todos:
    - GET /todos — list all
    - POST /todos — create from {"title","done"?} → 201, assign id
    - PUT /todos/{id} — update → 404 if missing
    - DELETE /todos/{id} — delete

TRY THIS INPUT:
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  client.post("/todos", json={"title": "Buy milk"})
  print(client.get("/todos").json())
  ```

EXPECTED OUTPUT:
  ```
  [{'id': 1, 'title': 'Buy milk', 'done': False}]
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
