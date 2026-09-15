# Lesson 04 — Concepts Explained (Conditional Rendering)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Conditional Rendering

**What:** Conditional rendering means showing different UI based on a condition — like `if` statements but for what appears on screen.

```jsx
function Greeting({ isLoggedIn }) {
  if (isLoggedIn) {
    return <h1>Welcome back!</h1>;
  }
  return <h1>Please sign in.</h1>;
}
```

React renders whatever the component returns. If you return different JSX based on a condition, the UI changes.

**Why it exists:** UIs are dynamic — you show different content for logged-in vs. anonymous users, loading vs. loaded data, empty vs. full lists. Conditional rendering makes this possible.

**Where it's used:** Auth gates (login vs. dashboard), loading spinners, error messages, empty states, feature toggles, admin vs. user views.

**What goes wrong without it:**
- Everything always shows → no loading states, no error handling, broken UX.
- Trying to hide with CSS (`display: none`) → component still mounts, runs effects, wastes resources. Better to not render at all.
- Returning `undefined` → React may render nothing or show "undefined" text. Always return `null` explicitly.

---

## Logical AND (&&) Operator

**What:** The `&&` operator renders content only when the condition is true. It's the simplest way to conditionally show something.

```jsx
function Notification({ hasMessage }) {
  return (
    <div>
      <h1>Inbox</h1>
      {hasMessage && <p>You have a new message!</p>}
    </div>
  );
}
```

When `hasMessage` is `true`, the `<p>` renders. When `false`, React renders nothing.

**Why it exists:** When you only need to show OR hide something (no alternative content), `&&` is cleaner than a ternary. One line, no `else` branch needed.

**Where it's used:** Showing badges (notification dot), conditional labels, showing/hiding optional sections, feature flags.

**What goes wrong without it:**
- **The number 0 trap:** `{count && <p>{count} items</p>}` — when `count` is 0, React renders "0" on screen! 0 is falsy but React still renders it. Fix: `{count > 0 && <p>{count} items</p>}`.
- **Empty string trap:** `{text && <p>{text}</p>}` — empty string is falsy, so this works. But `{"" && <p />}` renders nothing (correct), while `{0 && <p />}` renders "0" (wrong).
- **Falsy values rendered:** `false`, `null`, `undefined`, `true` are NOT rendered by React. But `0` and `NaN` ARE rendered. Always use explicit comparisons for numbers.

---

## Ternary Operator (? :)

**What:** The ternary operator renders one thing if true, another if false. It's an inline if-else for JSX.

```jsx
function AuthButton({ isLoggedIn }) {
  return (
    <button>
      {isLoggedIn ? "Logout" : "Login"}
    </button>
  );
}

// Rendering different components
function Dashboard({ user }) {
  return (
    <div>
      {user.role === "admin" ? <AdminPanel /> : <UserPanel />}
    </div>
  );
}
```

**Why it exists:** When you need to show one of TWO options, the ternary is the cleanest inline approach. It's more compact than an `if-else` in the function body when the condition is inside JSX.

**Where it's used:** Login/logout buttons, loading vs. content, empty vs. filled states, admin vs. user views, enabled vs. disabled states.

**What goes wrong without it:**
- Nesting ternaries: `cond1 ? (cond2 ? A : B) : (cond3 ? C : D)` → hard to read, easy to get wrong. Extract to variables or use early returns instead.
- Using `&&` when you need an else: `{isLoggedIn && "Logout"}` → shows nothing when logged out (no "Login" button). Need ternary for both branches.
- Forgetting the colon: `cond ? A` → syntax error. Ternary requires both `?` and `:`.

---

## Early Return

**What:** Return `null` (or different JSX) before the main return based on a condition. This keeps the main JSX clean.

```jsx
function UserProfile({ user, loading, error }) {
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;
  if (!user) return <p>No user found.</p>;

  // Main render — only runs when user exists and no error/loading
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

**Why it exists:** Without early returns, you'd nest everything in conditionals: `{!loading && !error && user && (<div>...</div>)}`. Early returns flatten the code — each condition is checked top-to-bottom, and the main render only handles the happy path.

**Where it's used:** Data fetching components (loading → error → empty → content), auth gates, permission checks, null guards.

**What goes wrong without it:**
- Deeply nested conditionals → hard to read, hard to maintain.
- Accessing `user.name` when `user` is null → crash: "Cannot read properties of null". Early return prevents this.
- Returning `undefined` instead of `null` → React may render "undefined". Always `return null`.

---

## Loading States

**What:** While waiting for async operations (API calls, file loading), show a loading indicator instead of the content.

```jsx
function DataFetcher() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  // (fetch logic would go here)

  if (loading) return <div>Loading...</div>;

  return <div>{data.name}</div>;
}
```

**Why it exists:** API calls take time. Without a loading state, the user sees a blank screen or a crash (trying to render `null` data). Loading states give feedback that something is happening.

**Where it's used:** API data fetching, image loading, file uploads, route transitions, any async operation.

**What goes wrong without it:**
- Rendering `data.name` before data loads → `data` is `null` → crash: "Cannot read properties of null (reading 'name')".
- No visual feedback → user thinks the app is broken, clicks again, causes duplicate requests.
- Loading state never set to false → stuck on "Loading..." forever.

---

## Error States

**What:** When an operation fails (API error, network issue), show an error message instead of crashing.

```jsx
function DataFetcher() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  if (error) return <div className="error">Error: {error.message}</div>;

  return <div>{data.name}</div>;
}
```

**Why it exists:** Networks fail, APIs return errors, data is malformed. Without error states, the app crashes and the user sees a white screen. Error states gracefully show what went wrong and often offer a retry button.

**Where it's used:** API calls, file uploads, form submissions, any operation that can fail.

**What goes wrong without it:**
- Unhandled promise rejection → app crashes, white screen.
- Rendering error data as if it's success → confusing UI, wrong information shown.
- No retry option → user is stuck, can't recover from a temporary error.

---

## Empty States

**What:** When a list or data is empty (no items, no results), show a helpful message instead of a blank screen.

```jsx
function TodoList({ todos }) {
  if (todos.length === 0) {
    return <p>No todos yet. Add one to get started!</p>;
  }

  return (
    <ul>
      {todos.map(todo => <li key={todo.id}>{todo.text}</li>)}
    </ul>
  );
}
```

**Why it exists:** A blank screen confuses users — they don't know if the app is broken, loading, or genuinely empty. Empty states explain the situation and guide the user on what to do next.

**Where it's used:** Empty inboxes, empty carts, no search results, empty dashboards, first-time user experiences.

**What goes wrong without it:**
- Empty `<ul></ul>` renders → user sees nothing → thinks app is broken.
- No call-to-action → user doesn't know how to get started.
- Checking `todos` instead of `todos.length` → `[]` is truthy! `if (!todos)` won't catch empty arrays. Use `todos.length === 0`.

---

## Conditional CSS Classes

**What:** Apply different CSS classes based on conditions using template literals or the `clsx`/`cn` pattern.

```jsx
function Button({ variant, disabled }) {
  return (
    <button
      className={`btn ${variant === "primary" ? "btn-primary" : "btn-secondary"} ${disabled ? "btn-disabled" : ""}`}
    >
      Click me
    </button>
  );
}

// Cleaner approach with array filter
function StatusBadge({ status }) {
  return (
    <span className={["badge", `badge-${status}`, status === "error" && "badge-pulse"]
      .filter(Boolean)
      .join(" ")}>
      {status}
    </span>
  );
}
```

**Why it exists:** UIs need dynamic styling — active tabs, error states, disabled buttons, hover effects. Conditional classes let you toggle styles based on state without inline styles.

**Where it's used:** Active nav items, error/success states, disabled buttons, theme switching, responsive layouts.

**What goes wrong without it:**
- Template literal with `false`: `className="btn ${isActive && "active"}` → renders "btn false" when inactive. Use ternary or filter: `${isActive ? "active" : ""}`.
- Forgetting to join: `className={["btn", "active"]}` → React renders "btnactive" (no space). Must `.join(" ")`.
- Overusing inline styles instead of conditional classes → harder to maintain, no CSS caching.

---

## Enum / Object Map for Multiple Conditions

**What:** When you have many mutually exclusive conditions (more than 2), use an object map instead of nested ternaries.

```jsx
function StatusMessage({ status }) {
  const messages = {
    loading: <p>Loading...</p>,
    success: <p>✓ Data loaded successfully!</p>,
    error: <p>✗ Something went wrong.</p>,
    empty: <p>No data available.</p>,
  };

  return <div>{messages[status] || <p>Unknown status.</p>}</div>;
}
```

**Why it exists:** Nested ternaries for 4+ conditions are unreadable: `status === "loading" ? A : status === "error" ? B : status === "empty" ? C : D`. An object map is cleaner, easier to extend, and easier to read.

**Where it's used:** Status displays, multi-state UIs (loading/success/error/empty), role-based rendering, step indicators.

**What goes wrong without it:**
- Nested ternaries → unreadable, bug-prone, hard to add new states.
- Switch statements in JSX → verbose, can't be used inline in JSX.
- Missing fallback: `messages[status]` when status is unknown → `undefined` → renders nothing. Always add `|| fallback`.

---

## Null and Falsy Values in JSX

**What:** React renders `false`, `null`, `undefined`, and `true` as nothing (empty). But `0` and `NaN` ARE rendered.

```jsx
function Example({ count, name }) {
  return (
    <div>
      {false}        // renders nothing ✓
      {null}         // renders nothing ✓
      {undefined}    // renders nothing ✓
      {true}         // renders nothing ✓
      {0}            // renders "0" ⚠️
      {NaN}          // renders "NaN" ⚠️
      {""}           // renders nothing ✓ (empty string)

      // Safe patterns:
      {count > 0 && <p>{count} items</p>}  // ✓ no "0" shown
      {name && <p>Hello, {name}</p>}       // ✓ empty string is falsy
    </div>
  );
}
```

**Why it exists:** React intentionally renders `false`/`null`/`undefined` as nothing so you can use `&&` for conditional rendering. But `0` is rendered because it's a valid number that users might want to display.

**Where it's used:** Every conditional rendering pattern — understanding what React shows vs. hides is fundamental.

**What goes wrong without it:**
- `{count && <p>{count}</p>}` when count is 0 → renders "0" on screen. Fix: `{count > 0 && ...}`.
- `{items.length && <List items={items} />}` when empty → renders "0". Fix: `{items.length > 0 && ...}`.
- Returning `undefined` from a component → React may warn. Always return `null` explicitly.
