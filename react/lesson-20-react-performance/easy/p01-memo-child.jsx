/*
LESSON 20 — React Performance
EASY P01 — React.memo Skips Child Re-Renders
============================================
CONCEPT: When a parent re-renders, ALL children re-render by default — even with unchanged props. `memo(Component)` skips the re-render when props are shallow-equal.
PROBLEM: Create `const Child = memo(({label}) => { console.log("Child rendered"); return <div>{label}</div>; })`. Build `Parent` with `count` state, an Increment button, and `<Child label="Static child" />`.
TRY THIS: Render `<Parent />`, click Increment several times, watch the console — "Child rendered" logs ONCE, not per click.
EXPECTED OUTPUT: Count updates; child never re-renders because `label` never changes.
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
