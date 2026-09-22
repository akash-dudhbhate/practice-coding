/*
LESSON 17 — Zustand
EASY P02 — Theme Store with Selectors
============================================
CONCEPT: `useStore((s) => s.theme)` selects just one field — the component only re-renders when THAT slice changes, not on every store update. Selectors are Zustand's performance story.
PROBLEM: Create `useThemeStore` with `theme: "light"` and `toggleTheme` (flips light/dark). Build `Header`, `Main`, and `Footer` — each selecting ONLY `s.theme` via the hook and styling its background dark/light. `App` selects `s.toggleTheme` for a Toggle button and renders all three.
TRY THIS: Render `<App />` and click Toggle — all three sections flip together with zero prop drilling.
EXPECTED OUTPUT: Header/Main/Footer all switch dark↔light on each click.
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
