/**
 * LESSON 07 — Pinia State Management
 * MEDIUM P01 — Cart Store
 * ============================================
 * CONCEPT: Getters are computed() over store state; actions mutate it.
 * addItem should merge duplicates by incrementing quantity rather than
 * pushing a second row.
 *
 * PROBLEM: Export `useCartStore` (id 'cart') with `items` ref([]) of
 * { id, name, price, quantity }, getters `totalItems` (sum of quantities)
 * and `totalPrice` (sum of price*quantity), and actions `addItem`,
 * `removeItem(id)`, `clearCart`. Include a cart component (template in a
 * comment or object) listing items + totals.
 *
 * TRY THIS: const totalItems = computed(() => items.value.reduce((s, i) => s + i.quantity, 0));
 * addItem finds existing by product.id and bumps quantity, else pushes { ...product, quantity: 1 }
 *
 * EXPECTED OUTPUT: A store driving a cart list with live item count and
 * price totals, plus working add/remove/clear.
 *
 * CHECK: python3 check.py medium/p01
 */
// TODO: write your store here
