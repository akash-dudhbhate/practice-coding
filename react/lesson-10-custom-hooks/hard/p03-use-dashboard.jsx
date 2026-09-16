/*
LESSON 10 — Custom Hooks
HARD P03 — Composed useUserDashboard
============================================
CONCEPT: Custom hooks compose like Lego: useUserDashboard internally calls useFetch + useDebounce + useLocalStorage and returns one tidy object for the component.
PROBLEM: Build `useFetch`, `useDebounce`, `useLocalStorage`, then `useUserDashboard(userId)` combining them: fetch the user, keep `search` state + debounced search feeding a second useFetch, and persist `theme` via localStorage. `Dashboard({userId=1})` renders user info, theme toggle (restyles the div), and the search results list. Export `Dashboard` default.
TRY THIS: Render `<Dashboard userId={1} />`, toggle theme, type in the search box.
EXPECTED OUTPUT: User card loads; theme flips and persists; results appear after the debounce.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
