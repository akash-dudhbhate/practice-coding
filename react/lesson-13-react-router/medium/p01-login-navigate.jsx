/*
LESSON 13 — React Router
MEDIUM P01 — Programmatic Navigation with useNavigate
============================================
CONCEPT: `Link` navigates on click, but sometimes code must navigate — after a form submit, a timeout, an async call. `useNavigate()` returns a function; `navigate(-1)` goes back in history.
PROBLEM: Build a `Login` component: a form whose `onSubmit` calls `e.preventDefault()` then `navigate("/dashboard")`. Build `Dashboard` with an `<h1>` and a Back button calling `navigate(-1)`. `App` wires `BrowserRouter` + `Routes` with `/` → Login and `/dashboard` → Dashboard.
TRY THIS: Render `<App />`, submit the login form — you land on /dashboard — then click Back.
EXPECTED OUTPUT: Submitting navigates to the Dashboard heading; Back returns to the login form.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
