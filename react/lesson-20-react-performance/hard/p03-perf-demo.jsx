/*
LESSON 20 — React Performance
HARD P03 — Performance Comparison Demo (Profiler)
============================================
CONCEPT: The `Profiler` component's `onRender` callback fires per commit with timing info — wrap sections in it to COUNT renders. Combined with a memoized vs. plain item pair, you can SEE the optimization delta live.
PROBLEM: Build `MemoItem` (memo + console.log) and `NonMemoItem` (plain + console.log). `PerformanceDemo` holds `optimized` (checkbox picking which Item renders), `count`, `renderTimes` ({largeList, expensiveCalc, frequentUpdates} counters via `onRender`), and `useTransition`'s `isPending`. Memoize `largeData` (1000 items) and an `expensiveResult` (100k-iteration Math.sqrt loop). Wrap THREE `<Profiler>` sections: the 20-item list, the calc result, and a counter — each displaying its live render count.
TRY THIS: Render `<PerformanceDemo />`, click Increment with optimized ON vs OFF — the largeList render count stays flat when memoized.
EXPECTED OUTPUT: Toggle flips memoized↔plain items; Profiler counters prove fewer re-renders when optimized.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
