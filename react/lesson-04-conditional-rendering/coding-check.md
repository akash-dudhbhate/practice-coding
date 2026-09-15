# Lesson 04 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01-solve.jsx (Show/Hide Toggle)
- [ ] Uses `useState(false)` for visibility boolean.
- [ ] Button toggles state: `setShow(!show)`.
- [ ] Message rendered with `&&`: `{show && <p>Message</p>}`.
- [ ] Test: Click once → message appears.
- [ ] Test: Click again → message disappears.
- [ ] Test: No "0" or "false" text rendered when hidden.

### p02-solve.jsx (Login/Logout Button)
- [ ] Uses `useState(false)` for isLoggedIn.
- [ ] Button text uses ternary: `{isLoggedIn ? "Logout" : "Login"}`.
- [ ] Clicking toggles login state.
- [ ] Test: Initially shows "Login".
- [ ] Test: Click → shows "Logout".
- [ ] Test: Click again → shows "Login".

### p03-solve.jsx (Even/Odd Display)
- [ ] Has a number state (with increment button or input).
- [ ] Uses ternary: `{number % 2 === 0 ? "Even" : "Odd"}`.
- [ ] Test: Number 0 → shows "Even".
- [ ] Test: Number 1 → shows "Odd".
- [ ] Test: Number 2 → shows "Even".
- [ ] Test: Number 7 → shows "Odd".

## Medium

### p01-solve.jsx (Loading State)
- [ ] Uses `useState(true)` for loading state.
- [ ] Uses `setTimeout(() => setLoading(false), 2000)` in `useEffect`.
- [ ] Early return: `if (loading) return <p>Loading...</p>`.
- [ ] Content shows after loading completes.
- [ ] Test: On mount → shows "Loading...".
- [ ] Test: After 2 seconds → shows content.
- [ ] Test: No crash when rendering content (data is available).

### p02-solve.jsx (Empty List Message)
- [ ] Uses `todos.length === 0` to check empty (NOT `!todos` — empty array is truthy).
- [ ] Empty state shows helpful message: "No todos yet!".
- [ ] Non-empty state renders the list with `.map()`.
- [ ] Test: Empty array → shows "No todos yet!".
- [ ] Test: Add one item → list shows with that item.
- [ ] Test: Remove all items → empty message returns.
- [ ] Test: No "0" rendered when list is empty.

### p03-solve.jsx (Conditional CSS Classes)
- [ ] Uses template literal for className: `` `btn ${isActive ? "active" : ""}` ``.
- [ ] Disabled state adds "disabled" class.
- [ ] No "false" or "undefined" in the className string.
- [ ] Test: Active state → className includes "active".
- [ ] Test: Inactive state → className does NOT include "active".
- [ ] Test: Disabled state → className includes "disabled".
- [ ] Test: No extra spaces or "false" text in class attribute.

## Hard

### p01-solve.jsx (Full Data Fetch States)
- [ ] Has `loading`, `error`, and `data` state variables.
- [ ] Early return for loading: `if (loading) return <p>Loading...</p>`.
- [ ] Early return for error: `if (error) return <p>Error: {error}</p>`.
- [ ] Early return for empty: `if (!data || data.length === 0) return <p>No data</p>`.
- [ ] Success state renders the data.
- [ ] Test: Initial render → shows "Loading...".
- [ ] Test: After load with data → shows content.
- [ ] Test: After load with error → shows error message.
- [ ] Test: After load with empty data → shows "No data".
- [ ] Test: No crash in any state (null/undefined guarded).

### p02-solve.jsx (Object Map Status Display)
- [ ] Defines a `messages` object with keys: "loading", "success", "error", "empty".
- [ ] Each key maps to different JSX.
- [ ] Renders `{messages[status]}` with fallback: `|| <p>Unknown</p>`.
- [ ] Test: status="loading" → shows loading message.
- [ ] Test: status="success" → shows success message.
- [ ] Test: status="error" → shows error message.
- [ ] Test: status="empty" → shows empty message.
- [ ] Test: status="unknown" → shows fallback "Unknown" message.
- [ ] Test: No nested ternaries used.

### p03-solve.jsx (Permission-Based Dashboard)
- [ ] Accepts `role` prop ("admin", "editor", "viewer").
- [ ] Admin sees: stats, edit tools, delete button, settings.
- [ ] Editor sees: stats, edit tools (no delete, no settings).
- [ ] Viewer sees: stats only (read-only).
- [ ] Uses `&&` for conditional elements: `{canEdit && <EditButton />}`.
- [ ] Test: role="admin" → all sections visible.
- [ ] Test: role="editor" → no delete button, no settings.
- [ ] Test: role="viewer" → only stats visible, no edit/delete/settings.
- [ ] Test: Unknown role → shows viewer content or a safe default.
