# 43 — Flask vs Django vs FastAPI — when to pick each

> **Interview question:** "When would you pick Flask vs Django vs FastAPI?"
> **What the interviewer is really testing:** Whether you match frameworks to problems — batteries-included vs micro vs async-first — not which one you personally like.

## Theory — what it is

All three are Python web frameworks, but they answer different questions. **Django** (2005) is *"batteries included"*: ORM, admin panel, auth, migrations, templating, sessions — a monolith designed to get a full database-backed site shipped fast. Convention over configuration: Django decides the structure, you fill it in.

**Flask** (2010) is a *microframework*: a routing layer plus request/response handling, that's it. No ORM, no auth, no admin — you plug in what you need (SQLAlchemy, Flask-Login). Small core, maximum freedom. Synchronous (WSGI) at heart — each request is handled one-at-a-time per worker.

**FastAPI** (2018) is *async-first and type-first*: built on Starlette (ASGI) + Pydantic. You declare request/response shapes with Python type hints; it auto-generates validation, serialization, and OpenAPI docs. Native `async def` endpoints mean it can juggle thousands of concurrent I/O-bound connections per process.

## Why it was needed

Django solved 2005's problem: building content sites (it was born at a newspaper) meant re-writing auth, ORM, admin every project — so it shipped them all. Flask answered the backlash: many apps (APIs, microservices, prototypes) didn't want a monolith dictating structure — give me routing and get out of the way.

FastAPI answered the 2018 problem: microservices + high-concurrency I/O (DB calls, upstream APIs, websockets). Flask/Django-WSGI blocks a worker per request — 10k concurrent connections needs 10k workers. Async lets one worker interleave thousands of waiting requests. And Pydantic type-hint validation removed the hand-rolled `if "email" not in body` boilerplate every Flask/Django API rewrites.

## Where it's used in a real project

- **Django:** internal tools, admin-heavy CRUD apps, marketplaces, CMS — anything where "users + DB + admin panel" is 80% of the product. Instagram ran on Django.
- **Flask:** small services, prototypes, webhook receivers, ML model serving behind a simple API, apps where you want explicit control of every component.
- **FastAPI:** JSON microservices, BFF/API gateways, high-traffic I/O-bound APIs, ML inference endpoints (needs async + auto docs + strict validation).

## Diagram

```
                    batteries-included        minimal core          async + types
Django    :   request -> middleware -> ORM -> admin/auth/sessions -> response
              (monolith: you get everything, it picks the structure)

Flask     :   request -> route -> YOUR code (+ your chosen libs) -> response
              (WSGI sync; extension for every need)

FastAPI   :   request -> Pydantic validate -> async def endpoint -> response
              (ASGI: one worker interleaves many in-flight requests;
               OpenAPI docs auto-generated from your type hints)

Concurrency sketch (I/O-bound work):
  sync (Flask/Django-WSGI):  req1 ====wait====   req2 ====wait====   (serial)
  async (FastAPI):           req1 --wait--       req1 resumes
                             req2 ====         req2 resumes         (interleaved)
```

## Code — explained

```python
# Flask — minimal, sync
from flask import Flask, request
app = Flask(__name__)

@app.post("/users")
def create_user():
    body = request.get_json()          # manual: no validation built in
    return {"id": 1, "name": body["name"]}, 201

# FastAPI — type-hinted, async, self-validating
from fastapi import FastAPI
from pydantic import BaseModel
app2 = FastAPI()

class UserIn(BaseModel):               # declares shape + types
    name: str
    age: int

@app2.post("/users")
async def create_user2(u: UserIn):     # invalid body -> 422 automatically
    return {"id": 1, **u.model_dump()} # docs at /docs for free
```

1. Flask: `request.get_json()` hands you a raw dict — `body["name"]` KeyErrors on bad input; you write validation yourself (or add marshmallow/pydantic).
2. FastAPI: `UserIn(BaseModel)` declares the contract — a missing `name` or non-int `age` gets an automatic `422` with field-level errors, before your code runs.
3. `async def` lets the endpoint await DB/HTTP calls without blocking the worker.
4. `u.model_dump()` serializes the validated model; Swagger UI appears at `/docs` with zero config.
5. Django's equivalent lives in views + forms/serializers inside a bigger app skeleton — more files, more structure, much more included.

## Problems

### Easy — pick the framework
**Problem:** For each, name the best fit: (a) weekend prototype REST API, (b) internal inventory system with admin UI + auth, (c) API gateway fanning out to 5 upstream services concurrently.
**Expected output:** (a) Flask (or FastAPI), (b) Django, (c) FastAPI
**Solution:**
```python
choices = {
    "prototype": "Flask — fastest to stand up, zero ceremony",
    "inventory": "Django — admin, auth, ORM are the product",
    "gateway":   "FastAPI — asyncio.gather fans out without threads",
}
print(choices["gateway"])
# FastAPI — asyncio.gather fans out without threads
```
**Logic explained:**
1. Prototype = minimal boilerplate wins → Flask.
2. Admin + auth = don't rebuild what Django ships → Django.
3. Fan-out I/O = concurrency without threads → FastAPI's `async`/`await` + `asyncio.gather`.

### Medium — minimal FastAPI endpoint
**Problem:** Write a `POST /items` endpoint that accepts `{"name": str, "price": float}` with `price > 0`, and returns the item with an `id`.
**Try this input:** `{"name": "book", "price": 9.99}` valid; `{"name": "x", "price": -1}` invalid
**Expected output:** valid → `{"id": 1, "name": "book", "price": 9.99}`; invalid → `422`
**Solution:**
```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float = Field(gt=0)        # price must be > 0

@app.post("/items", status_code=201)
async def create_item(item: Item):
    return {"id": 1, **item.model_dump()}
```
**Logic explained:**
1. `Field(gt=0)` puts the price rule in the schema — no `if` in your handler.
2. FastAPI validates before calling `create_item`; bad input → automatic 422.
3. `async def` is free concurrency for the DB insert this would really do.

### Hard — async fan-out (why FastAPI wins here)
**Problem:** A gateway endpoint must call 3 upstream services and combine results. Show why `async` matters: naive sequential awaits vs `asyncio.gather`.
**Try this input:** each upstream takes 0.1s
**Expected output:** sequential ≈ 0.3s; `gather` ≈ 0.1s — and during waits, other requests get served
**Solution:**
```python
import asyncio, time

async def upstream(i):
    await asyncio.sleep(0.1)          # simulates an HTTP call
    return f"svc{i}"

async def handler_sequential():
    return [await upstream(i) for i in range(3)]   # 0.3s

async def handler_gather():
    return await asyncio.gather(*[upstream(i) for i in range(3)])  # 0.1s

async def main():
    t = time.perf_counter(); await handler_sequential()
    print(round(time.perf_counter() - t, 2))       # ~0.3
    t = time.perf_counter(); await handler_gather()
    print(round(time.perf_counter() - t, 2))       # ~0.1

asyncio.run(main())
```
**Logic explained:**
1. Sequential `await`s serialize the I/O — total = sum of latencies.
2. `asyncio.gather` starts all three calls, then awaits them together — total = max latency.
3. The bigger win: in FastAPI, *while* this handler awaits, the worker serves other requests — a sync Flask view would hold a worker hostage for the full duration.

## The 30-second interview answer

"Django when the app IS a database-backed product — admin, auth, ORM, migrations included; fastest path for CRUD-heavy sites and internal tools. Flask when you want a thin routing layer and full control — small services, prototypes, or teams who prefer composing their own stack; it's synchronous WSGI. FastAPI for I/O-bound JSON microservices and gateways — async ASGI handles high concurrency per process, Pydantic type hints give automatic validation, and OpenAPI docs are free. The real tradeoff: Django trades flexibility for velocity, Flask trades batteries for freedom, FastAPI trades maturity for async + validation. In practice: Django for the monolith, FastAPI for the microservices around it."

## Follow-up trap

**"So is FastAPI always faster than Flask?"** No — async only wins on *I/O-bound* work (DB calls, HTTP calls, websockets). For CPU-bound endpoints they're similar, and a single `await`ed blocking call (e.g., `requests.get` instead of `httpx`) silently serializes everything. Also expect: *"Can Django do async?"* — Django 3.1+ supports ASGI and async views, but the ORM's async support is newer/partial; FastAPI was async-native from day one. And: *"What about Flask's community/maturity?"* — Flask has the deepest extension ecosystem; FastAPI is newer but huge now.
