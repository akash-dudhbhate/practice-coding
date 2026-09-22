"""
LESSON 18 — Flask Server
EASY P03 — Search with Query Param
============================================

CONCEPT:
  Query strings (`?q=test`) live in `request.args` — a dict-like
  object where `.get("q", default)` reads them safely.

PROBLEM:
  Create a Flask `app` with `GET /api/search` that reads the `q`
  query parameter and returns JSON {"query": q, "results": []}.

TRY THIS INPUT:
  ```python
  client = app.test_client()
  print(client.get("/api/search?q=python").get_json())
  ```

EXPECTED OUTPUT:
  ```
  {'query': 'python', 'results': []}
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
