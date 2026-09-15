# FastAPI REST API — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-12-fastapi-rest/
├── main.py, models.py, database.py, schemas.py, crud.py
└── README.md
```

---

## Implementation Steps

### Step 1: Setup

pip install fastapi uvicorn. Create main.py with FastAPI app.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Database

SQLite with SQLAlchemy. Create engine, session, Base. models.py: Item model.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Schemas

Pydantic models: ItemCreate, ItemResponse. Validation rules.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: CRUD

crud.py: get_items, get_item, create_item, update_item, delete_item.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Routes

GET /items, GET /items/{id}, POST /items, PUT /items/{id}, DELETE /items/{id}.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Error Handling

404 for missing items. 422 for validation errors. HTTPException.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Documentation

Auto-docs at /docs. Add descriptions, tags, response models.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Testing

pytest with TestClient. Test all endpoints. Test error cases.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: CORS

Add CORS middleware for frontend integration.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] SQLite database with SQLAlchemy
- [ ] Pydantic schemas with validation
- [ ] Full CRUD endpoints
- [ ] Proper HTTP status codes
- [ ] Error handling (404, 422)
- [ ] Auto-docs at /docs
- [ ] Tests with pytest
- [ ] CORS enabled

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
