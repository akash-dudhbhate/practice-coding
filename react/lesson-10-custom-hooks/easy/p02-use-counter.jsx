/*
LESSON 10 — Custom Hooks
EASY P02 — useCounter Hook
============================================
CONCEPT: Packaging count + increment/decrement/reset into useCounter means any component gets a full counter API in one line.
PROBLEM: Build `useCounter(initial)` returning `{ count, increment, decrement, reset }` using useCallback + functional updates. Then a `CounterDemo` with +1/-1/Reset buttons and the count. Export `CounterDemo` default.
TRY THIS: Render `<CounterDemo />`, press +1 twice, -1 once, Reset.
EXPECTED OUTPUT: Count shows 1 after the clicks, back to 0 on Reset.
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
