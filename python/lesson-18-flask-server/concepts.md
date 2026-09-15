# Lesson 18 — Concepts Explained (Flask Web Server)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Flask Framework

**What:** Flask is a lightweight Python web framework. It maps URLs to Python functions.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)    # starts server at http://localhost:5000
```

**Why it exists:** Without a web framework, you'd handle HTTP parsing, routing, responses manually — hundreds of lines for "Hello World". Flask does all the HTTP plumbing so you focus on your app logic.

**Where it's used:** Web APIs, small web apps, prototypes, internal tools, microservices. Companies like Pinterest and LinkedIn started with Flask.

**What goes wrong without it:**
- Raw HTTP handling → you parse headers, bodies, cookies manually → error-prone, slow development.
- `debug=True` in production → code errors show stack traces to users → security risk.
- Forgetting `app.run()` → nothing happens when you run the file.

---

## Routing (@app.route)

**What:** Routing maps a URL pattern to a Python function. When a browser requests that URL, Flask calls the function.

```python
@app.route("/")
def index(): return "Home page"

@app.route("/about")
def about(): return "About page"

@app.route("/user/<username>")      # dynamic URL
def profile(username): return f"User: {username}"

@app.route("/post/<int:post_id>")   # typed parameter
def post(post_id): return f"Post #{post_id}"
```

**Why it exists:** Without routing, you'd parse URLs manually with if/else: `if path == "/about": ...`. Routing handles this declaratively — one decorator per URL.

**Where it's used:** Every web framework — Flask, Django, FastAPI, Express (JS). Routing is the core of web development.

**What goes wrong without it:**
- Two routes with the same URL → the second overwrites the first → only one works.
- Forgetting the leading `/` → `@app.route("about")` → Flask adds it but it's bad practice.
- `int:` converter: `@app.route("/post/<post_id>")` → `post_id` is a string. `@app.route("/post/<int:post_id>")` → `post_id` is an int. Wrong type → 404 for non-numeric URLs.

---

## HTTP Methods

**What:** Restrict which HTTP methods a route accepts.

```python
@app.route("/api/users", methods=["GET"])
def list_users(): return "List of users"

@app.route("/api/users", methods=["POST"])
def create_user(): return "User created"

# Multiple methods on one route
@app.route("/api/users/<id>", methods=["GET", "PUT", "DELETE"])
def handle_user(id):
    from flask import request
    if request.method == "GET": return f"Get user {id}"
    elif request.method == "PUT": return f"Update user {id}"
    elif request.method == "DELETE": return f"Delete user {id}"
```

**Why it exists:** Without method restrictions, every route accepts every method → someone can POST to a GET-only route → unexpected behavior, security issues.

**Where it's used:** REST APIs — GET for reading, POST for creating, PUT for updating, DELETE for deleting.

**What goes wrong without it:**
- No method specified → defaults to GET only → POST requests get 405 Method Not Allowed.
- Allowing all methods on one route → giant if/else for each method → messy. Use separate routes or Flask MethodView.

---

## Request Object (request)

**What:** `request` gives access to incoming data — form data, JSON body, query params, headers.

```python
from flask import request

@app.route("/search")
def search():
    query = request.args.get("q")          # query param: /search?q=hello
    page = request.args.get("page", 1)     # with default
    return f"Searching for {query}, page {page}"

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()              # JSON body
    name = data.get("name")
    email = data.get("email")
    return f"Created user {name}"

@app.route("/form", methods=["POST"])
def handle_form():
    name = request.form.get("name")        # form data
    return f"Hello, {name}"
```

**Why it exists:** Without the request object, you'd parse the raw HTTP body manually — complex and error-prone. `request` gives clean access to all incoming data.

**Where it's used:** Every route that receives data — form submissions, API endpoints, file uploads.

**What goes wrong without it:**
- `request.args` (query params) vs `request.form` (POST form) vs `request.get_json()` (JSON body) → using the wrong one → `None` → errors.
- `request.get_json()` on non-JSON request → returns None or raises → check `request.is_json` first.
- `request.args.get("q")` → returns None if missing. `request.args["q"]` → raises KeyError if missing. Use `.get()` with defaults.

---

## JSON Responses (jsonify)

**What:** `jsonify()` converts a Python dict to a JSON HTTP response with the correct content-type.

```python
from flask import jsonify

@app.route("/api/user/<id>")
def get_user(id):
    user = {"id": id, "name": "Akash", "age": 25}
    return jsonify(user)                    # → JSON response with 200

@app.route("/api/users")
def list_users():
    users = [{"id": 1, "name": "Akash"}, {"id": 2, "name": "Bob"}]
    return jsonify(users)                   # → JSON array response

# With custom status code
@app.route("/api/error")
def error():
    return jsonify({"error": "Not found"}), 404
```

**Why it exists:** Without `jsonify()`, you'd do `json.dumps(data)` and set content-type manually → verbose. `jsonify()` handles both in one call and sets the correct `application/json` header.

**Where it's used:** Every API endpoint that returns JSON.

**What goes wrong without it:**
- Returning a dict directly (Flask 2.0+) → works but `jsonify()` is more explicit and sets headers correctly.
- Returning a string → content-type is `text/html` → API clients expecting JSON fail.
- Forgetting status code: `return jsonify({"error": "Not found"})` → returns 200 (success) → clients think it succeeded. Always return the correct status code.

---

## Templates (Jinja2)

**What:** Jinja2 templates let you generate HTML with dynamic data.

```python
from flask import render_template

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name, age=25)
```

```html
<!-- templates/profile.html -->
<h1>Hello, {{ name }}!</h1>
<p>You are {{ age }} years old.</p>

{% if age >= 18 %}
  <p>You are an adult.</p>
{% else %}
  <p>You are a minor.</p>
{% endif %}

{% for item in items %}
  <li>{{ item }}</li>
{% endfor %}
```

**Why it exists:** Without templates, you'd build HTML strings in Python: `f"<h1>Hello, {name}</h1>"` → messy, no logic, hard to maintain. Templates separate HTML from Python.

**Where it's used:** Server-rendered web pages, email templates, any HTML that needs dynamic data.

**What goes wrong without it:**
- Templates must be in a `templates/` folder → Flask won't find them elsewhere.
- XSS vulnerability: `{{ user_input|safe }}` → renders raw HTML → XSS attack. Never use `|safe` on user input.
- Forgetting to pass a variable → Jinja2 renders empty string (not an error) → silent bug.

---

## Template Inheritance

**What:** Templates can extend a base template — common layout (header, footer, nav) defined once, content overridden per page.

```html
<!-- templates/base.html -->
<html>
<head><title>{% block title %}My App{% endblock %}</title></head>
<body>
  <nav>Navigation here</nav>
  {% block content %}{% endblock %}
  <footer>Footer here</footer>
</body>
</html>

<!-- templates/profile.html -->
{% extends "base.html" %}
{% block title %}Profile{% endblock %}
{% block content %}
  <h1>User Profile</h1>
{% endblock %}
```

**Why it exists:** Without inheritance, you'd copy the header/footer into every template → change the nav, edit 20 files. Inheritance defines the layout once; pages just fill in the content blocks.

**Where it's used:** Every multi-page web app with a consistent layout.

**What goes wrong without it:**
- Forgetting `{% extends %}` → page renders without layout → no header/footer.
- Block name mismatch: `{% block content %}` in base, `{% block main %}` in child → content doesn't appear.
- Too many blocks → confusing. Keep it simple: title, content, maybe sidebar.

---

## Session Management

**What:** Flask sessions store user data across requests (like login state) using signed cookies.

```python
from flask import session

app.secret_key = "your-secret-key-here"    # REQUIRED for sessions

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    session["username"] = username          # store in session
    return f"Logged in as {username}"

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return "Please log in", 401
    return f"Welcome, {session['username']}"

@app.route("/logout")
def logout():
    session.pop("username", None)           # remove from session
    return "Logged out"
```

**Why it exists:** HTTP is stateless — each request is independent. Without sessions, you can't keep a user logged in across page loads. Sessions use cookies to maintain state.

**Where it's used:** Login systems, shopping carts, user preferences, flash messages.

**What goes wrong without it:**
- No `secret_key` → `RuntimeError: session is unavailable because no secret key was set`. Always set a strong, random secret key.
- Storing large data in session → cookies have a 4KB limit → data gets truncated.
- Secret key in source code → committed to git → security breach. Use environment variables.

---

## Blueprints

**What:** Blueprints let you organize routes into modules — like mini-apps that get registered on the main app.

```python
# users_bp.py
from flask import Blueprint
users_bp = Blueprint("users", __name__)

@users_bp.route("/users")
def list_users(): return "User list"

@users_bp.route("/users/<id>")
def get_user(id): return f"User {id}"

# app.py
from flask import Flask
from users_bp import users_bp

app = Flask(__name__)
app.register_blueprint(users_bp, url_prefix="/api")
# Now routes are: /api/users, /api/users/<id>
```

**Why it exists:** Without blueprints, all routes are in one file → 500-line `app.py` → unmaintainable. Blueprints split routes by feature: `users_bp`, `posts_bp`, `auth_bp`.

**Where it's used:** Any Flask app with more than a few routes. Essential for large applications.

**What goes wrong without it:**
- Blueprint not registered → routes don't exist → 404.
- `url_prefix` conflicts → two blueprints with `/api` prefix → URL conflicts.
- Circular imports: blueprint imports from app, app imports blueprint → `ImportError`. Use separate files.

---

## Error Handling

**What:** Custom error pages and API error responses.

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request", "details": str(error)}), 400
```

**Why it exists:** Without custom error handlers, Flask returns ugly HTML error pages → bad for APIs (clients expect JSON) and bad for users (confusing error pages).

**Where it's used:** Every production Flask app. APIs must return JSON errors, not HTML.

**What goes wrong without it:**
- Default 404 page → HTML → API client tries to parse JSON → fails → confusing error.
- Exposing stack traces in 500 errors → security risk (reveals code structure, file paths).
- Not handling 400 (bad request) → user gets generic error → doesn't know what they did wrong.
