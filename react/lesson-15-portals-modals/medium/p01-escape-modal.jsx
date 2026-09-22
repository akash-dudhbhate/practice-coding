/*
LESSON 15 — Portals & Modals
MEDIUM P01 — Modal with Escape Key + Scroll Lock
============================================
CONCEPT: Real modals need side effects: a `keydown` listener for Escape and `document.body.style.overflow = "hidden"` to freeze background scroll — both cleaned up in `useEffect`'s return so nothing leaks after close.
PROBLEM: Build `Modal({onClose, children})` whose `useEffect` adds a `keydown` listener calling `onClose` when `e.key === "Escape"`, sets body overflow hidden, and removes both in cleanup. Render the usual portal overlay + `stopPropagation` content with a Close button. `App` toggles via `useState`.
TRY THIS: Render `<App />`, open the modal, press Escape — it closes; try scrolling the page while open — it's locked.
EXPECTED OUTPUT: Escape closes the modal; background can't scroll while open; both restore on close.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
