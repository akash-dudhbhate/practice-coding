/*
LESSON 09 — useMemo & useCallback
MEDIUM P01 — SearchFilter with useMemo
============================================
CONCEPT: Filtering 100+ items on every keystroke is fine — but it should NOT re-run when unrelated state changes. useMemo with `[items, query]` deps guarantees that.
PROBLEM: Build a `SearchFilter` with an `items` useMemo (100 items), `query` and `unrelated` counter state. `filtered = useMemo(() => items.filter(... includes query ...), [items, query])`. Render search input, an "Unrelated" counter button, and the filtered `<ul>`.
TRY THIS: Render `<SearchFilter />`, type "1", then click the Unrelated button.
EXPECTED OUTPUT: Search narrows the list; clicking Unrelated re-renders without re-filtering.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
