/*
LESSON 19 — Testing React
HARD P03 — Test a Context-Powered ShoppingCart
============================================
CONCEPT: To test a context store, build a tiny `TestComponent` that consumes the hook and exposes actions as buttons plus state via `data-testid` spans — then drive everything with fireEvent and assert the rendered values.
PROBLEM: For `CartProvider`/`useCart` (import "../CartContext"), write a `TestComponent` exposing `addItem`/`removeItem`/`updateQty` buttons and `data-testid` spans for `count` and `total` (plus a "Cart is empty" message). Write FIVE tests via a `renderApp` helper wrapping it in `CartProvider`: starts empty; adding Apple+Banana shows both rows and count "2"; removing Apple returns to empty; `updateQty(1,3)` shows "Apple x3"; total shows "1.50" after Apple+Banana.
TRY THIS: Run the suite — every cart action and both derived values verified.
EXPECTED OUTPUT: 5 passing tests: add, remove, updateQty, total math, empty state.
CHECK: python3 check.py hard/p03
*/
// TODO: write your test from scratch
