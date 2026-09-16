/*
LESSON 17 — Zustand
EASY P01 — Counter Store
============================================
CONCEPT: Zustand's `create()` builds a global store hook — no Provider, no Context. Call the hook anywhere to read state or grab actions; `set` merges partial updates.
PROBLEM: Create `useCounterStore = create((set) => ({...}))` with `count: 0` and actions `increment`, `decrement`, `reset` (each calling `set`). Build `Counter` destructuring all four from the store: a `<p>Count: {count}</p>` and three buttons wired to the actions.
TRY THIS: Render `<Counter />` in two places — both instances share the same count (global state!).
EXPECTED OUTPUT: "Count: 0" with +1 / -1 / Reset buttons working globally.
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
