# Lesson 18 — Flask Web Server

## What you'll learn
- Flask app setup and routing
- HTTP methods (GET, POST, PUT, DELETE)
- Request object (args, form, JSON)
- JSON responses with jsonify
- Jinja2 templates and inheritance
- Session management
- Blueprints for organization
- Error handling

## Lesson

### Basic Flask app
```python
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/api/health")
def health(): return jsonify({"status": "ok"})

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify({"created": data}), 201
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Create a Flask app with 3 routes: `/` (home), `/about`, `/contact`. Each returns a simple text response.
2. `easy/p02-solve.py` — Create a Flask API with `GET /api/greet/<name>` that returns JSON `{"message": "Hello, {name}"}`.
3. `easy/p03-solve.py` — Create a Flask route `GET /api/search` that reads a `q` query parameter and returns `{"query": q, "results": []}`.

### Medium
4. `medium/p01-solve.py` — Create a Flask REST API for a todo list: `GET /todos` (list all), `POST /todos` (create), `DELETE /todos/<id>` (delete). Store todos in a list.
5. `medium/p02-solve.py` — Create a Flask app with session-based login: `/login` (POST, sets session), `/dashboard` (requires login), `/logout` (clears session).
6. `medium/p03-solve.py` — Create a Flask app with two blueprints: `auth_bp` (login, register routes) and `api_bp` (CRUD routes). Register both with URL prefixes.

### Hard
7. `hard/p01-solve.py` — Build a complete Flask blog API: posts CRUD, comments on posts, tag filtering. Use SQLite for storage. Include error handlers for 404, 400, 500.
8. `hard/p02-solve.py` — Build a Flask app with Jinja2 templates: base template with nav, index page listing posts, post detail page, and a form to create a new post. Use template inheritance.
9. `hard/p03-solve.py` — Build a Flask API with middleware-like decorators: `@require_auth` (checks for API key header), `@rate_limit` (limits requests per IP using a dict), and `@log_request` (logs method, path, status).

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
- Test with `flask run` or `python <filename>`.
