"""
LESSON 19 — FastAPI Server
HARD P02 — JWT Auth
============================================

CONCEPT:
  JWT = signed token the client sends back on later requests. A
  dependency (e.g. HTTPBearer + decode) protects routes without
  repeating auth code.

PROBLEM:
  Build a FastAPI `app` with:
    - POST /register — {"username","password"} stores a user
      (400 if it exists)
    - POST /login — verifies credentials and returns
      {"access_token": <jwt>} (401 on bad creds)
    - GET /me — requires the bearer token via a dependency,
      returns {"username": ...}; 401 without/invalid token.
  Use python-jose (from jose import jwt) for tokens.

TRY THIS INPUT:
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  client.post("/register", json={"username": "u1", "password": "pw"})
  tok = client.post("/login", json={"username": "u1", "password": "pw"}).json()["access_token"]
  print(client.get("/me", headers={"Authorization": f"Bearer {tok}"}).json())
  ```

EXPECTED OUTPUT:
  ```
  {'username': 'u1'}
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
