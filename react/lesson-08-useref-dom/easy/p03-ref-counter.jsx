/*
LESSON 08 — useRef & DOM Access
EASY P03 — Ref Click Counter
============================================
CONCEPT: Updating `ref.current` does NOT re-render — perfect demonstration of ref vs state: the count changes, the UI doesn't.
PROBLEM: Build a `RefCounter` with `countRef = useRef(0)`. The button's onClick does `countRef.current++` and `console.log`s it; render `countRef.current` in a `<p>` to show it stays stale on screen.
TRY THIS: Render `<RefCounter />` and click 3 times.
EXPECTED OUTPUT: Console logs 1, 2, 3 — but the paragraph still shows 0.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
