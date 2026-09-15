# Lesson 13 — Debug Exercises

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
