/*
LESSON 11 — Context API
MEDIUM P03 — Custom useTheme Hook with Error Check
============================================
CONCEPT: useContext returns the default value when there's no Provider above — which silently hides bugs. A custom hook that throws a clear error when the context is missing turns silent failures into obvious ones.
PROBLEM: Create `ThemeContext` with default `null`. Write a `useTheme()` hook that calls `useContext(ThemeContext)` and throws `new Error("useTheme must be used within ThemeProvider")` when the result is falsy. Build `ThemeProvider({children})` providing `{theme: "dark"}` and a `ThemedComponent` that renders the theme via `useTheme()`. `App` wraps `ThemedComponent` in `ThemeProvider`.
TRY THIS: Render `<App />` — it works. Then render `<ThemedComponent />` WITHOUT the provider — you get a clear error instead of a crash on `undefined`.
EXPECTED OUTPUT: "Theme: dark" when wrapped; a descriptive thrown error when not.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
