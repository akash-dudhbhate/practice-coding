/*
LESSON 09 — useMemo & useCallback
EASY P02 — Memo Child + useCallback
============================================
CONCEPT: useCallback caches a FUNCTION. Paired with React.memo on the child, the child's props stay identical so it skips re-rendering.
PROBLEM: Build `Child = memo(({ onClick }) => ...)` logging "Child rendered" per render, then a `Parent` with `count` state and `handleClick = useCallback(() => console.log("Clicked"), [])`. Render count, an Increment button, and `<Child onClick={handleClick} />`. Export `Parent` default.
TRY THIS: Render `<Parent />` and click Increment twice.
EXPECTED OUTPUT: Count goes 1, 2 — but "Child rendered" logs only once.
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
