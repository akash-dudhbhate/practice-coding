"""
LESSON 18 — Flask Server
MEDIUM P03 — Blueprints
============================================

CONCEPT:
  A Blueprint bundles routes that you attach to the app with a URL
  prefix — keeps a big app organized into feature modules.

PROBLEM:
  Create two blueprints and register them on a Flask `app`:
    - `auth_bp` with url_prefix="/auth": POST /login and
      POST /register (each returns a small JSON status).
    - `api_bp` with url_prefix="/api": GET /items (list) and
      POST /items (create, 201).

TRY THIS INPUT:
  ```python
  client = app.test_client()
  print(client.get("/api/items").get_json())
  print(client.post("/auth/login").status_code)
  ```

EXPECTED OUTPUT:
  ```
  {'items': []}
  200
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
