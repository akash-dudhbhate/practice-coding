/*
LESSON 02 — State & useState
HARD P03 — Accordion
============================================
CONCEPT: Store the open index — not a boolean per item — and only one section can be open. Clicking the open one sets the index back to null.
PROBLEM: Build an `Accordion` component taking a `sections` prop (array of `{ title, content }`). Keep `openIndex` state (start null). Each section renders a full-width title button; clicking sets `openIndex` to that index (or null if already open). Only the open section's content renders.
TRY THIS: Render `<Accordion sections={[{ title: "A", content: "aaa" }, { title: "B", content: "bbb" }]} />` and click "A", then "B".
EXPECTED OUTPUT: Clicking a title expands its content and collapses the previously open one.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
