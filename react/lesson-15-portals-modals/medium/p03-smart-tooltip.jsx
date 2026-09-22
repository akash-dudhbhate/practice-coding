/*
LESSON 15 — Portals & Modals
MEDIUM P03 — Smart-Positioning Tooltip
============================================
CONCEPT: A tooltip that overflows the viewport is broken. Measuring the anchor (`getBoundingClientRect`) against `window.innerWidth/innerHeight` lets you flip the tooltip left/above when there's no room right/below.
PROBLEM: Build `SmartTooltip({text, children})`: on `onMouseEnter`, read the anchor's rect; if `rect.right + tooltipWidth > vw` position it left of the anchor, if `rect.bottom + tooltipHeight > vh` position it above; store `{top, left}` and show a portal'ed fixed div into `document.body`. Hide on mouse leave. `App` renders one around "Hover me".
TRY THIS: Render `<App />` with the anchor near the right/bottom edge — the tooltip flips to stay visible.
EXPECTED OUTPUT: Tooltip never clips off-screen; it mirrors to the free side near edges.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
