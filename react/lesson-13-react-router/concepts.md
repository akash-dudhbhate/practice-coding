# Lesson 13 — Concepts Explained (React Router)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Client-Side Routing

**What:** React Router enables navigation between pages WITHOUT full page reloads. The URL changes but only the relevant components re-render.

```jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function App() {
    return (
        <BrowserRouter>
            <nav>
                <Link to="/">Home</Link>
                <Link to="/about">About</Link>
                <Link to="/contact">Contact</Link>
            </nav>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/contact" element={<Contact />} />
            </Routes>
        </BrowserRouter>
    );
}
```

**Why it exists:** Without client-side routing, every link click reloads the entire page → slow, loses state, bad UX. React Router changes the URL and renders only the new component → fast, seamless, app-like experience (SPA).

**Where it's used:** Every multi-page React app — dashboards, e-commerce, blogs, admin panels.

**What goes wrong without it:**
- Forgetting `<BrowserRouter>` → router components don't work → errors.
- No `<Route>` for a path → blank page when navigating to that URL.
- Using `<a href="/about">` instead of `<Link to="/about">` → full page reload → defeats the purpose of SPA.

---

## Link vs NavLink

**What:** `Link` navigates to a route. `NavLink` does the same but adds an "active" class when the route matches.

```jsx
import { Link, NavLink } from 'react-router-dom';

// Link — simple navigation
<Link to="/about">About</Link>

// NavLink — adds "active" class when current URL matches
<NavLink to="/about" className="nav-link">
    About
</NavLink>
// When on /about: <a class="nav-link active">About</a>

// NavLink with custom active class function
<NavLink to="/about" className={({ isActive }) => isActive ? "active-link" : "link"}>
    About
</NavLink>

// NavLink with exact matching
<NavLink to="/about" end>About</NavLink>
// "end" prevents matching /about/team when on /about
```

**Why it exists:** Without `NavLink`, you'd manually check the current URL and add the active class → verbose. `NavLink` handles it automatically → clean navigation highlighting.

**Where it's used:** Navigation bars, tabs, breadcrumbs — any link that should show which page is active.

**What goes wrong without it:**
- `NavLink` without `end` → `/about` is active when on `/about/team` too (partial match). Use `end` for exact matching.
- `Link` to an external URL: `<Link to="https://google.com">` → treated as internal route → 404. Use `<a href>` for external links.
- `Link to="/about"` vs `Link to="about"` → leading `/` is absolute, no `/` is relative. Usually you want absolute.

---

## Dynamic Routes and useParams

**What:** Routes with variable segments (e.g., `/users/:id`) and accessing the parameter.

```jsx
// Route with dynamic parameter
<Route path="/users/:id" element={<UserProfile />} />

// Access the parameter in the component
import { useParams } from 'react-router-dom';

function UserProfile() {
    const { id } = useParams();  // gets :id from the URL
    return <h1>User ID: {id}</h1>;
}

// URL: /users/123 → id = "123"
// URL: /users/akash → id = "akash"
```

**Why it exists:** Without dynamic routes, you'd need a separate route for each user → impossible for thousands of users. Dynamic routes use a pattern → one route handles all users.

**Where it's used:** Profile pages, product pages, blog posts, any page that displays data for a specific entity.

**What goes wrong without it:**
- `useParams()` returns strings, not numbers. `id` from `/users/123` is `"123"` → convert: `Number(id)`.
- Multiple params: `/users/:userId/posts/:postId` → `useParams()` returns `{ userId, postId }`.
- Optional params: React Router doesn't support `?` optional params. Use separate routes or query params.

---

## useNavigate (Programmatic Navigation)

**What:** Navigate to a route from JavaScript code (not a link click).

```jsx
import { useNavigate } from 'react-router-dom';

function LoginForm() {
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        // ... authenticate ...
        navigate('/dashboard');          // go to dashboard
        navigate('/dashboard', { replace: true });  // replace (no back button)
        navigate(-1);                    // go back (like browser back)
        navigate(1);                     // go forward
    };

    return <form onSubmit={handleSubmit}>...</form>;
}
```

**Why it exists:** Without `useNavigate`, you can't redirect after an action (login, form submit, delete). `Link` only works for clicks. `useNavigate` works from any code → redirects after async operations.

**Where it's used:** Post-login redirect, after form submission, after delete → go back to list, conditional redirects.

**What goes wrong without it:**
- `navigate('/page')` pushes to history → back button goes to previous page. `navigate('/page', { replace: true })` → replaces → back button skips it. Use `replace` for redirects after login (don't want back to login page).
- `useNavigate` outside a `<BrowserRouter>` → error. Must be inside the router.
- Navigating during render → error. Navigate in event handlers or effects, not during render.

---

## Nested Routes and Outlet

**What:** Routes within routes — a parent route renders an `<Outlet>` for child routes.

```jsx
// Route configuration with nested routes
<Routes>
    <Route path="/dashboard" element={<DashboardLayout />}>
        <Route index element={<DashboardHome />} />        {/* /dashboard */}
        <Route path="stats" element={<Stats />} />          {/* /dashboard/stats */}
        <Route path="settings" element={<Settings />} />    {/* /dashboard/settings */}
    </Route>
</Routes>

// DashboardLayout renders children via Outlet
function DashboardLayout() {
    return (
        <div className="dashboard">
            <Sidebar />
            <main>
                <Outlet />  {/* child route renders here */}
            </main>
        </div>
    );
}
```

**Why it exists:** Without nested routes, you'd repeat the layout (sidebar, header) in every page → duplication. Nested routes share the parent layout → child routes render in the `<Outlet>` → DRY.

**Where it's used:** Dashboards with sidebar, admin panels, pages with persistent headers/footers, tabbed interfaces.

**What goes wrong without it:**
- Forgetting `<Outlet />` in the parent → child routes don't render → blank area.
- `index` route → renders when the parent path matches exactly (no child path). Without it → blank page at `/dashboard`.
- Child path: `path="stats"` (no leading `/`) → relative to parent. `path="/stats"` → absolute → breaks nesting.

---

## URL Search Parameters (useSearchParams)

**What:** Read and write URL query parameters (`?page=2&sort=name`).

```jsx
import { useSearchParams } from 'react-router-dom';

function ProductList() {
    const [searchParams, setSearchParams] = useSearchParams();
    const page = searchParams.get('page') || '1';
    const sort = searchParams.get('sort') || 'name';

    const handleSort = (newSort) => {
        setSearchParams({ page, sort: newSort });
        // URL becomes: /products?page=1&sort=price
    };

    return (
        <>
            <button onClick={() => handleSort('price')}>Sort by Price</button>
            <p>Page: {page}, Sort: {sort}</p>
        </>
    );
}
```

**Why it exists:** Without URL params, filter/sort state is in component state → lost on page refresh, not shareable. URL params persist → shareable links, bookmarkable, back button works.

**Where it's used:** Pagination, search filters, sort options, any state that should be in the URL.

**What goes wrong without it:**
- `searchParams.get('page')` returns a string or null. Convert: `Number(searchParams.get('page')) || 1`.
- `setSearchParams({ page, sort })` → replaces ALL params. To update one: `setSearchParams(prev => { prev.set('sort', 'price'); return prev; })`.
- Too many params → ugly URLs. Use them for important state (page, sort, filter), not everything.

---

## Protected Routes

**What:** Routes that require authentication — redirect to login if not authenticated.

```jsx
function ProtectedRoute({ children }) {
    const { user } = useAuth();  // your auth context/hook

    if (!user) {
        return <Navigate to="/login" replace />;
    }

    return children;
}

// Usage in routes
<Routes>
    <Route path="/login" element={<Login />} />
    <Route path="/dashboard" element={
        <ProtectedRoute>
            <Dashboard />
        </ProtectedRoute>
    } />
</Routes>
```

**Why it exists:** Without protected routes, anyone can access `/dashboard` by typing the URL → security issue. Protected routes check auth → redirect to login if not authenticated.

**Where it's used:** Any authenticated page — dashboard, settings, admin panel, user profile.

**What goes wrong without it:**
- `Navigate` without `replace` → back button goes back to the protected route → redirect loop. Always use `replace`.
- Checking auth in each component → repetitive. Use a wrapper component (`ProtectedRoute`).
- Client-side auth check is NOT security — the server must verify auth for API calls. Client-side routing is UX, not security.

---

## 404 (NotFound) Route

**What:** A catch-all route for unmatched URLs.

```jsx
<Routes>
    <Route path="/" element={<Home />} />
    <Route path="/about" element={<About />} />
    {/* ... other routes ... */}
    <Route path="*" element={<NotFound />} />
</Routes>

function NotFound() {
    return (
        <div>
            <h1>404 - Page Not Found</h1>
            <Link to="/">Go Home</Link>
        </div>
    );
}
```

**Why it exists:** Without a 404 route, unmatched URLs show a blank page → confusing. A 404 page tells the user the page doesn't exist and provides navigation.

**Where it's used:** Every React Router app — always have a catch-all route.

**What goes wrong without it:**
- `path="*"` must be the LAST route → routes are matched in order. If `*` is first → everything matches it → other routes never render.
- Forgetting `*` → blank page on unknown URLs → bad UX.
- Nested 404: put `*` inside a nested route → 404 for unknown sub-paths of the parent.

---

## useLocation

**What:** Access the current location object (pathname, search, hash, state).

```jsx
import { useLocation } from 'react-router-dom';

function CurrentPage() {
    const location = useLocation();
    console.log(location.pathname);  // "/about"
    console.log(location.search);    // "?page=2&sort=name"
    console.log(location.hash);      // "#section1"
    console.log(location.state);     // state passed via navigate

    return <p>You are on: {location.pathname}</p>;
}

// Passing state with navigate
navigate('/dashboard', { state: { fromLogin: true } });
// In Dashboard: location.state.fromLogin → true
```

**Why it exists:** Without `useLocation`, you can't know the current URL or pass data between routes (without URL params). Useful for analytics, breadcrumbs, conditional rendering based on path.

**Where it's used:** Breadcrumbs, analytics tracking, conditional rendering, reading navigation state.

**What goes wrong without it:**
- `location.state` is `null` on direct visits (no navigate). Always check: `if (location.state?.fromLogin)`.
- `location.search` is the raw string (`"?page=2"`). Use `useSearchParams` or `URLSearchParams` to parse it.
- `useLocation` triggers re-render on every navigation → fine, but be aware if using it in a hot path.
