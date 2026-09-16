/*
LESSON 16 — React Query
HARD P01 — Debounced Search
============================================
CONCEPT: Querying on every keystroke spams the API. A `useDebounce` hook (setTimeout inside useEffect) delays the value 500ms; putting the DEBOUNCED term in the queryKey means the query only refires when typing pauses. `enabled: !!term` skips empty searches.
PROBLEM: Write `useDebounce(value, delay = 500)` returning a lagged value via `useState` + `useEffect`/`setTimeout`/`clearTimeout`. Build `SearchUsers`: `query` state, `debouncedQuery = useDebounce(query)`, and `useQuery` with `queryKey: ["search", debouncedQuery]`, a `?name_like=` fetch, and `enabled: !!debouncedQuery`. Render the input, "Searching..." on `isFetching`, "Type to search" when empty, "No results" on empty data, else the `<ul>` of names.
TRY THIS: Render `<SearchUsers />` and type "leanne" quickly — one request fires ~500ms after you stop.
EXPECTED OUTPUT: Single debounced fetch per pause; correct empty/loading/results states.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
