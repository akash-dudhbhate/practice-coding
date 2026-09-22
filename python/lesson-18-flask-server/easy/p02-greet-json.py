"""
LESSON 18 — Flask Server
EASY P02 — JSON Greet API
============================================

CONCEPT:
  `<name>` in a route captures a URL segment as a function argument.
  `jsonify({...})` returns a JSON response with the right headers.

PROBLEM:
  Create a Flask `app` with `GET /api/greet/<name>` returning JSON
  {"message": "Hello, {name}"}.

TRY THIS INPUT:
  ```python
  client = app.test_client()
  print(client.get("/api/greet/Akash").get_json())
  ```

EXPECTED OUTPUT:
  ```
  {'message': 'Hello, Akash'}
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
