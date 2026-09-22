/*
LESSON 11 — Context API
MEDIUM P02 — Multiple Contexts
============================================
CONCEPT: An app usually has several contexts (auth, theme, locale…). You nest their Providers, and each consumer subscribes only to the ones it needs — updating one context doesn't re-render consumers of the other.
PROBLEM: Create two contexts: `UserContext` and `ThemeContext`. Build a `Component` that reads BOTH via `useContext` and renders `user.name` plus the theme with theme-dependent styles. `App` holds `theme` in `useState`, nests `<UserContext.Provider value={{name:"Alice"}}>` around `<ThemeContext.Provider value={theme}>`, renders `Component`, and a button toggling the theme.
TRY THIS: Render `<App />` and click "Toggle Theme" — theme flips while the user stays "Alice".
EXPECTED OUTPUT: "Alice - light" on white background; after toggle "Alice - dark" on dark background.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
