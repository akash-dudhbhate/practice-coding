/*
LESSON 10 — Custom Hooks
MEDIUM P02 — useLocalStorage Hook
============================================
CONCEPT: useLocalStorage mirrors useState's API but hydrates from localStorage and writes back in an effect — state that survives reloads.
PROBLEM: Build `useLocalStorage(key, initial)` returning `[value, setValue]`: lazy-init state from `localStorage.getItem` (JSON.parse) and a `[key, value]` effect that `setItem`s (JSON.stringify). Then `LocalStorageDemo` persists `theme` (light/dark toggle restyles the div) and `name` input. Export `LocalStorageDemo` default.
TRY THIS: Render `<LocalStorageDemo />`, type a name, toggle dark, reload the page.
EXPECTED OUTPUT: Theme and name are still there after reload.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
