/*
LESSON 02 — State & useState
MEDIUM P02 — Counter with Step Controls
============================================
CONCEPT: Functional updates `setCount(prev => prev + 1)` always compute from the latest state — the safe pattern when the new value depends on the old.
PROBLEM: Build a `Counter` component with `count` state and three buttons: "+1", "-1", and "Reset". Use functional updates (`prev => ...`) and never let count drop below 0 (`Math.max(0, prev - 1)`). Show the count in a `<p>`.
TRY THIS: Render `<Counter />`, press +1 twice, -1 five times.
EXPECTED OUTPUT: The count shows 2, then clamps at 0 — never negative.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
