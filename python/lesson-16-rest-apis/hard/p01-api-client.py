"""
LESSON 16 — REST APIs
HARD P01 — APIClient Class
============================================

CONCEPT:
  A `requests.Session()` reuses connections and carries default
  headers (auth!) across every request — wrap it in a small client
  class with get/post/put/delete methods.

PROBLEM:
  Write an `APIClient(base_url, token=None, timeout=30)` class that
  holds a Session, sets an Authorization Bearer header when a token
  is given, applies a default timeout, calls raise_for_status() on
  every response, and exposes `get(path)`, `post(path, data)`,
  `put(path, data)`, `delete(path)` returning parsed JSON.

TRY THIS INPUT:
  ```python
  client = APIClient("https://api.github.com")
  print(client.get("/users/torvalds")["name"])
  ```

EXPECTED OUTPUT:
  ```
  Linus Torvalds
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
