/*
LESSON 19 — Testing React
HARD P01 — Comprehensive Modal Tests
============================================
CONCEPT: A modal has many behaviors — presence/absence (queryByText returns null instead of throwing), close via button / overlay (`data-testid`) / Escape `keyDown`, and a side effect on `document.body.style.overflow`.
PROBLEM: For `Modal` (import "../Modal") taking `{open, onClose, children}` and rendering an overlay with `data-testid="modal-overlay"`, write SIX tests: closed → `queryByText("Content")` is null; open → content found; close button calls `onClose`; overlay click calls `onClose`; `fireEvent.keyDown(document, {key: "Escape"})` calls `onClose`; `document.body.style.overflow` is "hidden" while open.
TRY THIS: Run the suite — the modal's full contract is pinned down.
EXPECTED OUTPUT: 6 passing tests covering visibility, all three close paths, and scroll lock.
CHECK: python3 check.py hard/p01
*/
// TODO: write your test from scratch
