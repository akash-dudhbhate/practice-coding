/*
LESSON 08 — useRef & DOM Access
EASY P01 — Auto-Focus Input
============================================
CONCEPT: useRef holds a DOM node without causing re-renders. Attach it with `ref={inputRef}`, then use `.current` inside useEffect once mounted.
PROBLEM: Build an `AutoFocus` component. `const inputRef = useRef(null)`; a `[]`-deps `useEffect` calls `inputRef.current.focus()`. Render `<input ref={inputRef} ...>`.
TRY THIS: Render `<AutoFocus />` and start typing without clicking.
EXPECTED OUTPUT: The input already has focus when the page loads.
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
