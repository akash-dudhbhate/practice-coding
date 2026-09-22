/*
LESSON 15 — Portals & Modals
HARD P01 — Accessible Modal (Focus Trap + ARIA)
============================================
CONCEPT: Accessible modals do three jobs: `role="dialog"` + `aria-modal="true"` for screen readers, a Tab focus trap (Tab on the last focusable wraps to first, Shift+Tab on first wraps to last), and restoring `document.activeElement` focus on close.
PROBLEM: Build `AccessibleModal({onClose, children})`: refs for the modal box and the previously focused element. In `useEffect`: save `document.activeElement`, focus the modal, and add a `keydown` handler — Escape closes; Tab queries `button, a, input, [tabindex]` inside the modal and wraps focus at both ends. Cleanup removes the listener, unlocks scroll, and re-focuses the previous element. Content div gets `role="dialog" aria-modal="true" tabIndex={-1}` and `stopPropagation`. `App` toggles it.
TRY THIS: Render `<App />`, open the modal, press Tab repeatedly — focus cycles inside only; Escape closes and focus returns to the Open button.
EXPECTED OUTPUT: Focus trapped while open, restored on close, proper dialog ARIA attrs.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
