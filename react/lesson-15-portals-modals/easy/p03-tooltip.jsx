/*
LESSON 15 — Portals & Modals
EASY P03 — Tooltip via Portal
============================================
CONCEPT: Tooltips need fixed positioning relative to the VIEWPORT, not the parent — so they must portal to `document.body` and measure the anchor with `getBoundingClientRect()` on hover.
PROBLEM: Build `Tooltip({text, children})`: a `useRef` on the wrapping `span`; `onMouseEnter` reads `ref.current.getBoundingClientRect()` and stores `{top: rect.bottom + 8, left: rect.left}` in state plus `show=true`; `onMouseLeave` hides. When shown, portal a small fixed-position div (dark bg, white text) at those coordinates into `document.body`. `App` uses it around some text.
TRY THIS: Render `<App />` and hover the wrapped text — the tooltip appears just below it.
EXPECTED OUTPUT: A dark tooltip pops under the element on hover and vanishes on leave.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
