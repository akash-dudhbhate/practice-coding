/*
LESSON 12 — useReducer
HARD P03 — Combined App State (useReducer + Context)
============================================
CONCEPT: One root reducer can manage several sub-states (auth, theme, notifications) at once — the "poor man's Redux" architecture. Context distributes `{state, dispatch}` so each component touches only the slice it needs.
PROBLEM: Define `initialState` = `{auth: {user: null}, theme: "light", notifications: []}` and a reducer handling `"LOGIN"`, `"LOGOUT"`, `"TOGGLE_THEME"`, `"ADD_NOTIFICATION"`, `"REMOVE_NOTIFICATION"`. Create `AppContext` and an `AppProvider({children})` providing `{state, dispatch}`. Build `Header` (greets `state.auth.user` or "Guest", a Theme toggle button, and Login/Logout buttons) and `Notifications` (renders each `state.notifications` item, click to remove). `App` wraps both in `AppProvider`.
TRY THIS: Render `<App />`, click Login, then Theme — the header background flips while the greeting stays.
EXPECTED OUTPUT: "Guest"/Login at first; "Hello, Alice"/Logout after Login; header color toggles independently.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
