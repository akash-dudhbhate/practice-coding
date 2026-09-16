/*
LESSON 13 — React Router
EASY P01 — Basic Routes with 404
============================================
CONCEPT: React Router swaps components based on the URL — no page reloads. `BrowserRouter` enables routing, `Routes`/`Route` map paths to elements, and `Link` navigates without a full refresh.
PROBLEM: Build an `App` wrapped in `BrowserRouter` with a `nav` of `Link`s to "/", "/about", "/contact" and a `Routes` block mapping each path to `Home`, `About`, `Contact` components (each renders an `<h1>`). Add a catch-all `<Route path="*">` rendering a `NotFound` component.
TRY THIS: Render `<App />`, click About, then visit a bogus URL like /nope.
EXPECTED OUTPUT: Headings swap on click; /nope shows "404 - Page Not Found".
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
