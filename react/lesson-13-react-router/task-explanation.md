# Lesson 13 — React Router

## What you'll learn
- Client-side routing (BrowserRouter, Routes, Route)
- Link vs NavLink (active states)
- Dynamic routes and useParams
- useNavigate (programmatic navigation)
- Nested routes and Outlet
- URL search parameters (useSearchParams)
- Protected routes (auth checks)
- 404 (NotFound) routes
- useLocation (current URL info)

## Lesson

### Basic routing
```jsx
<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/users/:id" element={<User />} />
    <Route path="*" element={<NotFound />} />
  </Routes>
</BrowserRouter>
```

### Navigation
```jsx
<Link to="/about">About</Link>
const { id } = useParams();
const navigate = useNavigate();
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create an app with 3 routes: Home, About, Contact. Use `Link` for navigation. Include a 404 route for unknown paths.
2. `easy/p02-solve.jsx` — Create a navigation bar with `NavLink` that highlights the active page. Include 4 routes.
3. `easy/p03-solve.jsx` — Create a dynamic route `/user/:username` that displays the username from `useParams`. Add links to 3 different user profiles.

### Medium
4. `medium/p01-solve.jsx` — Create a login form that uses `useNavigate` to redirect to `/dashboard` after submit. Include a back button on the dashboard using `navigate(-1)`.
5. `medium/p02-solve.jsx` — Create a dashboard with nested routes: `/dashboard` (overview), `/dashboard/stats`, `/dashboard/settings`. Use `<Outlet>` for the shared layout (sidebar + content area).
6. `medium/p03-solve.jsx` — Create a product list with `useSearchParams` for pagination (`?page=2`) and sorting (`?sort=price`). Buttons update the URL params. Display current page and sort.

### Hard
7. `hard/p01-solve.jsx` — Build a blog app with routes: home (post list), `/post/:slug` (single post), `/category/:category` (filtered list), `/admin` (protected). Include a 404 page and protected route for admin.
8. `hard/p02-solve.jsx` — Build a multi-step wizard: `/wizard/step1`, `/wizard/step2`, `/wizard/step3`, `/wizard/review`. Each step saves data. Use `useLocation` state to pass data between steps. Can't skip to step3 without completing step1.
9. `hard/p03-solve.jsx` — Build a complete e-commerce routing structure: `/` (home), `/products` (list with filters), `/products/:id` (detail), `/cart`, `/checkout` (protected), `/account` (protected), `/account/orders`, `/account/settings`. Include nested routes for account.

### How to work
- Write your complete React solution (router, pages, components).
- Remove the TODO comment when done.
- Test by importing into a React app with react-router-dom installed.
