/**
 * LESSON 07 — Pinia State Management
 * EASY P01 — Counter Store
 * ============================================
 * CONCEPT: A Pinia setup store is a function passed to defineStore(). Inside,
 * refs are state, computeds are getters, functions are actions — return them
 * all to expose them.
 *
 * PROBLEM: Export `useCounterStore` (store id 'counter') with `count` ref(0),
 * `double` computed (count * 2), and `increment` / `decrement` actions.
 *
 * TRY THIS: export const useCounterStore = defineStore('counter', () => {
 *   const count = ref(0); const double = computed(() => count.value * 2); ...
 *   return { count, double, increment, decrement } })
 *
 * EXPECTED OUTPUT: An importable store whose count starts at 0 and whose
 * double getter tracks it.
 *
 * CHECK: python3 check.py easy/p01
 */
// TODO: write your store here
