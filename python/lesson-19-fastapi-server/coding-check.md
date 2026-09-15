# Lesson 19 — Coding Check

## Easy

### p01-solve.py — Basic FastAPI
- [ ] `GET /` returns `{"status": "ok"}`
- [ ] `GET /items/5` returns `{"item_id": 5}`
- [ ] `GET /items/abc` returns 422 (validation error — id must be int)
- [ ] Auto-docs at `/docs` work

### p02-solve.py — Product model
- [ ] `POST /products` with valid JSON returns the product
- [ ] Missing `name` → 422 validation error
- [ ] `price` is required
- [ ] `in_stock` defaults to True if not provided

### p03-solve.py — Query params
- [ ] `GET /users` returns defaults: skip=0, limit=10, active=True
- [ ] `GET /users?skip=5&limit=20` returns those values
- [ ] `GET /users?active=false` returns active=False
- [ ] Wrong type (`?skip=abc`) → 422 error

## Medium

### p01-solve.py — Todo CRUD API
- [ ] `GET /todos` returns list of todos
- [ ] `POST /todos` creates and returns todo with 201
- [ ] `PUT /todos/{id}` updates a todo
- [ ] `DELETE /todos/{id}` deletes a todo
- [ ] 404 for non-existent todo on PUT/DELETE
- [ ] Uses Pydantic model for todo

### p02-solve.py — Pagination dependency
- [ ] `get_pagination` is a dependency function
- [ ] Extracts `page` (default 1) and `size` (default 10)
- [ ] Returns `{"skip": (page-1)*size, "limit": size}`
- [ ] `GET /items` uses `Depends(get_pagination)`
- [ ] Query params work: `/items?page=3&size=5`

### p03-solve.py — Response model filtering
- [ ] `UserCreate` has: name, email, password
- [ ] `UserResponse` has: id, name, email (NO password)
- [ ] `POST /users` accepts UserCreate
- [ ] Response does NOT contain password field
- [ ] Uses `response_model=UserResponse`

## Hard

### p01-solve.py — Books API with SQLite
- [ ] Books table: id, title, author, year, isbn
- [ ] `GET /books` with pagination and `?author=` filter
- [ ] `POST /books` creates a book
- [ ] `GET /books/{id}` returns single book (404 if not found)
- [ ] `PUT /books/{id}` updates a book
- [ ] `DELETE /books/{id}` deletes a book
- [ ] DB connection via dependency (yield)
- [ ] Pydantic models for input and output

### p02-solve.py — JWT Auth
- [ ] `POST /register` creates a user (hash password)
- [ ] `POST /login` validates credentials, returns JWT token
- [ ] `GET /me` requires Authorization: Bearer token
- [ ] `GET /me` without token → 401
- [ ] `GET /me` with invalid token → 401
- [ ] `GET /me` with valid token → returns user info
- [ ] Uses Depends() for auth

### p03-solve.py — Async endpoints
- [ ] `GET /weather/{city}` is async (async def)
- [ ] Uses `await asyncio.sleep()` to simulate fetch
- [ ] `POST /notify` sends to multiple users concurrently
- [ ] Uses `asyncio.gather()` for concurrent notifications
- [ ] Total time for 3 notifications is ~1x (not 3x)
