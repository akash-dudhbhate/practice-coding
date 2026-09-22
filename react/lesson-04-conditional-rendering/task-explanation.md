# Lesson 04 — Conditional Rendering

## What you'll learn
- How to show or hide content based on conditions.
- Three main patterns: `&&`, ternary `? :`, and early return.
- How to handle loading, error, and empty states.
- Common pitfalls with falsy values in JSX.

## Lesson

Conditional rendering lets you show different UI based on data, state, or user roles.

```jsx
function App({ isLoggedIn, isLoading }) {
  if (isLoading) return <Spinner />;
  if (!isLoggedIn) return <Login />;

  return <Dashboard />;
}
```

### Three main patterns
1. **`&&`** — show only if true: `{showMessage && <p>Hello!</p>}`
2. **Ternary** — show one or the other: `{isLoggedIn ? <Logout /> : <Login />}`
3. **Early return** — return early before main render: `if (loading) return <Spinner />;`

### Key rules
- `false`, `null`, `undefined`, `true` → React renders nothing.
- `0` and `NaN` → React RENDERS them. Use `{count > 0 && ...}` not `{count && ...}`.
- For 3+ mutually exclusive states, use an object map instead of nested ternaries.
- Always return `null` explicitly — never `undefined`.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.jsx` — **Show/Hide Toggle:** A button that toggles a message on and off. Use `&&` to conditionally render the message.

   WHAT IT SHOULD LOOK LIKE:
   ```
   HIDDEN:                  SHOWN (after click):
   +----------+             +----------+
   | [ Show ] |             | [ Hide ] |
   +----------+             +----------+
                            Hello, I'm visible!   <- <p> appears
   ```
2. `easy/p02-solve.jsx` — **Login/Logout Button:** Show "Login" button when not logged in, "Logout" button when logged in. Use ternary operator.

   WHAT IT SHOULD LOOK LIKE:
   ```
   LOGGED OUT:              LOGGED IN (after click):
   +-----------+            +------------+
   | [ Login ] |            | [ Logout ] |
   +-----------+            +------------+
   ```
3. `easy/p03-solve.jsx` — **Even/Odd Display:** Given a number state, show "Even" or "Odd" text. Use ternary with modulo operator.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-----+                  +-----+
   |  4  |                  |  7  |        <- number input
   +-----+                  +-----+
   Even                     Odd            <- <p> via ternary
   ```

### Medium
4. `medium/p01-solve.jsx` — **Loading State:** A component that simulates loading (use state + setTimeout). Show "Loading..." while loading, then show content. Practice early return + loading state.

   WHAT IT SHOULD LOOK LIKE:
   ```
   WHILE LOADING:           AFTER CLICK:
   Loading...               Content loaded!
   [ Simulate Loaded ]
   ```
5. `medium/p02-solve.jsx` — **Empty List Message:** A todo list that shows "No todos yet!" when the list is empty, and the list when it has items. Practice empty state with `length === 0`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   EMPTY:                   AFTER 2 x ADD:
   [ Add ]                  [ Add ]
   No todos yet!            * Item 1
                            * Item 2
   ```
6. `medium/p03-solve.jsx` — **Conditional CSS Classes:** A button that changes its className based on state (active/inactive/disabled). Use template literals for conditional classes.

   WHAT IT SHOULD LOOK LIKE:
   ```
   ACTIVE:                  DISABLED (after [Disable]):
   +-----------+            +-------------+
   | [ Click ] |  btn-active| [ Click ]   |  btn-disabled, grayed
   +-----------+            +-------------+   out, unclickable
   [ Disable ]
   ```

### Hard
7. `hard/p01-solve.jsx` — **Full Data Fetch States:** A component with loading, error, empty, and success states. Each shows different UI. Practice handling all states with early returns.

   WHAT IT SHOULD LOOK LIKE:
   ```
   IDLE:          LOADING:      SUCCESS:                ERROR:
   [ Fetch Data ] Loading...    Data loaded             Something went wrong (red)
                                successfully!           [ Retry ]
   ```
8. `hard/p02-solve.jsx` — **Object Map Status Display:** A component that shows different content based on status ("loading", "success", "error", "empty"). Use an object map pattern instead of nested ternaries.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [loading] [success] [error] [empty]   <- 4 status buttons

   Please wait...            <- <p> swaps to match the
                                  clicked status
   ```
9. `hard/p03-solve.jsx` — **Permission-Based Dashboard:** Show different UI for admin, editor, and viewer roles. Admin sees everything, editor sees edit tools, viewer sees read-only. Practice multiple conditional checks.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Role: [admin v]              <- <select>
   Dashboard (admin)
   +----------------------------------+
   | View Content                     |  <- everyone sees this
   +----------------------------------+
   | Edit Tools                       |  <- editor + admin only
   +----------------------------------+
   | Admin Panel                      |  <- admin only
   +----------------------------------+
   (viewer sees only View Content)
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete component from scratch** below the TODO marker.
- Remove the TODO line when done.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
