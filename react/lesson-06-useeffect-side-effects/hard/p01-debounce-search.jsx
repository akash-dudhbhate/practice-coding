/*
LESSON 06 — useEffect & Side Effects
HARD P01 — Live Search with Debounce
============================================
CONCEPT: Debounce = setTimeout in the effect + clearTimeout in cleanup. Every keystroke cancels the pending fetch until typing pauses.
PROBLEM: Build a `LiveSearch` with `query` and `results` state. In a `[query]`-deps effect: empty query clears results; otherwise setTimeout 500ms then fetch `users?name_like=${query}` into results; cleanup clears the timer. Render the input and a `<ul>` of result names.
TRY THIS: Render `<LiveSearch />` and type "lea" quickly.
EXPECTED OUTPUT: One fetch fires ~500ms after you stop typing; results list appears.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
