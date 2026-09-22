"""
LESSON 19 — FastAPI Server
MEDIUM P02 — Pagination Dependency
============================================

CONCEPT:
  `Depends(func)` runs shared logic before the route and injects the
  result — perfect for common params like pagination.

PROBLEM:
  Write a dependency `get_pagination(page: int = 1, size: int = 10)`
  returning {"skip": (page-1)*size, "limit": size}, and use it via
  Depends in `GET /items` which returns
  {"pagination": pagination, "items": []}.

TRY THIS INPUT:
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  print(client.get("/items?page=3&size=5").json())
  ```

EXPECTED OUTPUT:
  ```
  {'pagination': {'skip': 10, 'limit': 5}, 'items': []}
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
