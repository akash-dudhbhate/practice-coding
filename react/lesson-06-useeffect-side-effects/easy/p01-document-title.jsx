/*
LESSON 06 — useEffect & Side Effects
EASY P01 — Document Title Updater
============================================
CONCEPT: useEffect runs AFTER render — the right place for side effects like touching document.title. The dep array [count] re-runs it only when count changes.
PROBLEM: Build a `DocTitleCounter` with `count` state. A `useEffect` sets `document.title = \`Count: ${count}\`` with `[count]` deps. Render a button that increments and shows the count.
TRY THIS: Render `<DocTitleCounter />` and click the button twice.
EXPECTED OUTPUT: The browser tab title updates to "Count: 2" on each click.
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
