# Lesson 13 — Common Mistakes

## Mistake 01: Using <a> instead of <Link>
```jsx
// WRONG — full page reload
<a href="/about">About</a>
// CORRECT — SPA navigation
<Link to="/about">About</Link>
```

## Mistake 02: Missing BrowserRouter
```jsx
// WRONG — no router context
<Routes><Route path="/" element={<Home />} /></Routes>
// CORRECT
<BrowserRouter><Routes>...</Routes></BrowserRouter>
```

## Mistake 03: Not using useParams
```jsx
// WRONG — can't access URL params without the hook
const id = window.location.pathname.split("/")[2];
// CORRECT
const { id } = useParams();
```

## Mistake 04: Hardcoded redirects
```jsx
// WRONG — full reload
window.location.href = "/login";
// CORRECT — SPA navigation
navigate("/login");
```

## Mistake 05: Missing Outlet for nested routes
```jsx
// WRONG — child routes don't render
function Dashboard() { return <div>Dashboard</div>; }
// CORRECT
function Dashboard() { return <div><Outlet /></div>; }
```
