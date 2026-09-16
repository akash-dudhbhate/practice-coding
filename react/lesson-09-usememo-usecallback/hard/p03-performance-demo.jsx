/*
LESSON 09 — useMemo & useCallback
HARD P03 — PerformanceDemo with Profiler
============================================
CONCEPT: You can A/B memoization at runtime: toggle a flag, switch between a useMemo'd value and a fresh computation, and wrap the output in <Profiler> to log real render timings.
PROBLEM: Build a `PerformanceDemo` with `memoized` and `count` state. `data = useMemo(() => 1000-element computation on count, [count])`; `compute = memoized ? data : fresh computation`. Define `onRender(id, phase, actualTime)` logging to console and wrap the preview `<p>` in `<Profiler id="list" onRender={onRender}>`. Add a Memoized checkbox and a Recompute button.
TRY THIS: Render `<PerformanceDemo />`, toggle memoized off/on, click Recompute.
EXPECTED OUTPUT: Console shows Profiler timings; memoized mode avoids the 1000-item recompute.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
