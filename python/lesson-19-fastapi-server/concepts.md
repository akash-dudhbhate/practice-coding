# Lesson 19 — Concepts Explained (FastAPI REST Server)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## FastAPI Framework

**What:** FastAPI is a modern, fast Python web framework for building APIs. It uses Python type hints for validation and auto-generates documentation.

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.get("/users/{user_id}")
def read_user(user_id: int):           # type hint → auto validation
    return {"user_id": user_id}

# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs (auto-generated Swagger UI)
```

**Why it exists:** Flask doesn't validate input or generate docs. FastAPI uses type hints to validate, serialize, and document automatically. Less code, fewer bugs, free documentation.

**Where it's used:** Modern Python APIs — used by Uber, Netflix, Microsoft. Replacing Flask for new API projects.

**What goes wrong without it:**
- Using Flask without validation → bad data reaches your database → corruption.
- No auto-docs → you write Swagger/OpenAPI specs manually → out of date → misleading.
- FastAPI is async-native → using sync code in it blocks the event loop (use `def` for sync, `async def` for async).

---

## Type Hints for Validation

**What:** FastAPI uses Python type hints to automatically validate inputs.

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):     # FastAPI validates the body
    return {"created": user.name}

# If you POST {"name": "Akash", "email": "a@b.com", "age": "twenty"}
# FastAPI returns 422: "age must be int" — automatic validation!
```

**Why it exists:** Without validation, bad data (string where int expected, missing fields) reaches your code → crashes or corrupts data. FastAPI validates before your code runs.

**Where it's used:** Every FastAPI endpoint. Type hints are the core of FastAPI.

**What goes wrong without it:**
- No type hints → no validation → `age` could be a string → `age + 1` → TypeError.
- Wrong type hint: `age: str` when you expect int → accepts "twenty" → bugs downstream.
- Optional fields: `age: Optional[int] = None` → field is optional. Forgetting `= None` → field is required → 422 if missing.

---

## Pydantic Models

**What:** Pydantic models define the shape of your data — field names, types, validation rules.

```python
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=50)  # required, 1-50 chars
    email: EmailStr                                       # validates email format
    age: int = Field(0, ge=0, le=150)                     # 0-150 range
    is_active: bool = True                                 # default True

# Auto-validation:
User(id=1, name="Akash", email="not-an-email")  # → ValidationError
User(id=1, name="", email="a@b.com", age=25)    # → ValidationError (name too short)
User(id=1, name="Akash", email="a@b.com", age=25)  # → OK
```

**Why it exists:** Without Pydantic, you validate manually: `if not email.contains("@"): return error`. Pydantic handles all validation declaratively — cleaner, less code, consistent.

**Where it's used:** Every FastAPI request/response model. Also used standalone for config management, data validation.

**What goes wrong without it:**
- No validation → garbage data in database → bugs, security issues.
- `Field(...)` → `...` means required. `Field(None)` → optional. Mixing these up → required fields accepted as None or vice versa.
- Pydantic v1 vs v2 → different syntax for validators. Check which version you're using.

---

## Path Parameters

**What:** Extract values from the URL path.

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):              # type hint → validated as int
    return {"user_id": user_id}

@app.get("/items/{item_id}/reviews/{review_id}")
def get_review(item_id: int, review_id: int):
    return {"item": item_id, "review": review_id}
```

**Why it exists:** Without path parameters, you'd parse the URL string manually → error-prone. FastAPI extracts and validates them automatically.

**Where it's used:** REST APIs — `/users/123`, `/posts/45/comments/6`.

**What goes wrong without it:**
- `user_id: int` → non-numeric path → 422 error (automatic). Without type hint → `user_id` is a string → `int(user_id)` might fail later.
- Path parameter name must match: `@app.get("/{id}")` with `def handler(user_id: int)` → FastAPI can't find `id` parameter → error.

---

## Query Parameters

**What:** Extract values from the query string (after `?` in URL).

```python
@app.get("/users")
def list_users(
    skip: int = 0,              # /users?skip=10
    limit: int = 10,            # /users?limit=20
    active: bool = True,        # /users?active=false
    name: str = None            # /users?name=Akash (optional)
):
    return {"skip": skip, "limit": limit, "active": active, "name": name}
```

**Why it exists:** Without query parameters, you can't filter, sort, or paginate. Query params are the standard way to pass optional filters to GET endpoints.

**Where it's used:** List endpoints — pagination (`page`, `limit`), filtering (`status`, `category`), sorting (`sort_by`, `order`).

**What goes wrong without it:**
- Default values: `skip: int = 0` → if not provided, defaults to 0. `skip: int` (no default) → required → 422 if missing.
- `bool` parsing: `?active=true`, `?active=1`, `?active=yes` all work. `?active=false`, `?active=0`, `?active=no` → False.
- Mixing path and query: `@app.get("/users/{id}")` with `def handler(id: int, detail: bool = False)` → `id` is path param, `detail` is query param. FastAPI figures this out automatically.

---

## Dependency Injection

**What:** FastAPI's `Depends()` lets you inject shared logic (database connections, auth, config) into routes.

```python
from fastapi import Depends

def get_db():
    db = create_connection()
    try:
        yield db          # provide the dependency
    finally:
        db.close()        # cleanup after request

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user:
        raise HTTPException(401, "Invalid token")
    return user

@app.get("/profile")
def profile(user = Depends(get_current_user), db = Depends(get_db)):
    return {"user": user.name}    # user and db are injected
```

**Why it exists:** Without DI, you'd copy-paste auth and DB connection code into every route. DI lets you define it once and inject it everywhere. Also makes testing easy — swap the dependency with a mock.

**Where it's used:** Database sessions, authentication, pagination params, common query params, rate limiting.

**What goes wrong without it:**
- Forgetting `Depends()`: `def profile(user = get_current_user)` → calls the function at import time, not per request. Must be `Depends(get_current_user)`.
- `yield` dependency: use `yield` for cleanup (close DB connection). Using `return` → no cleanup → resource leak.
- Circular dependencies: dependency A depends on B, B depends on A → infinite loop. Restructure.

---

## HTTPException

**What:** Raise HTTP errors with proper status codes and messages.

```python
from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = find_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# With custom headers
raise HTTPException(
    status_code=429,
    detail="Rate limit exceeded",
    headers={"Retry-After": "60"}
)
```

**Why it exists:** Without HTTPException, you'd return `{"error": "..."}` with 200 status → clients think it succeeded. HTTPException sets the correct status code automatically.

**Where it's used:** Every error case — not found (404), unauthorized (401), forbidden (403), validation (422), server error (500).

**What goes wrong without it:**
- Returning error with 200 status → clients parse it as success → bugs.
- Wrong status code: 400 for not-found (should be 404) → confusing API.
- Generic error message: `detail="Error"` → users don't know what went wrong. Be specific.

---

## Async in FastAPI

**What:** FastAPI supports async route handlers for I/O-bound operations.

```python
@app.get("/users/{id}")
async def get_user(id: int):
    user = await fetch_user_from_db(id)    # async DB call
    return user

# Sync version (for CPU-bound or non-async code)
@app.get("/users/{id}")
def get_user_sync(id: int):
    user = db.query(User).get(id)          # sync DB call
    return user
```

**Why it exists:** Async handlers let FastAPI handle thousands of concurrent requests. Sync handlers run in a thread pool (slower but still works).

**Where it's used:** Async for I/O (database, API calls, file operations). Sync for CPU-bound or when using sync libraries (like regular SQLAlchemy).

**What goes wrong without it:**
- `async def` with sync blocking calls (e.g., `time.sleep(5)`) → blocks the event loop → ALL other requests freeze. Use `await asyncio.sleep(5)` or make it `def` (sync).
- `def` (sync) with async libraries → can't `await` → error. Use `async def`.
- Mixing: some routes async, some sync → fine, FastAPI handles both. But don't call async from sync or vice versa without proper handling.

---

## Auto Documentation (Swagger / ReDoc)

**What:** FastAPI auto-generates interactive API documentation at `/docs` (Swagger UI) and `/redoc` (ReDoc).

```python
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="A sample API for managing users",
    version="1.0.0"
)

@app.get("/users", tags=["users"], summary="List all users")
def list_users():
    """Get a list of all users in the system."""
    return []
```

Visit `http://localhost:8000/docs` → interactive UI where you can test endpoints.

**Why it exists:** Without auto-docs, you write API documentation manually → always out of date → misleading. FastAPI generates docs from your code → always accurate.

**Where it's used:** Every FastAPI project. Share the `/docs` URL with frontend developers → they can see and test all endpoints.

**What goes wrong without it:**
- No descriptions/tags → docs show bare endpoint info → not helpful. Add `tags`, `summary`, `description`.
- Breaking changes without updating docs → but with FastAPI, docs are always in sync (generated from code).
- Exposing `/docs` in production → reveals your API structure to attackers. Disable with `FastAPI(docs_url=None)`.

---

## Response Models

**What:** Define what the API returns (separate from what it accepts) using `response_model`.

```python
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    # NO password field → not exposed in response

class UserCreate(BaseModel):
    name: str
    email: str
    password: str          # accepted on input

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    # user has password, but response_model filters it out
    return user            # only id, name, email are returned
```

**Why it exists:** Without response models, you might accidentally return sensitive fields (passwords, tokens, internal IDs). `response_model` filters the output to only include specified fields.

**Where it's used:** Every endpoint that returns data — especially when input and output have different fields.

**What goes wrong without it:**
- Returning the full user object → password hash is in the response → security breach.
- `response_model` doesn't match return type → FastAPI tries to convert → might fail or drop fields.
- Forgetting `response_model` → returns whatever you return → no filtering → potential data leak.
