/*
LESSON 09 — useMemo & useCallback
HARD P01 — DataTable with useMemo
============================================
CONCEPT: Chain derived work inside ONE useMemo — filter then sort then slice — so a 1000-row table only reprocesses when search or sortKey actually changes.
PROBLEM: Build a `DataTable` with `rows` (lazy 1000-row init: id/name/age), `search`, `sortKey`, and a `renderCount` state + Re-render button to prove memoization. `processed = useMemo(...)` filters by name, sorts a copy by sortKey, slices to 20. Render the counter, search input, two sort buttons, and a `<table>` of rows.
TRY THIS: Render `<DataTable />`, click Re-render, then sort by age and search "5".
EXPECTED OUTPUT: Re-render alone doesn't reprocess; sort/search change the visible 20 rows.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
