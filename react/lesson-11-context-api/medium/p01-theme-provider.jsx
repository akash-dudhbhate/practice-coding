/*
LESSON 11 — Context API
MEDIUM P01 — ThemeProvider with Toggle
============================================
CONCEPT: The common pattern is a dedicated Provider component that owns the state and exposes `{value, updater}` through context. Consumers get both the data and the way to change it.
PROBLEM: Create `ThemeContext` and a `useTheme()` hook wrapping `useContext`. Build `ThemeProvider({children})` that holds `theme` in `useState("light")` and provides `{theme, toggleTheme}` where `toggleTheme` flips light/dark. Create `Header`, `Sidebar`, and `Main` components that all read `theme` via `useTheme()` and style their background accordingly. `App` renders a toggle button calling `toggleTheme` plus all three consumers inside `ThemeProvider`.
TRY THIS: Render `<App />` and click "Toggle" — all three sections flip colors together.
EXPECTED OUTPUT: Header, Sidebar, and Main all switch between light and dark styling on each click.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
