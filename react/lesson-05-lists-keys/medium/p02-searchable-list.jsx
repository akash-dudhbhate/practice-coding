/*
LESSON 05 — Lists & Keys
MEDIUM P02 — Searchable List
============================================
CONCEPT: Filtering is derived data — compute `items.filter(...)` during render from state instead of storing a second copy.
PROBLEM: Build a `SearchableList` component. Keep an `items` constant (fruit names) and `query` state. Compute `filtered` with `.filter(i => i.toLowerCase().includes(query.toLowerCase()))`. Render a search input, then "No results" or the filtered `<ul>`.
TRY THIS: Render `<SearchableList />` and type "an".
EXPECTED OUTPUT: Only items containing "an" remain (Banana); gibberish shows "No results".
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
