/*
LESSON 13 — React Router
EASY P02 — NavLink with Active Highlight
============================================
CONCEPT: `NavLink` is a `Link` that knows whether its route is active. Its `style` (or `className`) prop accepts a function receiving `{isActive}` so the current page's link can look different.
PROBLEM: Build an `App` in `BrowserRouter` with 4 routes — Home, About, Services, Contact — each a simple `<h1>` component. The nav uses 4 `NavLink`s whose `style` is a function `({isActive}) => ({color: isActive ? "red" : "blue"})`.
TRY THIS: Render `<App />` and click Services — that link turns red while the others stay blue.
EXPECTED OUTPUT: Active link renders red, inactive links blue; headings swap per route.
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
