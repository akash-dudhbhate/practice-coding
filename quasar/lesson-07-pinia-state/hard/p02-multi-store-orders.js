/**
 * LESSON 07 — Pinia State Management
 * HARD P02 — Multi-Store App (User + Cart + Order)
 * ============================================
 * CONCEPT: Separate stores stay decoupled — the orchestration (checkout)
 * happens in the component, which calls one store's action with data from
 * the others.
 *
 * PROBLEM: Export `useUserStore` (user, login, logout), `useCartStore`
 * (items, totalItems, totalPrice, addItem, removeItem, clearCart), and
 * `useOrderStore` (orders, createOrder(cartItems, user) — stamps userId/
 * userName/total/date). Include a checkout component (template in comment
 * or object) wiring all three: create order from cart, then clear cart.
 *
 * TRY THIS: function checkout() { createOrder(items.value, user.value); clearCart() }
 * Order shape: { id: Date.now(), items: [...cartItems], userId, userName, total, date }
 *
 * EXPECTED OUTPUT: Add items → checkout moves them into an order row showing
 * id, buyer name, and total; cart empties.
 *
 * CHECK: python3 check.py hard/p02
 */
// TODO: write your stores here
