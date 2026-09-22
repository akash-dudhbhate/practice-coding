/*
LESSON 20 — React Performance
EASY P03 — useCallback + memo (Stable Props)
============================================
CONCEPT: `memo` fails silently when a prop is a NEW function every render — `onClick={() => ...}` breaks the shallow-compare. `useCallback(fn, [])` returns the SAME function identity, restoring memo's benefit.
PROBLEM: Create `const Child = memo(({onClick}) => { console.log("Child rendered"); return <button onClick={onClick}>Click me</button>; })`. Build `Parent` with `count` and `text` states, `handleClick = useCallback(() => console.log("Clicked"), [])`, an Increment button, a text input, and `<Child onClick={handleClick} />`.
TRY THIS: Render `<Parent />`, increment and type — "Child rendered" logs only once. Then remove useCallback and watch it log every keystroke.
EXPECTED OUTPUT: Child renders once; unrelated state changes don't touch it.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
