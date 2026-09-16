/*
LESSON 10 — Custom Hooks
EASY P01 — useToggle Hook
============================================
CONCEPT: A custom hook is just a function starting with `use` that calls other hooks — it packages stateful logic so any component can reuse it.
PROBLEM: Build `useToggle(initial)` returning `{ value, toggle, setTrue, setFalse }` (wrap the callbacks in useCallback). Then a `ToggleDemo` component using it to Show/Hide a paragraph. Export `ToggleDemo` default.
TRY THIS: Render `<ToggleDemo />` and click the button.
EXPECTED OUTPUT: "Toggle content visible!" appears and disappears on each click.
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
