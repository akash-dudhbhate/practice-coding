"""
LESSON 19 — FastAPI Server
EASY P01 — Basic Routes
============================================

CONCEPT:
  FastAPI routes use typed decorators: `@app.get("/path")`. Type
  hints on parameters (`item_id: int`) give you parsing and
  validation for free.

PROBLEM:
  Create a FastAPI `app` with:
    - GET / returning {"status": "ok"}
    - GET /items/{item_id} returning {"item_id": item_id}
      (item_id typed as int)

TRY THIS INPUT:
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  print(client.get("/").json())
  print(client.get("/items/42").json())
  ```

EXPECTED OUTPUT:
  ```
  {'status': 'ok'}
  {'item_id': 42}
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
