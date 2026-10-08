# 47 — Dependency injection and FastAPI's `Depends`

> **Interview question:** "What is dependency injection, and how does FastAPI's `Depends` work?"
> **What the interviewer is really testing:** Whether you understand DI as a *design pattern* (inverting who creates what), not just a FastAPI keyword you copy-paste.

## Theory — what it is

A **dependency** is anything a function needs that it doesn't make itself: a DB connection, a config object, an HTTP client, the current user. **Dependency injection (DI)** means the function *receives* its dependencies as parameters instead of constructing or importing them.

Without DI: `def handler(): db = PostgresDB("prod-url")` — the function *decides* what DB it gets, forever. With DI: `def handler(db):` — the *caller* decides. This is called **inversion of control**: control over "what to use" moves from the function to whoever calls it.

FastAPI's **`Depends`** is DI built into the framework. You declare `def endpoint(db = Depends(get_db))` and FastAPI calls `get_db()` for you, passes the result in, and — if `get_db` is a generator — runs its cleanup after the response is sent. Dependencies can themselves declare dependencies, forming a tree FastAPI resolves per request.

## Why it was needed

Hard-coded dependencies make code untestable and rigid:

- `UserService()` that internally does `psycopg2.connect(PROD_URL)` can't be tested without a real Postgres.
- `get_current_user()` reading a global `settings` object can't be configured per-test.
- Shared resources (DB connections) need *per-request* lifecycles — open at request start, close at end — which the function itself can't manage cleanly.

DI lets tests swap a `FakeRepo` for `PostgresRepo`, lets `Depends(get_db)` guarantee connections close, and lets one function serve every environment without `if os.environ == "test"` branches inside business logic.

## Where it's used in a real project

- **DB sessions**: `Depends(get_db)` yields a session per request and closes it — the #1 use case.
- **Auth**: `Depends(get_current_user)` parses the JWT once; every protected route just declares it.
- **Tests**: `app.dependency_overrides[get_db] = fake_db` swaps the real dependency for a fake — no monkeypatching.
- **Shared clients**: a `Depends(get_http_client)` returning a pooled `httpx.AsyncClient` instead of creating one per call.

## Diagram

```
request GET /me  (Authorization: Bearer <jwt>)
      |
      v
FastAPI builds the dependency tree for this endpoint:

  get_db() ─────────────┐
      | yields session   |        endpoint(session, user)
      v                  |
  get_current_user( ─────┤   -->   runs business logic
      token=Depends(     |            |
        oauth2_scheme))  |            v
      |                  |        response sent
      v                  |            |
  decodes JWT, loads     |        get_db cleanup runs:
  user from DB           |        session.close() after yield
```

## Code — explained

```python
from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()

# --- a dependency is just a callable ---
def get_db():                                            # 1
    db = FakeSession()                                   # 2
    try:
        yield db                                         # 3
    finally:
        db.close()                                       # 4

def get_current_user(authorization: str = Header(...)):  # 5
    token = authorization.removeprefix("Bearer ")
    user = decode_jwt(token)                             # 6
    if user is None:
        raise HTTPException(401, "bad token")            # 7
    return user

@app.get("/me")
def read_me(user = Depends(get_current_user),            # 8
            db   = Depends(get_db)):                     # 9
    return db.get_user(user["id"])                       # 10

# --- tests override, no monkeypatching ---
app.dependency_overrides[get_db] = lambda: FakeSession() # 11
```

1. A dependency is any callable — a function, class, or `__call__` object. Generator functions get lifecycle support.
2. Open the resource — here a fake DB session; in prod, `SessionLocal()` from SQLAlchemy.
3. `yield` hands the session to the endpoint. Everything after `yield` is teardown.
4. `finally: db.close()` runs after the response — guaranteed cleanup even on exceptions. This replaces try/finally boilerplate in every endpoint.
5. `Header(...)` means "read the `Authorization` header" — dependencies can themselves take request data. `...` = required.
6. Decode the token, look up the user — auth logic lives in ONE place, not copied into 40 endpoints.
7. Raising `HTTPException` inside a dependency short-circuits the request — the endpoint never runs. Clean 401 handling.
8. `Depends(get_current_user)` tells FastAPI: "call it, give me the result." The endpoint receives a plain `user` dict — fully decoupled from headers.
9. Same for the DB session — declared, not constructed.
10. The endpoint is one line of business logic. All plumbing was injected.
11. In tests: `dependency_overrides` maps the real dependency to a fake. TestClient calls then use `FakeSession` — no network, no Postgres, and no `mock.patch` gymnastics.

## Problems

### Easy — spot the injection
**Problem:** Without any framework, rewrite this rigid code so `mailer` is injected. `send_alert(msg)` currently creates `SmtpMailer()` internally.
**Try this input:** call `send_alert("disk full", FakeMailer())`
**Expected output:** `FAKE sent: disk full`
**Solution:**
```python
class SmtpMailer:
    def send(self, msg): print("SMTP sent:", msg)

class FakeMailer:                    # same interface: has .send(msg)
    def send(self, msg): print("FAKE sent:", msg)

# before:  def send_alert(msg): SmtpMailer().send(msg)   # hard-coded!
def send_alert(msg, mailer):         # after: dependency injected
    mailer.send(msg)

send_alert("disk full", FakeMailer())    # FAKE sent: disk full
send_alert("disk full", SmtpMailer())    # SMTP sent: disk full
```
**Logic explained:**
1. The function signature gains a `mailer` parameter — that's the entire pattern. DI is boring on purpose.
2. `FakeMailer` works because both classes have `.send(msg)` — Python's duck typing means no interface declaration needed.
3. Production code calls `send_alert(msg, real_mailer)`; tests call it with a fake. Same function, different dependency.

### Medium — a mini `Depends`
**Problem:** Implement a 20-line DI container: `resolve(fn)` inspects `fn`'s parameters, calls each parameter's registered provider, and calls `fn` with the results. Register `get_db` → `FakeSession`.
**Try this input:** `def handler(db=USE(get_db))` → `resolve(handler)` returns what `handler(db)` returns
**Expected output:** `query ran on FakeSession`
**Solution:**
```python
import inspect

def USE(provider):                   # marker object like Depends()
    return ("USE", provider)

def resolve(fn):
    kwargs = {}
    for name, param in inspect.signature(fn).parameters.items():
        default = param.default              # Parameter object -> its .default
        if isinstance(default, tuple) and default[0] == "USE":
            kwargs[name] = default[1]()      # call the provider
    return fn(**kwargs)

class FakeSession:
    def query(self): return "query ran on FakeSession"

def get_db():
    return FakeSession()

def handler(db=USE(get_db)):
    return db.query()

print(resolve(handler))    # query ran on FakeSession
```
**Logic explained:**
1. `USE(provider)` is a default value that *marks* the parameter — exactly what `Depends(get_db)` is: a marker FastAPI reads off the signature.
2. `resolve` walks the signature; when a default is a `USE` marker it calls the provider and passes the result.
3. That's genuinely how FastAPI works under the hood — signature inspection at route-registration time, providers called per request. FastAPI adds caching, nested dependencies, and `yield`-teardown.

### Hard — override in a real FastAPI app
**Problem:** Build a tiny FastAPI app where `GET /items` depends on `get_repo`. In the test, override `get_repo` with a fake returning `[{"id": 1}]` and assert the endpoint returns it — proving `dependency_overrides` works.
**Try this input:** `TestClient(app).get("/items")`
**Expected output:** `200` and `[{'id': 1, 'name': 'fake'}]`
**Solution:**
```python
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

app = FastAPI()

class RealRepo:
    def all(self): return [{"id": 0, "name": "real"}]   # would hit prod DB

class FakeRepo:
    def all(self): return [{"id": 1, "name": "fake"}]

def get_repo():
    return RealRepo()

@app.get("/items")
def items(repo = Depends(get_repo)):
    return repo.all()

app.dependency_overrides[get_repo] = lambda: FakeRepo()  # the swap

r = TestClient(app).get("/items")
print(r.status_code, r.json())   # 200 [{'id': 1, 'name': 'fake'}]
```
**Logic explained:**
1. The endpoint never constructs `RealRepo` — it asks for whatever `get_repo` provides.
2. `dependency_overrides[get_repo]` remaps the provider *by function object* — the key is the original callable.
3. Result: the test exercises the full HTTP stack (routing, serialization, status code) while the DB layer is a dict — the sweet spot between unit and integration test.

## The 30-second interview answer

"Dependency injection means a function receives what it needs instead of building it — the caller decides which implementation to hand in, which makes swapping a real DB for a fake in tests trivial. FastAPI's `Depends` automates this: I write a provider function like `get_db`, declare it in the endpoint signature, and FastAPI calls it per request. Generator providers get `yield`-based cleanup, so sessions close after the response. Dependencies can depend on other dependencies — `get_current_user` uses the auth header and the DB session — and `app.dependency_overrides` lets tests replace any of them without monkeypatching."

## Follow-up trap

**"How do you test an endpoint that depends on `get_current_user` without a real JWT?"** Answer: `app.dependency_overrides[get_current_user] = lambda: {"id": 1, "role": "admin"}` — override the auth dependency itself, don't forge tokens. Related trap: **"is `Depends` re-run per request?"** Yes — dependencies execute per request by default (there's `use_cache` per request, dedup'd within one request). So `Depends(expensive_setup)` in a hot path can hurt; move true singletons (connection pools, HTTP clients) to app startup (`lifespan`/module level) and inject the *pool*, not the connection.
