/*
LESSON 04 — Conditional Rendering
HARD P01 — Full Data Fetch States
============================================
CONCEPT: Real data fetching has four UI states — idle, loading, error, success. A chain of early returns, one per state, reads top-to-bottom like a flowchart.
PROBLEM: Build a `DataFetcher` with `state` ("idle" first). `fetchData` sets "loading", then a `setTimeout` (~1s) randomly resolves to "success" or "error". Render early returns: idle → Fetch Data button; loading → "Loading..."; error → red text + Retry button; success → "Data loaded successfully!".
TRY THIS: Render `<DataFetcher />`, click Fetch Data, retry on error.
EXPECTED OUTPUT: UI cycles idle → loading → success OR error, and Retry re-runs the cycle.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
