/*
LESSON 08 — useRef & DOM Access
MEDIUM P02 — usePrevious Hook
============================================
CONCEPT: A ref + useEffect can remember the LAST render's value: the effect runs after render, so `ref.current` still holds the previous value during render.
PROBLEM: Build a `usePrevious(value)` hook: `const ref = useRef()`, `useEffect(() => { ref.current = value })`, return `ref.current`. Use it in a `PreviousDemo` component with a counter showing "Current: X, Previous: Y" and an Increment button.
TRY THIS: Render `<PreviousDemo />` and click Increment twice.
EXPECTED OUTPUT: Shows "Current: 2, Previous: 1" — always one step behind.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
