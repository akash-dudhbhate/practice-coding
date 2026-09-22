/**
 * LESSON 07 — Pinia State Management
 * EASY P02 — Component Using the Counter Store
 * ============================================
 * CONCEPT: Inside setup, call the use*Store() function to get the store.
 * Destructure state/getters with storeToRefs() to keep reactivity; destructure
 * actions directly — they're just functions.
 *
 * PROBLEM: A component object (export default { setup() {...}, template })
 * using useCounterStore from './p01-counter-store.js' (or define/import an
 * equivalent store). Show count and double; Increment and Decrement q-btns.
 *
 * TRY THIS: const store = useCounterStore();
 * const { count, double } = storeToRefs(store);
 * const { increment, decrement } = store;
 * return { count, double, increment, decrement }
 *
 * EXPECTED OUTPUT: "Count: 0", "Double: 0" and two buttons that mutate them.
 *
 * CHECK: python3 check.py easy/p02
 */
// TODO: write your component here
