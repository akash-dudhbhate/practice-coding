# Lesson 18 — Coding Check

## Easy

### p01-solve.py — Basic routes
- [ ] `GET /` returns home page text
- [ ] `GET /about` returns about text
- [ ] `GET /contact` returns contact text
- [ ] App runs without errors

### p02-solve.py — Greet API
- [ ] `GET /api/greet/Akash` returns `{"message": "Hello, Akash"}`
- [ ] Returns JSON (content-type: application/json)
- [ ] Uses jsonify()

### p03-solve.py — Search with query params
- [ ] `GET /api/search?q=hello` returns `{"query": "hello", "results": []}`
- [ ] Missing `q` parameter handled gracefully (default or error)
- [ ] Uses request.args.get()

## Medium

### p01-solve.py — Todo API
- [ ] `GET /todos` returns list of todos
- [ ] `POST /todos` with JSON body creates a todo, returns 201
- [ ] `DELETE /todos/<id>` removes a todo
- [ ] Todos stored in a list (in-memory)
- [ ] Each todo has id, title, done fields

### p02-solve.py — Session login
- [ ] `POST /login` with username sets session["username"]
- [ ] `GET /dashboard` returns welcome message if logged in
- [ ] `GET /dashboard` returns 401 if not logged in
- [ ] `GET /logout` clears session
- [ ] `secret_key` is set

### p03-solve.py — Blueprints
- [ ] `auth_bp` blueprint with login/register routes
- [ ] `api_bp` blueprint with CRUD routes
- [ ] Both registered with URL prefixes (e.g., /auth, /api)
- [ ] Routes are accessible at prefixed paths

## Hard

### p01-solve.py — Blog API with SQLite
- [ ] Posts table: id, title, content, created_at
- [ ] Comments table: id, post_id, content (FK to posts)
- [ ] `GET /api/posts` — list all posts
- [ ] `POST /api/posts` — create post
- [ ] `GET /api/posts/<id>` — get single post with comments
- [ ] `DELETE /api/posts/<id>` — delete post
- [ ] `POST /api/posts/<id>/comments` — add comment
- [ ] `GET /api/posts?tag=python` — filter by tag
- [ ] Error handlers for 404, 400, 500 returning JSON

### p02-solve.py — Flask with templates
- [ ] `base.html` with nav and `{% block content %}`
- [ ] `index.html` extends base, lists posts
- [ ] `detail.html` extends base, shows single post
- [ ] `create.html` extends base, has form to create post
- [ ] `GET /` renders index with posts
- [ ] `GET /post/<id>` renders detail page
- [ ] `GET /create` renders form, `POST /create` handles submission

### p03-solve.py — Decorator middleware
- [ ] `@require_auth` checks for `X-API-Key` header, returns 401 if missing
- [ ] `@rate_limit` limits to N requests per IP per minute (using dict)
- [ ] `@log_request` prints method, path, and response status
- [ ] All three decorators can stack on one route
- [ ] Decorators use functools.wraps
