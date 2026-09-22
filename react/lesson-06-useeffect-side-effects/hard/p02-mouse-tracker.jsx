/*
LESSON 06 — useEffect & Side Effects
HARD P02 — Mouse Position Tracker
============================================
CONCEPT: Global listeners go on `window` inside an effect; cleanup removes them so they don't leak after unmount.
PROBLEM: Build a `MouseTracker` with `pos` state `{x, y}`. In a `[]` effect add a "mousemove" listener on window storing `e.clientX/clientY`; cleanup removes it. Render the coordinates and a small fixed red dot positioned at the cursor.
TRY THIS: Render `<MouseTracker />` and move the mouse.
EXPECTED OUTPUT: "X: N, Y: M" tracks the cursor and a red dot follows it.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
