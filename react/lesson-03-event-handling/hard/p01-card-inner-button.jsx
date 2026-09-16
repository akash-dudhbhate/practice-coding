/*
LESSON 03 — Event Handling
HARD P01 — Clickable Card with Inner Button
============================================
CONCEPT: Clicks bubble up the DOM — a button inside a clickable card triggers BOTH handlers. `e.stopPropagation()` stops the bubble.
PROBLEM: Build a `CardWithButton` component with a `log` array state. An outer div's `onClick` appends "Card clicked"; an inner "Details" button calls `e.stopPropagation()` then appends "Details". Render the log joined below.
TRY THIS: Render `<CardWithButton />`, click the card, then click Details.
EXPECTED OUTPUT: Card click logs "Card clicked"; Details logs only "Details" — not both.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
