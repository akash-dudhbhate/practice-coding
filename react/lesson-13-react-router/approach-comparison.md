# Lesson 13 — Approach Comparison

## Problem: Navigation

### Approach 1: <a> tag
```jsx
<a href="/about">About</a>
```
**Cons:** Full page reload, loses SPA state.

### Approach 2: <Link>
```jsx
<Link to="/about">About</Link>
```

**Winner:** Approach 2 — SPA navigation, no reload.

---

## Problem: Protected Route

### Approach 1: Inline conditional
```jsx
<Route path="/admin" element={isAdmin ? <Admin /> : <Navigate to="/login" />} />
```

### Approach 2: Wrapper component
```jsx
<Route path="/admin" element={<Protected><Admin /></Protected>} />
```

**Winner:** Approach 2 — reusable for multiple protected routes.
