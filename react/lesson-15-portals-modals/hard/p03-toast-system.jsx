/*
LESSON 15 — Portals & Modals
HARD P03 — Toast / Notification System
============================================
CONCEPT: Toasts need to be callable from ANYWHERE without props — so a module-level `toast` object notifies a `Set` of listeners, and one `ToastContainer` (portaled to `document.body`) renders the stack.
PROBLEM: Create `toast` with `success(msg)`/`error(msg)` methods that broadcast `{id: ++toastId, type, msg}` to a module-level `listeners` Set. Build `ToastContainer`: `useState` list; a `useEffect` registers a listener that appends the toast and `setTimeout`-removes it after 3000ms; cleanup removes the listener. Portal a fixed top-right column mapping `toasts` to styled divs (green for success, red for error, click to dismiss, `key` per toast). `App` has Success/Error buttons calling `toast.success("Saved!")` etc. plus `<ToastContainer />`.
TRY THIS: Render `<App />`, click Success twice fast — two toasts stack, each auto-dismissing after 3s.
EXPECTED OUTPUT: Corner toasts appear, stack, click-to-close, and auto-dismiss.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
