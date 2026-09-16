/*
LESSON 08 — useRef & DOM Access
HARD P02 — Scroll To Top Button
============================================
CONCEPT: Scroll position lives on `window`, not in React — a `[]` effect adds the scroll listener, state tracks visibility, cleanup removes the listener.
PROBLEM: Build a `ScrollToTop` with `visible` state. In a `[]` effect, listen for "scroll" and set `visible` when `window.scrollY > 200`; cleanup removes it. Render `null` when hidden, else a fixed-position button calling `window.scrollTo({ top: 0, behavior: "smooth" })`.
TRY THIS: Render `<ScrollToTop />` on a tall page and scroll down past 200px.
EXPECTED OUTPUT: A "↑ Top" button fades in; clicking it smooth-scrolls to the top.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
