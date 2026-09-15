# Lesson 06 — Concepts Explained (useEffect & Side Effects)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Side Effects in React

**What:** A side effect is anything that affects something OUTSIDE the component — fetching data, setting up subscriptions, timers, manually changing the DOM, reading from localStorage. React components should be "pure" (same input → same output). Side effects don't belong in the render phase.

```jsx
// PURE — no side effects, just computes UI
function Greeting({ name }) {
  return <h1>Hello, {name}</h1>;
}

// SIDE EFFECT — fetches data from an API (affects outside world)
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data));
  }, [userId]);
  return <h1>{user?.name}</h1>;
}
```

**Why it exists:** React's render phase must be pure — no API calls, no DOM mutations, no timers during render. If side effects ran during render, they'd run on EVERY render (causing infinite loops with state updates), and React couldn't optimize rendering. `useEffect` separates side effects from rendering.

**Where it's used:** Data fetching, event subscriptions (WebSocket, resize listener), timers (setInterval, setTimeout), localStorage read/write, document title updates, analytics tracking.

**What goes wrong without it:**
- Fetching in render body → runs on every render → infinite loop (fetch → setState → re-render → fetch → ...).
- Setting timers in render → new timer created on every render → memory leak, dozens of timers running.
- Direct DOM manipulation in render → conflicts with React's virtual DOM, inconsistent UI.

---

## useEffect Hook

**What:** `useEffect` runs a function AFTER the component renders. It lets you perform side effects without blocking rendering.

```jsx
useEffect(() => {
  // This runs AFTER every render (by default)
  document.title = `Count: ${count}`;
});
```

The effect function runs after the browser paints the screen, so the user sees the UI first, then the effect runs.

**Why it exists:** Components need to interact with the outside world (APIs, timers, DOM). `useEffect` provides a safe place for this — after render, not during. It also provides cleanup (returning a function) to undo side effects when the component unmounts.

**Where it's used:** Every component that needs to fetch data, set up listeners, run timers, or interact with browser APIs.

**What goes wrong without it:**
- Side effects in render → infinite loops, crashes, performance issues.
- Forgetting the dependency array → effect runs on EVERY render → unnecessary work, potential infinite loops if the effect sets state.
- Calling `useEffect` conditionally → React tracks hooks by call order. Skipping a hook breaks all subsequent hooks.

---

## Dependency Array

**What:** The second argument to `useEffect` is an array of dependencies. The effect only re-runs when one of these values changes.

```jsx
// Runs once on mount (empty array)
useEffect(() => {
  console.log("Component mounted");
}, []);

// Runs when count changes
useEffect(() => {
  document.title = `Count: ${count}`;
}, [count]);

// Runs on every render (no array)
useEffect(() => {
  console.log("Every render");
});
```

**Why it exists:** Without the dependency array, effects run on every render — wasteful and often causes infinite loops. The array tells React: "only re-run this effect when these specific values change." Empty array = run once (on mount).

**Where it's used:** Every `useEffect` call. You must decide what triggers the effect.

**What goes wrong without it:**
- No dependency array → effect runs on every render → if it sets state → infinite loop.
- Empty array but effect uses props/state → stale closure (effect captures old values, never updates).
- Missing dependency → effect uses old value. React's exhaustive-deps lint rule catches this.
- Including objects/arrays in deps → they're new references every render → effect runs every render anyway. Extract primitive values or memoize.

---

## Effect with Empty Dependencies (Run Once on Mount)

**What:** `useEffect(() => { ... }, [])` runs the effect ONCE when the component mounts, never again.

```jsx
function DataFetcher() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/api/data")
      .then(res => res.json())
      .then(data => setData(data));
  }, []);  // empty array = run once on mount

  if (!data) return <p>Loading...</p>;
  return <div>{data.name}</div>;
}
```

**Why it exists:** Many side effects only need to run once — initial data fetch, setting up a WebSocket connection, adding a global event listener. The empty array tells React "this effect has no dependencies, so it never needs to re-run."

**Where it's used:** Initial API calls, setting up subscriptions, adding window event listeners, initializing third-party libraries.

**What goes wrong without it:**
- Forgetting `[]` → effect runs on every render → fetch called repeatedly → infinite loop if it sets state.
- Using props/state inside `[]` effect → captures initial values (stale closure). If you use `userId` prop, it captures the initial `userId` forever. Add it to deps: `[userId]`.
- No cleanup → event listeners and subscriptions stay active after unmount → memory leaks.

---

## Effect with Dependencies (Re-run on Change)

**What:** `useEffect(() => { ... }, [dep1, dep2])` re-runs the effect whenever one of the listed dependencies changes.

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data));
  }, [userId]);  // re-runs when userId changes

  if (!user) return <p>Loading...</p>;
  return <h1>{user.name}</h1>;
}
```

**Why it exists:** When a side effect depends on a prop or state value, it should re-run when that value changes. If `userId` changes from 1 to 2, you need to fetch user 2's data. Without the dependency, the effect would keep showing user 1's data.

**Where it's used:** Re-fetching when a prop changes, re-subscribing when a parameter changes, updating derived data.

**What goes wrong without it:**
- Missing dependency → stale data. `userId` changes but effect doesn't re-run → shows old user's data.
- Including non-primitive deps (objects, arrays, functions) → new reference every render → effect runs every render. Use `useMemo`/`useCallback` or extract primitive values.
- Too many dependencies → effect runs too often. Split into multiple effects with focused dependencies.

---

## Cleanup Function

**What:** If your `useEffect` returns a function, React calls it before the next effect run AND when the component unmounts. This is for cleanup — removing listeners, clearing timers, canceling requests.

```jsx
useEffect(() => {
  const handleResize = () => console.log("Window resized");
  window.addEventListener("resize", handleResize);

  // Cleanup — runs before next effect and on unmount
  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

**Why it exists:** Every side effect that sets up something (listener, timer, subscription) should tear it down. Without cleanup, listeners accumulate, timers keep running after the component is gone, causing memory leaks and errors.

**Where it's used:** Event listeners (resize, scroll, keydown), timers (setInterval, setTimeout), WebSocket subscriptions, aborting fetch requests.

**What goes wrong without it:**
- No cleanup on event listener → listener stays active after unmount → fires on resize for a component that doesn't exist → errors.
- No cleanup on `setInterval` → timer keeps running after unmount → tries to update state of unmounted component → memory leak warning.
- Cleanup runs BEFORE the next effect, not after → if your effect sets up a new listener, cleanup removes the OLD one first. This prevents duplicate listeners.

---

## Fetch on Mount Pattern

**What:** The most common `useEffect` pattern — fetch data when the component first appears.

```jsx
function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch("/api/users")
      .then(res => {
        if (!res.ok) throw new Error("Failed to fetch");
        return res.json();
      })
      .then(data => {
        setUsers(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;
  return users.map(u => <div key={u.id}>{u.name}</div>);
}
```

**Why it exists:** Almost every page needs to load data. This pattern handles loading, error, and success states cleanly. The effect runs once on mount, fetches data, and updates state.

**Where it's used:** Dashboard pages, list views, profile pages, any component that displays server data.

**What goes wrong without it:**
- No loading state → renders `users.map(...)` before data arrives → `users` is `[]` → renders nothing (or crashes if trying to access properties).
- No error handling → unhandled rejection → app crashes.
- Fetch in render body → runs on every render → infinite loop.
- No cleanup with AbortController → if component unmounts before fetch completes, state update on unmounted component → warning.

---

## Timer Effects with Cleanup

**What:** Setting up intervals or timeouts in `useEffect` with proper cleanup to prevent memory leaks.

```jsx
function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setSeconds(prev => prev + 1);
    }, 1000);

    // CRITICAL — clean up the interval
    return () => clearInterval(interval);
  }, []);

  return <p>Time: {seconds}s</p>;
}
```

**Why it exists:** Timers keep running until cleared. If a component unmounts without clearing its timer, the timer fires forever — trying to update state of a component that no longer exists. This causes memory leaks and React warnings.

**Where it's used:** Countdowns, clocks, auto-refresh data, polling, animations, delayed actions.

**What goes wrong without it:**
- No `clearInterval` in cleanup → timer runs forever after unmount → memory leak, "Can't perform a React state update on an unmounted component" warning.
- `setInterval` without functional update: `setSeconds(seconds + 1)` → captures stale `seconds` (always 0) → timer stays at 1. Use `setSeconds(prev => prev + 1)`.
- Setting up interval in render → new interval on every render → dozens of intervals running simultaneously.

---

## Event Listener Effects

**What:** Adding global event listeners (window, document) in `useEffect` with cleanup.

```jsx
function WindowSize() {
  const [windowSize, setWindowSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
  });

  useEffect(() => {
    const handleResize = () => {
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
    };

    window.addEventListener("resize", handleResize);

    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return <p>Window: {windowSize.width} x {windowSize.height}</p>;
}
```

**Why it exists:** Some events are global (window resize, scroll, keyboard) and need to be listened to at the window/document level. `useEffect` is the place to add them, and cleanup removes them when the component unmounts.

**Where it's used:** Window resize tracking, scroll events, keyboard shortcuts, mouse position tracking, online/offline detection.

**What goes wrong without it:**
- No `removeEventListener` in cleanup → listener stays active after unmount → fires for components that don't exist → errors, memory leaks.
- Adding listener in render → new listener on every render → hundreds of listeners → performance disaster.
- Inline function in addEventListener: `window.addEventListener("resize", () => ...)` → can't remove it (different function reference). Always store the handler in a variable.

---

## Multiple Effects

**What:** A component can have multiple `useEffect` calls, each managing a different side effect.

```jsx
function ChatApp({ roomId }) {
  const [messages, setMessages] = useState([]);

  // Effect 1: fetch messages when room changes
  useEffect(() => {
    fetch(`/api/rooms/${roomId}/messages`)
      .then(res => res.json())
      .then(setMessages);
  }, [roomId]);

  // Effect 2: update document title
  useEffect(() => {
    document.title = `Room: ${roomId}`;
  }, [roomId]);

  // Effect 3: set up WebSocket connection
  useEffect(() => {
    const ws = new WebSocket(`wss://api/rooms/${roomId}`);
    ws.onmessage = (e) => setMessages(prev => [...prev, JSON.parse(e.data)]);
    return () => ws.close();
  }, [roomId]);

  return messages.map(m => <div key={m.id}>{m.text}</div>);
}
```

**Why it exists:** Different side effects have different dependencies and lifecycles. Splitting them into separate `useEffect` calls keeps each effect focused, makes cleanup easier, and prevents unnecessary re-runs.

**Where it's used:** Any component with multiple side effects — data fetching + subscriptions, timers + event listeners, analytics + DOM updates.

**What goes wrong without it:**
- One giant effect doing everything → runs all side effects when any dependency changes → wasteful.
- Mixing unrelated cleanup logic → hard to maintain, easy to forget a cleanup.
- Effects must be called unconditionally (top-level) — never inside conditions. Use the dependency array to control when they run.
