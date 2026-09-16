/*
LESSON 13 — React Router
MEDIUM P03 — useSearchParams for Pagination & Sorting
============================================
CONCEPT: `useSearchParams()` reads and writes the `?query=string` part of the URL — so filters/pagination live in the address bar and survive refresh and sharing.
PROBLEM: Build `ProductList` calling `useSearchParams()` for `[params, setParams]`. Read `page` via `params.get("page") || "1"` and `sort` via `params.get("sort") || "name"`. Render "Page: X, Sort: Y" plus four buttons: Next/Prev page and Sort-by-price / Sort-by-name, each calling `setParams({page, sort})`. `App` mounts it at `/` inside `BrowserRouter`.
TRY THIS: Render `<App />` and click "Next Page" then "Sort by Price".
EXPECTED OUTPUT: "Page: 2, Sort: price" and the URL reads `?page=2&sort=price`.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
