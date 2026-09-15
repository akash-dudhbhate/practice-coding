# Social Dashboard (React + FastAPI) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
capstone-02-social-dashboard/
├── frontend/src/..., backend/main.py, backend/models.py, backend/auth.py
└── README.md
```

---

## Implementation Steps

### Step 1: Backend Setup

FastAPI + SQLAlchemy + PostgreSQL/SQLite. User, Post, Comment, Like models.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Auth Backend

JWT auth. Register, login, get current user. Password hashing. Rate limiting.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Posts API

CRUD for posts. Pagination. Like/unlike. Comments. Feed (following's posts).

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Frontend Setup

React + Router + Zustand. Axios instance with auth interceptor.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Auth Frontend

Login/register pages. Protected routes. Auth context/store. Token refresh.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Feed Page

Infinite scroll feed. Post cards with like, comment, share. Create post.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Profile Page

User info, posts grid, edit profile, follow/unfollow. Avatar upload.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Notifications

Real-time notifications (WebSocket or polling). Like/comment notifications.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Search

Search users and posts. Hashtag support. Trending posts.

**Checkpoint:** Step 9 is complete when the described functionality works.

### Step 10: Responsive

Mobile: bottom nav, single column. Desktop: sidebar + feed + suggestions.

**Checkpoint:** Step 10 is complete when the described functionality works.

### Step 11: Deploy

Backend: Railway/Render. Frontend: Vercel. Environment variables. CORS configured.

**Checkpoint:** Step 11 is complete when the described functionality works.

---

## Final Checklist

- [ ] FastAPI backend with auth
- [ ] Posts CRUD with likes + comments
- [ ] React frontend with auth
- [ ] Infinite scroll feed
- [ ] Profile pages with follow
- [ ] Real-time notifications
- [ ] Search + hashtags
- [ ] Responsive (mobile + desktop)
- [ ] Deployed (backend + frontend)
- [ ] CORS + environment variables

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
