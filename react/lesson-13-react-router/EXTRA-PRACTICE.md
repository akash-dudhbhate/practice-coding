# lesson-13-react-router — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: BrowserRouter vs HashRouter
What's the difference?
<details><summary>Answer</summary>
BrowserRouter — clean URLs (/about), needs server config. HashRouter — URLs with # (/#/about), works without server config. Use BrowserRouter for production.
</details>

## Check 02: Route parameters
```jsx
<Route path="/users/:id" element={<User />} />
// URL: /users/123
```
<details><summary>Answer</summary>
`:id` is a URL parameter. Access with `useParams()`: `const { id } = useParams();` → "123".
</details>

## Check 03: useNavigate
```jsx
const navigate = useNavigate();
navigate("/dashboard");
navigate(-1); // go back
```
<details><summary>Answer</summary>
Programmatic navigation. Replaces the old `useHistory`. Navigate to a path or relative number (1 forward, -1 back).
</details>

## Check 04: Nested routes
```jsx
<Route path="/dashboard" element={<Dashboard />}>
  <Route path="stats" element={<Stats />} />
</Route>
```
<details><summary>Answer</summary>
Nested route — `/dashboard/stats` renders Dashboard with Stats inside. Parent must have `<Outlet />` to render child.
</details>

## Check 05: Protected routes
```jsx
<Route path="/admin" element={isAdmin ? <Admin /> : <Navigate to="/login" />} />
```
<details><summary>Answer</summary>
Conditional rendering — if not admin, redirect to login. Common pattern for auth-protected pages.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Missing BrowserRouter
```jsx
function App() {
  return <Routes><Route path="/" element={<Home />} /></Routes>;
}
```
<details><summary>Answer</summary>
**Bug:** No `<BrowserRouter>` wrapping the routes. Router context is missing.
**Fix:** `return <BrowserRouter><Routes>...</Routes></BrowserRouter>;`.
</details>

## Debug 02 (Medium): Route Path Mismatch
```jsx
<Route path="users" element={<Users />} />
// URL: /user
```
<details><summary>Answer</summary>
**Bug:** Path is "users" (plural), URL is "user" (singular). No match.
**Fix:** Make them consistent.
</details>

## Debug 03 (Hard): Missing Link
```jsx
<a href="/about">About</a>
```
<details><summary>Answer</summary>
**Bug:** Regular `<a>` causes full page reload. Loses SPA behavior.
**Fix:** `<Link to="/about">About</Link>`.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual Navigation State
### Before
```jsx
const [page, setPage] = useState("home");
page === "about" && <About />
```
### After
```jsx
<Routes>
  <Route path="/about" element={<About />} />
</Routes>
```

## Refactor 02 (Medium): Hardcoded URLs
### Before
```jsx
navigate("/users/" + userId);
```
### After
```jsx
navigate(`/users/${userId}`);
// or better: named routes
```

## Refactor 03 (Hard): No Lazy Loading
### Before
```jsx
import Home from "./Home";
import About from "./About";
import Admin from "./Admin"; // all loaded upfront
```
### After
```jsx
const Home = lazy(() => import("./Home"));
const About = lazy(() => import("./About"));
const Admin = lazy(() => import("./Admin"));
<Suspense fallback={<Spinner />}><Routes>...</Routes></Suspense>
```

---

## Approach Comparison — different ways to solve it

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
