"""
LESSON 18 — Flask Server
HARD P02 — Jinja2 Templates
============================================

CONCEPT:
  Template inheritance: a base template defines blocks ({% block %})
  that child templates fill. `render_template_string` renders a
  template from a Python string (no files needed).

PROBLEM:
  Build a Flask `app` with string templates: a BASE template with
  nav + {% block content %}, an index page listing posts, a post
  detail page at /post/<id>, and /new (GET shows a form, POST
  creates a post from request.form and redirects to /).

TRY THIS INPUT:
  ```python
  client = app.test_client()
  client.post("/new", data={"title": "First", "content": "Hello"})
  print("First" in client.get("/").data.decode())
  ```

EXPECTED OUTPUT:
  ```
  True
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
