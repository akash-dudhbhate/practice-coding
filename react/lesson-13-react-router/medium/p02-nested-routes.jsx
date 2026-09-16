/*
LESSON 13 — React Router
MEDIUM P02 — Nested Routes with Outlet
============================================
CONCEPT: Child `<Route>`s nested inside a parent route render into the parent's `<Outlet />` — perfect for shared layouts like a sidebar that stays while the content swaps.
PROBLEM: Build `DashboardLayout` rendering an `aside` with Links to /dashboard, /dashboard/stats, /dashboard/settings and a `main` containing `<Outlet />`. Create `Overview`, `Stats`, `Settings` (each an `<h2>`). In `App`, nest three child routes under `<Route path="/dashboard" element={<DashboardLayout />}>`: an `index` route → Overview, plus "stats" and "settings".
TRY THIS: Render `<App />`, visit /dashboard/stats — sidebar stays put, only the content changes.
EXPECTED OUTPUT: Sidebar links always visible; /dashboard shows Overview, /stats shows Stats, /settings shows Settings.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
