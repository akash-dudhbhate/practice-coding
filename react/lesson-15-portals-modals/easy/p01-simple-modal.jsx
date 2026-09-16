/*
LESSON 15 — Portals & Modals
EASY P01 — Simple Modal with createPortal
============================================
CONCEPT: `createPortal(jsx, document.body)` renders children into a DOM node OUTSIDE the React tree — essential for modals that must escape parent `overflow`/`z-index` stacking contexts.
PROBLEM: Build `Modal({onClose})` that portals a fixed overlay div (dark translucent background, centered white box with content + Close button calling `onClose`) into `document.body`. `App` holds `open` in `useState` with an "Open Modal" button; render `<Modal>` only when `open`.
TRY THIS: Render `<App />`, click Open — overlay covers the viewport; Close dismisses it.
EXPECTED OUTPUT: Centered modal over a dimmed page; Close button hides it.
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
