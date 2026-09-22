"""
LESSON 19 — FastAPI Server
EASY P03 — Query Params
============================================

CONCEPT:
  Function parameters that aren't in the path become query params.
  Defaults make them optional; types coerce strings to int/bool.

PROBLEM:
  Create `GET /users` on a FastAPI `app` with query params
  `skip: int = 0`, `limit: int = 10`, `active: bool = True` that
  returns them as JSON.

TRY THIS INPUT:
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  print(client.get("/users").json())
  print(client.get("/users?skip=5&limit=3&active=false").json())
  ```

EXPECTED OUTPUT:
  ```
  {'skip': 0, 'limit': 10, 'active': True}
  {'skip': 5, 'limit': 3, 'active': False}
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
