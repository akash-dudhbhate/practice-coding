# Task Management API (FastAPI) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
capstone-03-task-api/
├── main.py, models.py, schemas.py, database.py, auth.py, tasks.py, projects.py, websockets.py, tests/
└── README.md
```

---

## Implementation Steps

### Step 1: Database Design

Users, Projects, Tasks, Comments, Tags. Relationships. Migrations with Alembic.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Auth System

JWT + refresh tokens. Role-based access (admin, member). OAuth2 password flow.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Project Endpoints

CRUD projects. Members. Roles. Invite by email. Leave project.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Task Endpoints

CRUD tasks. Assign to user. Status (todo/in-progress/done). Priority. Due date.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Comments + Tags

Comments on tasks. Tags for categorization. Filter by tag. @mentions.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: WebSocket

Real-time task updates. Notify on assign, status change, comment. Connected clients.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: File Uploads

Attach files to tasks. Upload to S3 or local. Download endpoint.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Search + Filter

Search tasks by name/description. Filter by status, assignee, priority, due date.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Pagination + Sorting

Cursor or offset pagination. Sort by any field. Include total count.

**Checkpoint:** Step 9 is complete when the described functionality works.

### Step 10: Testing

pytest: unit tests, integration tests, auth tests, WebSocket tests. 80%+ coverage.

**Checkpoint:** Step 10 is complete when the described functionality works.

### Step 11: Documentation

OpenAPI with examples. WebSocket docs. Postman collection. README with setup.

**Checkpoint:** Step 11 is complete when the described functionality works.

### Step 12: Deploy

Docker + docker-compose. PostgreSQL. Gunicorn + uvicorn workers. CI/CD pipeline.

**Checkpoint:** Step 12 is complete when the described functionality works.

---

## Final Checklist

- [ ] Database with 5+ models and relationships
- [ ] JWT auth with refresh tokens
- [ ] Role-based access control
- [ ] Project CRUD with members
- [ ] Task CRUD with assign/status/priority
- [ ] Comments and tags
- [ ] WebSocket real-time updates
- [ ] File uploads
- [ ] Search + filter + pagination
- [ ] Tests with 80%+ coverage
- [ ] Docker deployment
- [ ] CI/CD pipeline

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
