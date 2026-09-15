# CRUD API with Auth (FastAPI) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
medium-06-crud-api-auth/
├── main.py, models.py, schemas.py, database.py, auth.py, crud.py, dependencies.py
└── README.md
```

---

## Implementation Steps

### Step 1: Database Setup

SQLAlchemy + SQLite. User model, Item model. Relationship (user → items).

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Auth System

JWT tokens. register, login endpoints. Password hashing (bcrypt).

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Dependencies

get_current_user: decode JWT, fetch user. Optional vs required auth.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: User Endpoints

POST /register, POST /login, GET /me, PUT /me (update profile).

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Item CRUD

POST /items (auth required), GET /items (public), GET /items/{id}, PUT, DELETE (owner only).

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Validation

Pydantic schemas. Email validation, password strength, item fields.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Rate Limiting

SlowAPI or custom: limit requests per IP. Prevent abuse.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Testing

pytest: test auth flow, CRUD operations, unauthorized access, owner checks.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Documentation

OpenAPI docs. Security scheme (Bearer JWT). Examples in descriptions.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] JWT authentication
- [ ] Password hashing (bcrypt)
- [ ] Register + login endpoints
- [ ] User profile endpoints
- [ ] Item CRUD (owner-only edit/delete)
- [ ] Pydantic validation
- [ ] Rate limiting
- [ ] Tests with pytest
- [ ] OpenAPI docs with security

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
