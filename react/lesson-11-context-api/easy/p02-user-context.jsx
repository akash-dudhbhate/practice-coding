/*
LESSON 11 — Context API
EASY P02 — User Context (No Prop Drilling)
============================================
CONCEPT: Prop drilling means passing the same prop through many layers that don't need it. Context removes it: any descendant can grab the value directly with useContext.
PROBLEM: Create a `UserContext` (default null). Build a `DeepChild` component that reads the user via `useContext(UserContext)` and renders the user's `name` and `role`. Render it through two wrapper components (`Top` → `Middle` → `DeepChild`) that take NO props. `App` provides `value={{ name: "Alice", role: "admin" }}`.
TRY THIS: Render `<App />` — notice `Top` and `Middle` never mention `user`.
EXPECTED OUTPUT: "Welcome, Alice! Role: admin" rendered by the deeply nested child.
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
