/*
LESSON 15 — Portals & Modals
EASY P02 — Modal that Closes on Overlay Click
============================================
CONCEPT: Clicking the dark backdrop should close a modal, but clicks INSIDE the content bubble up to the overlay too. `e.stopPropagation()` on the content box stops that — the standard dismiss-on-outside-click pattern.
PROBLEM: Build `Modal({onClose})`: the overlay div's `onClick={onClose}`, the inner content div's `onClick={(e) => e.stopPropagation()}` so only outside clicks close. Portal to `document.body`. `App` toggles it with `useState` and an Open button.
TRY THIS: Render `<App />`, open the modal, click the dimmed area — closes. Click inside the white box — stays open.
EXPECTED OUTPUT: Overlay click closes; content click does not.
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
