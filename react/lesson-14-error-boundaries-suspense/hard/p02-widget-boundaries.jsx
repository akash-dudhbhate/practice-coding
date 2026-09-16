/*
LESSON 14 — Error Boundaries & Suspense
HARD P02 — Dashboard with Per-Widget Error Boundaries
============================================
CONCEPT: Error boundaries isolate failures — wrap each widget separately so one crash doesn't take down the whole dashboard. This is fault isolation, like circuit breakers for UI.
PROBLEM: Write `ErrorBoundary` (hasError state + `reset`). Build `StatsWidget` and `ChartWidget` (render normally) plus `BuggyWidget` that throws. `Dashboard` lays all three out in a flex row, EACH inside its own `<ErrorBoundary>` whose fallback shows "Widget crashed" with a Retry button.
TRY THIS: Render `<Dashboard />` — Stats and Chart render fine while BuggyWidget shows only its own fallback.
EXPECTED OUTPUT: Two healthy widgets + one "Widget crashed" fallback with Retry; the page stays alive.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
