/*
LESSON 17 — Zustand
MEDIUM P03 — Persist Middleware (localStorage)
============================================
CONCEPT: `persist` from `zustand/middleware` wraps your store creator and syncs state to localStorage under a `name` key. `partialize` picks WHICH fields survive — you usually don't want to persist functions or transient UI state.
PROBLEM: Create `usePrefsStore = create(persist((set) => ({theme:"light", username:"", setTheme, setUsername}), {name:"user-prefs", partialize: (state) => ({theme: state.theme, username: state.username})}))`. Build `App` reading all four: a themed container, a Theme toggle button, a username input, and a greeting.
TRY THIS: Render `<App />`, set a username and dark theme, then RELOAD the page — both survive.
EXPECTED OUTPUT: Preferences persist across reloads (check localStorage key "user-prefs").
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
