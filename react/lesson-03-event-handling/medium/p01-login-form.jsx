/*
LESSON 03 — Event Handling
MEDIUM P01 — Login Form
============================================
CONCEPT: Forms reload the page by default — `e.preventDefault()` in `onSubmit` stops that so React keeps control.
PROBLEM: Build a `LoginForm` component with `email`, `password`, and `creds` state. A `<form onSubmit={handleSubmit}>` wraps two controlled inputs and a submit button; the handler calls `e.preventDefault()` then stores `{ email, password }` in `creds`, which renders in a `<p>` below.
TRY THIS: Render `<LoginForm />`, enter a@b.com / secret, press Login.
EXPECTED OUTPUT: After submit, "Email: a@b.com, Password: secret" appears (no page reload).
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
