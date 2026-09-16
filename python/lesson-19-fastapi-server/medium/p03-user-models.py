"""
LESSON 19 — FastAPI Server
MEDIUM P03 — Separate Input/Output Models
============================================

CONCEPT:
  Never echo secrets back. `response_model=UserResponse` filters the
  output — password goes in but never comes out.

PROBLEM:
  Create `UserCreate` (name, email, password) and `UserResponse`
  (id, name, email — NO password). `POST /users` accepts UserCreate,
  stores the user, and returns UserResponse via response_model.

TRY THIS INPUT:
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  r = client.post("/users", json={"name": "Akash", "email": "a@e.com", "password": "pw"})
  print(r.json())
  ```

EXPECTED OUTPUT:
  ```
  {'id': 1, 'name': 'Akash', 'email': 'a@e.com'}
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
