/*
LESSON 10 — Custom Hooks
MEDIUM P03 — useDebounce Hook
============================================
CONCEPT: useDebounce(value, delay) returns a value that only updates after `delay`ms of quiet — then a second effect can safely fetch on the debounced value.
PROBLEM: Build `useDebounce(value, delay=500)`: `debounced` state + `[value, delay]` effect with setTimeout/clearTimeout. Then `DebounceSearch` keeps `query`/`results` state, debounces query, and a `[debouncedQuery]` effect fetches `users?name_like=...` into results. Render input + results `<ul>`. Export `DebounceSearch` default.
TRY THIS: Render `<DebounceSearch />` and type "le" quickly.
EXPECTED OUTPUT: The fetch fires once ~500ms after typing stops; results render below.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
