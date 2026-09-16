/*
LESSON 17 — Zustand
MEDIUM P01 — Auth Store with Async Login
============================================
CONCEPT: Store actions can be async: `login` sets `loading: true`, awaits a fake API, then sets `user` or `error`. Components just read `{user, loading, error}` — no useEffect orchestration.
PROBLEM: Create `useAuthStore` with `user: null, loading: false, error: null`, an async `login(username, password)` (set loading, await a 500ms setTimeout promise, throw "Password too short" if password < 4 chars, set user `{name: username}` or catch → `error`), and `logout()`. Build `LoginForm` (controlled username/password, error paragraph, submit button disabled+labeled by `loading`), `Dashboard` (welcome + Logout), and `App` rendering Dashboard when `user` else LoginForm.
TRY THIS: Render `<App />`, enter user + a 3-char password — error shows; retry with 4+ chars — dashboard appears.
EXPECTED OUTPUT: Loading label during login, error on short password, welcome screen on success.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
