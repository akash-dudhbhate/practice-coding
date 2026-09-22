/*
LESSON 20 — React Performance
MEDIUM P02 — useDeferredValue Search
============================================
CONCEPT: `useDeferredValue(query)` returns a lagging copy of state — React updates the input URGENTLY and re-renders the expensive filtered list in the background when idle. `query !== deferredQuery` tells you a deferral is in flight.
PROBLEM: Build `DeferredSearch`: `query` state; `deferredQuery = useDeferredValue(query)`; `items` = memoized array of 10,000 strings; `filtered = useMemo(() => items.filter(i => i.includes(deferredQuery)), [items, deferredQuery])`; `isStale = query !== deferredQuery`. Render the input, a blue "Filtering..." when `isStale`, the result count, and the first 20 matches.
TRY THIS: Render `<DeferredSearch />` and type quickly into a 10k list — the input never stutters, results lag slightly behind.
EXPECTED OUTPUT: Instant keystrokes; "Filtering..." flashes while the deferred list catches up.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
