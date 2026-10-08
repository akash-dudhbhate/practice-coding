# 45 — Building a REST API endpoint: route → service → db layers

> **Interview question:** "Walk me through building a REST API endpoint. How do you structure the code?"
> **What the interviewer is really testing:** Whether you separate concerns or dump SQL inside the HTTP handler — and whether you know *why*.

## Theory — what it is

A layered design splits an endpoint into three tiers, each with one job:

- **Route layer** (a.k.a. controller/handler): speaks HTTP. Parses the request, validates input shape, calls the service, maps the result to a status code + JSON response. No business logic, no SQL.
- **Service layer**: speaks *business*. "Register a user", "cancel an order". Enforces rules, orchestrates multiple db calls, raises domain errors like `UserAlreadyExists`. Knows nothing about HTTP or SQL.
- **DB/repository layer**: speaks storage. Runs the actual queries, returns plain objects. Knows nothing about business rules or HTTP.

The rule that makes it work: **dependencies point down, never up**. Routes call services; services call repositories; repositories never call routes.

## Why it was needed

Without layers you get the "fat view" — a 200-line Flask/Django view that parses JSON, checks permissions, runs raw SQL, sends an email, and formats the response. That code is:

- **Untestable**: to test "duplicate email is rejected" you must spin up HTTP + a real DB.
- **Unreusable**: the "register user" logic can't be called from a CLI command or a Celery job because it's welded to a request object.
- **Unreviewable**: a bug in SQL sits next to a bug in status codes, and diffs touch everything.

Layers let you test business rules with plain function calls, swap the DB without touching routes, and reuse logic across endpoints.

## Where it's used in a real project

- **FastAPI/Flask/Django apps**: routers stay thin (5–15 lines), services hold the rules, repositories hold the queries.
- **Background workers**: a Celery task calls the *same* `OrderService.cancel()` the REST endpoint calls — no copy-pasted logic.
- **Testing**: unit tests hit the service layer with a fake repository; only a few integration tests go through real HTTP.
- **Multiple front-ends**: REST + GraphQL + admin CLI all reuse one service layer.

## Diagram

```
 HTTP POST /users  {"email": "a@b.com"}
        |
        v
 +-----------------------------+
 | ROUTE (users_api.py)        |  validate JSON, pick status code
 |   create_user_endpoint()    |
 +-----------------------------+
        |  calls service (no SQL, no Request object passed down)
        v
 +-----------------------------+
 | SERVICE (user_service.py)   |  business rules: "email must be unique"
 |   register_user(email)      |  raises UserAlreadyExists -> route maps to 409
 +-----------------------------+
        |  calls repo (returns domain objects, not rows)
        v
 +-----------------------------+
 | REPOSITORY (user_repo.py)   |  SQL / ORM lives here and ONLY here
 |   find_by_email(), save()   |
 +-----------------------------+
        |
        v
     DATABASE
```

## Code — explained

```python
# ---------- repository layer ----------
class UserRepo:                                        # 1
    def __init__(self, conn):
        self.conn = conn                               # 2
    def find_by_email(self, email):
        return self.conn.execute(
            "SELECT id, email FROM users WHERE email=?", (email,)
        ).fetchone()                                   # 3
    def save(self, email):
        cur = self.conn.execute("INSERT INTO users(email) VALUES(?)", (email,))
        return cur.lastrowid                           # 4

# ---------- service layer ----------
class UserAlreadyExists(Exception):                    # 5
    pass

class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo                               # 6
    def register_user(self, email: str) -> dict:
        email = email.strip().lower()                  # 7
        if self.repo.find_by_email(email):
            raise UserAlreadyExists(email)             # 8
        uid = self.repo.save(email)
        return {"id": uid, "email": email}             # 9

# ---------- route layer (FastAPI) ----------
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr               # 10

app = FastAPI()

class CreateUser(BaseModel):
    email: str                                         # 11

@app.post("/users", status_code=201)
def create_user(body: CreateUser):                     # 12
    try:
        return service.register_user(body.email)       # 13
    except UserAlreadyExists:
        raise HTTPException(status_code=409, detail="email taken")  # 14
```

1. `UserRepo` wraps every SQL statement touching the `users` table. If you swap SQLite for Postgres, only this file changes.
2. The connection is passed in — the repo doesn't know how it was made (easy to swap for a fake in tests).
3. `find_by_email` returns a row or `None`; the repo decides *how* to look, callers just ask.
4. `save` returns the new id — a plain value, not a cursor, so callers never see DB details.
5. A domain exception. The service signals *what went wrong in business terms*, not SQL errors or HTTP codes.
6. The service depends on the repo's *interface*, injected via `__init__` — this is dependency injection (see file 47).
7. Business rule: normalize emails before comparing — lives here, not in the route.
8. Business rule: duplicates are rejected. A CLI script calling `register_user` gets the same protection for free.
9. Returns a plain dict/dataclass — the route layer decides how to serialize it.
10. Pydantic model = the *input contract*: request body is validated before your code even runs.
11. `email: str` — with `EmailStr` (needs `pip install email-validator`) FastAPI rejects malformed emails automatically with a 422.
12. The route is 4 lines: parse → call → translate. That's the goal — routes should be boring.
13. On success return the dict; FastAPI serializes it to JSON with the 201 status from the decorator.
14. Domain exception → HTTP 409. The mapping table (domain error ↔ status code) lives at the HTTP edge, where it belongs.

## Problems

### Easy — which layer?
**Problem:** Write a function `which_layer(task)` that classifies a task string as `"route"`, `"service"`, or `"repo"` using keyword rules.
**Try this input:** `which_layer("check email is unique")`, `which_layer("run INSERT INTO users")`, `which_layer("return HTTP 201")`
**Expected output:** `"service"`, `"repo"`, `"route"`
**Solution:**
```python
def which_layer(task: str) -> str:
    t = task.lower()
    if any(w in t for w in ("http", "status", "request", "json body")):
        return "route"
    if any(w in t for w in ("select", "insert", "update", "delete", "query", "sql")):
        return "repo"
    return "service"          # business rules are the default bucket

print(which_layer("check email is unique"))   # service
print(which_layer("run INSERT INTO users"))   # repo
print(which_layer("return HTTP 201"))         # route
```
**Logic explained:**
1. Route keywords are anything HTTP-shaped: status codes, request/response, JSON parsing.
2. Repo keywords are SQL verbs — if a sentence mentions a query, it belongs in the repository.
3. Everything else ("must be unique", "only admins can", "apply discount") is a business rule → service layer.

### Medium — service with a fake repo
**Problem:** Implement `UserService.register_user` from above and test it with an in-memory fake repo (no DB). Show that a duplicate registration raises `UserAlreadyExists`.
**Try this input:** register `"A@B.com"` then `"a@b.com"`
**Expected output:** first returns `{'id': 1, 'email': 'a@b.com'}`; second raises `UserAlreadyExists`
**Solution:**
```python
class UserAlreadyExists(Exception):
    pass

class FakeRepo:                       # same interface, dict instead of SQL
    def __init__(self):
        self.rows = {}
        self.next_id = 1
    def find_by_email(self, email):
        return self.rows.get(email)
    def save(self, email):
        uid = self.next_id
        self.next_id += 1
        self.rows[email] = {"id": uid, "email": email}
        return uid

class UserService:
    def __init__(self, repo):
        self.repo = repo
    def register_user(self, email):
        email = email.strip().lower()
        if self.repo.find_by_email(email):
            raise UserAlreadyExists(email)
        return {"id": self.repo.save(email), "email": email}

svc = UserService(FakeRepo())
print(svc.register_user("A@B.com"))   # {'id': 1, 'email': 'a@b.com'}
try:
    svc.register_user("a@b.com")
except UserAlreadyExists:
    print("UserAlreadyExists raised") # <- duplicate caught by the SERVICE
```
**Logic explained:**
1. `FakeRepo` implements the same two methods with a dict — the service can't tell the difference because it only depends on the interface.
2. The first call normalizes `"A@B.com"` → `"a@b.com"`, finds nothing, saves, returns id 1.
3. The second call normalizes to the *same* email, `find_by_email` hits, and the domain exception fires — no HTTP needed to prove the rule works. This is exactly why the layer exists.

### Hard — full pipeline end-to-end
**Problem:** Wire the real `UserRepo` (sqlite3) + `UserService` + a route-style function `handle_create_user(body: dict)` that returns `(status_code, json_dict)` — mimicking what a FastAPI handler does. Register two users, reject a duplicate with 409, reject a missing email with 422.
**Try this input:** `{"email": "x@y.com"}`, `{"email": "X@y.com"}`, `{}`
**Expected output:** `(201, {'id': 1, 'email': 'x@y.com'})`, `(409, {'detail': 'email taken'})`, `(422, {'detail': 'email required'})`
**Solution:**
```python
import sqlite3

class UserRepo:
    def __init__(self, conn):
        self.conn = conn
        conn.execute("CREATE TABLE IF NOT EXISTS users"
                     "(id INTEGER PRIMARY KEY, email TEXT UNIQUE)")
    def find_by_email(self, email):
        return self.conn.execute(
            "SELECT id, email FROM users WHERE email=?", (email,)).fetchone()
    def save(self, email):
        return self.conn.execute(
            "INSERT INTO users(email) VALUES(?)", (email,)).lastrowid

class UserAlreadyExists(Exception):
    pass

class UserService:
    def __init__(self, repo):
        self.repo = repo
    def register_user(self, email):
        email = email.strip().lower()
        if self.repo.find_by_email(email):
            raise UserAlreadyExists(email)
        return {"id": self.repo.save(email), "email": email}

def handle_create_user(body: dict):              # the "route" in plain Python
    email = body.get("email")
    if not email:                                # pydantic would do this for us
        return 422, {"detail": "email required"}
    try:
        return 201, svc.register_user(email)
    except UserAlreadyExists:
        return 409, {"detail": "email taken"}

svc = UserService(UserRepo(sqlite3.connect(":memory:")))
print(handle_create_user({"email": "x@y.com"}))   # (201, {...})
print(handle_create_user({"email": "X@y.com"}))   # (409, email taken)
print(handle_create_user({}))                     # (422, email required)
```
**Logic explained:**
1. `handle_create_user` is the route layer: it validates the raw dict, calls the service, and translates exceptions into status codes — precisely what FastAPI + `HTTPException` automate.
2. The service enforces uniqueness via `find_by_email`; note `"X@y.com"` → `"x@y.com"` normalization makes the duplicate check work.
3. The repo owns the SQL. Swapping `:memory:` SQLite for Postgres changes only `UserRepo`.
4. Outputs: 201 success, 409 domain conflict, 422 validation failure — the three codes interviewers expect you to name.

## The 30-second interview answer

"I split endpoints into three layers: the route layer handles HTTP — parsing, validation, status codes — and nothing else. The service layer holds business rules like 'emails must be unique' and raises domain exceptions. The repository layer owns the SQL and returns plain objects. Arrows only point down, so the service doesn't know about HTTP and the repo doesn't know about rules. The payoff is testability — I unit test services with a fake repo — and reusability, since a Celery job or CLI can call the same service the endpoint uses."

## Follow-up trap

**"Where does validation live — route or service?"** Answer: *both, different kinds*. Shape validation (is `email` present and string-shaped?) belongs at the route/Pydantic edge — reject garbage early with 422. Rule validation (is this email already taken? does the user have permission?) needs DB state and belongs in the service — return 409/403 from domain exceptions. If they push further: "what about transactions?" — the service owns transaction boundaries (it orchestrates multiple repo calls that must commit or roll back together), not the repo, since a transaction often spans several tables.
