/*
LESSON 04 — Conditional Rendering
HARD P02 — Object Map Status Display
============================================
CONCEPT: Nested ternaries get unreadable fast. An object that maps status → JSX (`content[status]`) is the cleaner lookup-table pattern.
PROBLEM: Build a `StatusDisplay` with `status` state. Define a `content` object mapping "loading"/"success"/"error"/"empty" to different `<p>` JSX, render `{content[status]}`, and add four buttons that set each status.
TRY THIS: Render `<StatusDisplay />` and click each of the four buttons.
EXPECTED OUTPUT: The displayed paragraph swaps to match whichever status button was clicked.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
