/*
LESSON 15 — Portals & Modals
MEDIUM P02 — Confirmation Dialog
============================================
CONCEPT: A reusable confirm dialog reports the user's choice through callback props — `onConfirm` / `onCancel` — so the parent decides what happens (delete, navigate away…) while the dialog stays generic.
PROBLEM: Build `ConfirmDialog({message, onConfirm, onCancel})` portaling an overlay (click → `onCancel`) and a centered box with `{message}`, a Confirm button (`onConfirm`), and a Cancel button (`onCancel`); `stopPropagation` on the content. `App` shows a "Delete Item" button that opens it with `message="Are you sure?"`; confirm alerts "Deleted!"; both buttons close it.
TRY THIS: Render `<App />`, click Delete Item, then Confirm vs. Cancel vs. the backdrop.
EXPECTED OUTPUT: Confirm runs the action; Cancel and overlay-click just dismiss.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
