"""
LESSON 18 — Flask Server
MEDIUM P01 — Todo REST API
============================================

CONCEPT:
  One URL can serve several HTTP methods: `methods=["GET"]` lists,
  `methods=["POST"]` creates. `request.get_json()` reads the JSON
  body of a POST.

PROBLEM:
  Create a Flask `app` with a todo API backed by a list:
    - GET /todos — returns JSON list of todos
    - POST /todos — reads {"title": ...} JSON, creates
      {"id": n, "title": ..., "done": False}, returns it with 201
    - DELETE /todos/<id> — removes the todo, returns 204

TRY THIS INPUT:
  ```python
  client = app.test_client()
  client.post("/todos", json={"title": "Buy milk"})
  print(client.get("/todos").get_json())
  ```

EXPECTED OUTPUT:
  ```
  [{'id': 1, 'title': 'Buy milk', 'done': False}]
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
