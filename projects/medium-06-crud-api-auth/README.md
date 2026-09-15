# Medium Project 06 — Full CRUD API with Auth

> **Type:** Medium Project
> **Subject:** Python
> **Estimated sell price:** $300–500
> **Difficulty:** Intermediate
> **Prerequisites:** Lessons 01–15 (Python basics through FastAPI)

## Project Brief

Build a complete REST API with CRUD operations, JWT authentication, input validation, and error handling. This is a sellable product — many businesses need a backend API for their mobile/web apps.

## What you'll build

A FastAPI application with:
- User registration and login (JWT auth)
- CRUD operations for a resource (e.g., books, products, or contacts)
- Input validation with Pydantic
- Error handling with proper HTTP status codes
- SQLite database
- Auto-generated API documentation (Swagger UI)

## Skills you'll demonstrate

- FastAPI framework
- JWT authentication
- SQLite database operations
- Pydantic validation
- REST API design
- Error handling

## Requirements

- [ ] POST /auth/register — create user (username, email, password)
- [ ] POST /auth/login — return JWT token
- [ ] GET /items — list all items for authenticated user (with pagination)
- [ ] POST /items — create item (requires auth)
- [ ] GET /items/{id} — get single item
- [ ] PUT /items/{id} — update item
- [ ] DELETE /items/{id} — delete item
- [ ] All item routes require JWT authentication
- [ ] Users can only access their own items
- [ ] Pydantic models for input validation
- [ ] Proper error responses (400, 401, 404, 422)
- [ ] SQLite database with users and items tables
- [ ] Passwords hashed (use bcrypt or passlib)
- [ ] Auto-generated Swagger docs at /docs

## Deliverables

- FastAPI project with organized structure
- SQLite database (auto-created)
- README with setup and API documentation
