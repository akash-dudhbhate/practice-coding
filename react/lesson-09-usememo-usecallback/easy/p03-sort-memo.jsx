/*
LESSON 09 — useMemo & useCallback
EASY P03 — Memoized Sort
============================================
CONCEPT: Expensive transforms like sorting 1000 items belong in useMemo — with `[nums]` deps it re-sorts only when the array actually changes.
PROBLEM: Build a `SortDemo` with `nums` state (lazy init: 1000 random ints) and `text` state. `const sorted = useMemo(() => [...nums].sort((a,b) => a - b), [nums])`. Render the first 5 sorted values, a Regenerate button, and a text input.
TRY THIS: Render `<SortDemo />`, type in the input, then hit Regenerate.
EXPECTED OUTPUT: Typing is instant (no re-sort); Regenerate produces a new sorted preview.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
