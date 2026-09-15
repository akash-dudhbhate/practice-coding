# Lesson 18 — Refactoring Challenges

## Refactor 01 (Easy): Inline Route Logic
### Before
```python
@app.route("/users")
def users():
    users = db.query("SELECT * FROM users")
    return json.dumps(users)
```
### After
```python
@app.route("/users")
def users():
    users = db.query("SELECT * FROM users")
    return jsonify(users)
```

## Refactor 02 (Medium): No Error Handler
### Before
```python
@app.route("/users/<id>")
def get_user(id):
    user = db.get(id)
    if not user:
        return "Not found", 404
    return jsonify(user)
```
### After
```python
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

@app.route("/users/<id>")
def get_user(id):
    user = db.get_or_404(id)
    return jsonify(user)
```

## Refactor 03 (Hard): Global State
### Before
```python
db = None
@app.before_first_request
def setup():
    global db
    db = connect_db()
```
### After
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
# No global state, managed by extension
```
