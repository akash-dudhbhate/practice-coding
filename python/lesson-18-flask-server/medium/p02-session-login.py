"""
LESSON 18 — Flask Server
MEDIUM P02 — Session Login
============================================

CONCEPT:
  `session` is a signed cookie-backed dict that persists across
  requests per browser. Set `app.secret_key` so Flask can sign it.

PROBLEM:
  Create a Flask `app` (with a secret_key) and:
    - POST /login — JSON {"username","password"}; if credentials
      match a USERS dict, store session["user"] and return
      {"status": "logged in"}; else 401.
    - GET /dashboard — 401 if not logged in, else
      {"user": name, "message": "Welcome!"}.
    - GET /logout — clears the session, returns
      {"status": "logged out"}.

TRY THIS INPUT:
  ```python
  client = app.test_client()
  client.post("/login", json={"username": "admin", "password": "password123"})
  print(client.get("/dashboard").get_json())
  ```

EXPECTED OUTPUT:
  ```
  {'user': 'admin', 'message': 'Welcome!'}
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
