# Lesson 19 — FastAPI REST Server

## What you'll learn
- FastAPI app setup and routing
- Type hints for automatic validation
- Pydantic models (request/response)
- Path and query parameters
- Dependency injection (Depends)
- HTTPException for errors
- Async handlers
- Auto documentation (Swagger/ReDoc)
- Response models

## Lesson

### Basic FastAPI
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root(): return {"message": "Hello"}

# Run: uvicorn main:app --reload
```

### With Pydantic
```python
class Item(BaseModel):
    name: str
    price: float = Field(gt=0)

@app.post("/items", response_model=Item)
def create_item(item: Item): return item
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Create a FastAPI app with `GET /` returning `{"status": "ok"}` and `GET /items/{id}` returning `{"item_id": id}` (id is int).
2. `easy/p02-solve.py` — Create a Pydantic model `Product` (name: str, price: float, in_stock: bool = True). Create `POST /products` that accepts and returns the product.
3. `easy/p03-solve.py` — Create `GET /users` with query params: `skip` (int, default 0), `limit` (int, default 10), `active` (bool, default True). Return the params as JSON.

### Medium
4. `medium/p01-solve.py` — Build a todo API: `GET /todos` (list), `POST /todos` (create with Pydantic model), `PUT /todos/{id}` (update), `DELETE /todos/{id}` (delete). Use in-memory list.
5. `medium/p02-solve.py` — Create a dependency `get_pagination` that extracts `page` and `size` query params. Use it in a `GET /items` route. The dependency returns `{"skip": ..., "limit": ...}`.
6. `medium/p03-solve.py` — Create a `UserCreate` model (name, email, password) and `UserResponse` model (id, name, email — NO password). `POST /users` accepts UserCreate, returns UserResponse. Verify password is not in the response.

### Hard
7. `hard/p01-solve.py` — Build a complete FastAPI CRUD API for books with SQLite. Pydantic models for input/output, dependency for DB connection, error handling (404, 400), pagination, and filtering by author.
8. `hard/p02-solve.py` — Build a FastAPI auth system: `POST /register` (create user), `POST /login` (return JWT token), `GET /me` (protected, requires token via dependency). Use python-jose for JWT.
9. `hard/p03-solve.py` — Build a FastAPI app with async endpoints: `GET /weather/{city}` that simulates fetching weather (asyncio.sleep), `POST /notify` that sends notifications concurrently to multiple users using asyncio.gather.

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
- Test with: `uvicorn filename:app --reload`
- Visit `/docs` for auto-generated Swagger UI.
