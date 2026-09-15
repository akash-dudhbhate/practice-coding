# Lesson 06 — Approach Comparison

## Problem: Route Configuration

### Approach 1: Flat routes
```javascript
[
  { path: "/", component: Home },
  { path: "/about", component: About },
  { path: "/admin", component: Admin }
]
```

### Approach 2: Nested with layouts
```javascript
[
  { path: "/", component: MainLayout, children: [
    { path: "", component: Home },
    { path: "about", component: About }
  ]},
  { path: "/admin", component: AdminLayout, children: [...] }
]
```

**Winner:** Approach 2 — layouts per section, cleaner.

---

## Problem: Protected Routes

### Approach 1: Per-route guard
```javascript
{ path: "/admin", beforeEnter: requireAuth }
```

### Approach 2: Global guard
```javascript
router.beforeEach((to) => {
  if (to.meta.requiresAuth) return checkAuth();
});
```

**Winner:** Approach 2 — centralized, consistent.
