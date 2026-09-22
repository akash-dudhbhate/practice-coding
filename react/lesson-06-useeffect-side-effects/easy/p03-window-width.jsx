/*
LESSON 06 — useEffect & Side Effects
EASY P03 — Window Width Tracker
============================================
CONCEPT: Listeners added in an effect must be removed — return a cleanup function so `removeEventListener` runs on unmount and before re-runs.
PROBLEM: Build a `WindowWidth` component with `width` state (init `window.innerWidth`). In a `[]`-deps effect, add a "resize" listener updating width and return a cleanup that removes it. Render the width.
TRY THIS: Render `<WindowWidth />` and resize the browser.
EXPECTED OUTPUT: "Window width: NNNpx" follows the window size live.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
