"""
LESSON 18 — Flask Server
EASY P01 — Basic Routes
============================================

CONCEPT:
  `@app.route("/path")` binds a function to a URL — whatever the
  function returns becomes the HTTP response body.

PROBLEM:
  Create a Flask `app` with three routes:
    - `/` returns "Welcome to the Home Page!"
    - `/about` returns "About Us"
    - `/contact` returns a contact string like
      "Contact: hello@example.com"

TRY THIS INPUT:
  ```python
  client = app.test_client()
  print(client.get("/").data.decode())
  ```

EXPECTED OUTPUT:
  ```
  Welcome to the Home Page!
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
