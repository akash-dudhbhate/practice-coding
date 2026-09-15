# Lesson 13 — Intuition Checks

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
