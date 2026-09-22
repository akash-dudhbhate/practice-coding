"""
LESSON 18 — Flask Server
HARD P03 — Decorator Middleware
============================================

CONCEPT:
  Decorators wrap a route to add cross-cutting behavior: auth checks,
  rate limiting, logging — without touching the route's own code.

PROBLEM:
  Build a Flask `app` with three decorators and a protected route:
    - `require_auth` — checks header X-API-Key == "secret123",
      else 401.
    - `rate_limit(max_requests, window)` — per-IP request cap using
      a dict; returns 429 when exceeded.
    - `log_request` — appends {"method","path","status"} to a
      `request_log` list.
    - GET /api/protected — guarded by all three, returns
      {"data": "secret"}.

TRY THIS INPUT:
  ```python
  client = app.test_client()
  print(client.get("/api/protected").status_code)
  print(client.get("/api/protected", headers={"X-API-Key": "secret123"}).get_json())
  ```

EXPECTED OUTPUT:
  ```
  401
  {'data': 'secret'}
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
