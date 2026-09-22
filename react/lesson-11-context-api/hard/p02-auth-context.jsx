/*
LESSON 11 — Context API
HARD P02 — Auth System with Context
============================================
CONCEPT: Auth is the classic context use case: the current user and the login/logout functions must be reachable from anywhere (nav bar, protected pages, forms) without threading props.
PROBLEM: Create `AuthContext` and a `useAuth()` hook that throws a clear error outside the provider. Build `AuthProvider({children})` holding `user` in `useState(null)` and providing `{user, login, logout, register}` — `login(email)` sets a user object, `logout()` clears it, `register(name, email)` sets a user. Build `LoginForm` (controlled email input + submit calling `login`) and `Dashboard` that renders `LoginForm` when there's no user, otherwise a welcome message with a Logout button. `App` wraps `Dashboard` in `AuthProvider`.
TRY THIS: Render `<App />`, type "alice@example.com", submit — the dashboard appears; click Logout to return to the form.
EXPECTED OUTPUT: Login form when logged out; "Welcome, alice" + Logout button when logged in.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
