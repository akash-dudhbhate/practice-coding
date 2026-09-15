# Lesson 06 — useEffect & Side Effects

## What you'll learn
- What side effects are and why they don't belong in the render phase.
- How to use the `useEffect` hook to run code after render.
- How the dependency array controls when effects re-run.
- How to clean up side effects (timers, listeners) to prevent memory leaks.

## Lesson

`useEffect` runs a function AFTER the component renders, letting you perform side effects safely.

```jsx
import { useState, useEffect } from "react";

function DataFetcher() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/api/data")
      .then(res => res.json())
      .then(setData);
  }, []); // empty array = run once on mount

  if (!data) return <p>Loading...</p>;
  return <div>{data.name}</div>;
}
```

### Dependency array patterns
- `[]` — run once on mount.
- `[dep]` — run on mount + when `dep` changes.
- No array — run on every render (rarely what you want).

### Key rules
- **Always clean up** timers, listeners, and subscriptions in the return function.
- **Use functional updates** in timers: `setCount(prev => prev + 1)`, not `setCount(count + 1)`.
- **Never call `useEffect` conditionally** — hooks must run in the same order every render.
- **Include all dependencies** the effect uses — missing deps cause stale closures.
- **Don't lie to the linter** — if you use a variable in the effect, put it in the deps array.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.jsx` — **Document Title Updater:** Update `document.title` to show the current count. Effect runs when count changes. Practice `useEffect` with a dependency.
2. `easy/p02-solve.jsx` — **Mount Message:** Log "Component mounted" to console once when the component appears. Practice `useEffect` with empty dependency array.
3. `easy/p03-solve.jsx` — **Window Width Tracker:** Track and display the window width. Add resize listener in `useEffect`, clean up on unmount. Practice event listener + cleanup.

### Medium
4. `medium/p01-solve.jsx` — **Fetch User on Mount:** Fetch user data from an API (use a mock function or `jsonplaceholder`). Show loading state, then data. Practice fetch-on-mount pattern.
5. `medium/p02-solve.jsx` — **Countdown Timer:** A countdown from 10 to 0 using `setInterval`. Clean up the interval on unmount and when countdown reaches 0. Practice timer + cleanup.
6. `medium/p03-solve.jsx` — **Re-fetch on Prop Change:** Fetch user data when `userId` prop changes. Show different user data when the prop updates. Practice effect with dependency.

### Hard
7. `hard/p01-solve.jsx` — **Live Search with Debounce:** Search input that debounces API calls (wait 500ms after typing stops). Clean up the timeout on each keystroke. Practice timer cleanup + dependency.
8. `hard/p02-solve.jsx` — **Mouse Position Tracker:** Track mouse X/Y position globally. Add `mousemove` listener in effect, clean up on unmount. Show coordinates and a dot following the cursor.
9. `hard/p03-solve.jsx` — **Multiple Effects Chat:** A chat component with 3 effects: fetch messages on room change, update document title, set up a mock WebSocket with cleanup. Practice multiple effects with different dependencies.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete component from scratch** below the TODO marker.
- Remove the TODO line when done.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
