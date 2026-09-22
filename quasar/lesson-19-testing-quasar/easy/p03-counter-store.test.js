/**
 * LESSON 19 — Testing Quasar Apps
 * EASY P03 — Pinia Store Test
 * ============================================
 * CONCEPT: Stores are plain JS — no mounting needed. Call
 * setActivePinia(createPinia()) in beforeEach so every test gets a fresh
 * store, then call actions/getters directly.
 *
 * PROBLEM: Test an inline useCounterStore (state count, action
 * increment, getter double): initial count 0, increment raises it,
 * double returns count*2.
 *
 * TRY THIS: beforeEach(() => setActivePinia(createPinia()))
 * const store = useCounterStore(); store.increment();
 * expect(store.double).toBe(2)
 *
 * EXPECTED OUTPUT: Three passing its — initial state, action, getter.
 *
 * CHECK: python3 check.py easy/p03
 */
// TODO: write your store tests here
