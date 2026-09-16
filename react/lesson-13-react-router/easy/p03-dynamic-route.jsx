/*
LESSON 13 — React Router
EASY P03 — Dynamic Route with useParams
============================================
CONCEPT: A `:param` segment in a path matches anything and exposes it via the `useParams()` hook — one route definition serves unlimited URLs like /user/alice, /user/bob…
PROBLEM: Build a `UserProfile` component that calls `useParams()` to get `username` and renders `Profile: {username}` in an `<h1>`. `App` wraps a `BrowserRouter` with a nav of 3 `Link`s (/user/alice, /user/bob, /user/charlie) and one `<Route path="/user/:username" element={<UserProfile />}>`.
TRY THIS: Render `<App />` and click each user link.
EXPECTED OUTPUT: "Profile: alice" / "Profile: bob" / "Profile: charlie" — same component, different param.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
