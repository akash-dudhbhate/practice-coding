/*
LESSON 17 — Zustand
MEDIUM P02 — Cart Store with Computed Total
============================================
CONCEPT: `create((set, get) => ...)` gives actions access to `get()` — and a getter like `get total() {...}` derives values from state at read time, so `total` is always in sync with `items`.
PROBLEM: Create `useCartStore` with `items: []`, `addItem(item)` (merge by id, bump `qty`), `removeItem(id)`, `updateQuantity(id, qty)`, `clearCart()`, and a `get total()` computing `reduce` over `price * qty`. Build `Cart` rendering an "Add Apple" button (`{id:1, name:"Apple", price:1}`), the items `<ul>` with per-item Remove, and `Total: $X.XX`.
TRY THIS: Render `<Cart />` and click Add Apple three times — one row shows "Apple x3".
EXPECTED OUTPUT: Items merge by id with qty; total stays correct; Remove deletes rows.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
