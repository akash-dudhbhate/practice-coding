/*
LESSON 02 — State & useState
HARD P01 — Shopping Cart
============================================
CONCEPT: Real apps keep arrays of objects in state. Every update (add, change quantity, remove) builds a NEW array with map/filter/spread so React sees the change.
PROBLEM: Build a `ShoppingCart` component. Keep a `products` constant (id/name/price) and `cart` state. Implement `addToCart`, `updateQty(id, delta)` (min qty 1), `removeFromCart`, and a `total` computed with `.reduce()`. Render product buttons, cart lines with +/-/Remove, and the total.
TRY THIS: Render `<ShoppingCart />`, add Apple twice and Banana once, press + on Apple.
EXPECTED OUTPUT: Cart lines show name, price, qty; "Total: $X.XX" updates on every change.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
