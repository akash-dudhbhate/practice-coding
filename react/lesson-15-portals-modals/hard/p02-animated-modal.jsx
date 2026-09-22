/*
LESSON 15 — Portals & Modals
HARD P02 — Animated Modal with Exit Transition
============================================
CONCEPT: A modal can't animate out if it unmounts instantly. The trick: keep it mounted, flip a `visible` flag to drive CSS `transition` (opacity for overlay, translateY for content), and call the real `onClose` inside a `setTimeout` matching the animation duration.
PROBLEM: Build `AnimatedModal({onClose, children})`: `visible` starts false; a `useEffect` + `requestAnimationFrame` sets it true (entry animation). `handleClose` sets `closing`/`visible` false and calls `setTimeout(onClose, 300)`. The portal overlay fades via `opacity` + `transition`, the content slides via `transform: translateY(...)`. `App` toggles via `useState`.
TRY THIS: Render `<App />`, open and close the modal — it slides/fades both directions instead of snapping.
EXPECTED OUTPUT: Smooth fade+slide in on open, reverse on close before unmount.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
