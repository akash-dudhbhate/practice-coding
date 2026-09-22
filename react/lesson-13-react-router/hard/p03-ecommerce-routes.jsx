/*
LESSON 13 — React Router
HARD P03 — E-Commerce Routing Structure
============================================
CONCEPT: This combines everything: static routes, a `/:id` detail route, protected-style routes, and a nested account section sharing a layout via `Outlet`.
PROBLEM: Build components: `Home`, `Products` (links to /products/1), `ProductDetail` (reads `id` via `useParams`), `Cart`, `Checkout`, `AccountLayout` (aside with account links + `<Outlet />` in main), `Orders`, `Settings`. `App` renders a nav (Home/Products/Cart/Account) and `Routes`: `/`, `/products`, `/products/:id`, `/cart`, `/checkout`, and `/account` nesting an `index` route (Orders) plus `settings`.
TRY THIS: Render `<App />`, visit /products/42, then /account/settings.
EXPECTED OUTPUT: "Product 42" from the param; account pages render inside the shared sidebar layout.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
