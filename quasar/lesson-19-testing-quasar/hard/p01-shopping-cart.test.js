/**
 * LESSON 19 — Testing Quasar Apps
 * HARD P01 — ShoppingCart Store + Component Tests
 * ============================================
 * CONCEPT: Test store and component in one suite: a fresh Pinia per test,
 * drive the store directly for logic its, then mount the component and
 * assert the DOM reflects store state (count/total/empty).
 *
 * PROBLEM: Given an inline cart store (addItem merging quantities,
 * removeItem, updateQuantity, total/count/isEmpty getters) and a
 * ShoppingCart component bound to it: test empty state, adding,
 * quantity merging, removing, updating quantity, total math, and that
 * the component shows count/total and removes items on click.
 *
 * TRY THIS: store.addItem({ id: 1, name: 'Apple', price: 2 })
 * expect(store.total).toBe(9) // 3*2 + 1*3
 *
 * EXPECTED OUTPUT: ~8 its split into 'Store' and 'Component' describes,
 * all passing.
 *
 * CHECK: python3 check.py hard/p01
 */
// TODO: write your ShoppingCart tests here
