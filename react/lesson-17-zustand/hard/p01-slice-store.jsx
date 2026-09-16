/*
LESSON 17 — Zustand
HARD P01 — Multi-Slice Store
============================================
CONCEPT: Big stores are composed from slice functions — `createAuthSlice(set)`, `createCartSlice(set)`, `createThemeSlice(set)` — each returning its own fields+actions, then spread together in one `create((...a) => ({...sliceA(...a), ...sliceB(...a)}))`. Components select only their slice.
PROBLEM: Write `createAuthSlice` (user, login, logout), `createCartSlice` (cart, addToCart, clearCart), `createThemeSlice` (theme, toggleTheme). Combine into `useStore`. Build `AuthComponent` (login/logout UI), `CartComponent` (add + count), `ThemeComponent` (toggle showing theme) — each selecting only its own fields. `App` renders all three.
TRY THIS: Render `<App />`, toggle theme — only ThemeComponent re-renders (check React DevTools highlighting).
EXPECTED OUTPUT: Three independent widgets sharing one store, each updating in isolation.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
