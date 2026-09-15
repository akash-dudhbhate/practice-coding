# Lesson 10 — Concepts Explained (Custom Hooks)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What are Custom Hooks?

**What:** Custom hooks are reusable functions that start with `use` and contain other hooks. They let you extract component logic into reusable functions.

```jsx
import { useState, useEffect } from 'react';

// Custom hook: reusable window size tracker
function useWindowSize() {
    const [size, setSize] = useState({ width: window.innerWidth, height: window.innerHeight });

    useEffect(() => {
        function handleResize() {
            setSize({ width: window.innerWidth, height: window.innerHeight });
        }
        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, []);

    return size;
}

// Use it in any component
function MyComponent() {
    const { width, height } = useWindowSize();
    return <p>Window: {width} x {height}</p>;
}
```

**Why it exists:** Without custom hooks, you'd copy-paste the same `useState` + `useEffect` logic into every component that needs window size → duplication. Custom hooks extract the logic → one definition, use everywhere.

**Where it's used:** Every React project — data fetching, form handling, localStorage, debounce, media queries, authentication.

**What goes wrong without it:**
- Name must start with `use` → `useWindowSize`, `useFetch`. Without `use` prefix → React's hooks lint rule doesn't recognize it → can't detect hook rule violations.
- Calling hooks conditionally inside a custom hook → same rules apply. Hooks must be called at the top level, not in conditions/loops.
- Custom hooks are NOT components → they don't render JSX. They return values (state, functions, objects).

---

## Rules of Custom Hooks

**What:** Custom hooks follow the same rules as built-in hooks:

1. **Only call hooks at the top level** — not inside conditions, loops, or nested functions.
2. **Only call hooks from React functions** — components or other custom hooks.
3. **Name must start with `use`** — convention that enables linting and tooling.

```jsx
// GOOD: hooks at top level
function useUser(userId) {
    const [user, setUser] = useState(null);
    useEffect(() => { fetchUser(userId).then(setUser); }, [userId]);
    return user;
}

// BAD: hook inside condition
function useUser(userId) {
    if (userId) {                          // WRONG
        const [user, setUser] = useState(null);  // hook in condition
    }
}
```

**Why it exists:** React relies on the ORDER of hook calls to associate state with the right hook. If hooks are called conditionally, the order changes between renders → React loses track → bugs.

**Where it's used:** Every custom hook you write.

**What goes wrong without it:**
- Hook in a condition → "React Hook is called conditionally" warning → state gets mixed up → unpredictable bugs.
- Hook in a loop → number of hooks changes between renders → React crashes.
- Not starting with `use` → ESLint can't enforce rules → silent violations.

---

## useFetch Hook (Data Fetching)

**What:** A reusable hook for API data fetching with loading, error, and data states.

```jsx
function useFetch(url) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        let cancelled = false;
        setLoading(true);
        fetch(url)
            .then(res => {
                if (!res.ok) throw new Error(`HTTP ${res.status}`);
                return res.json();
            })
            .then(data => {
                if (!cancelled) { setData(data); setError(null); }
            })
            .catch(err => {
                if (!cancelled) setError(err.message);
            })
            .finally(() => {
                if (!cancelled) setLoading(false);
            });

        return () => { cancelled = true; };  // prevent state update after unmount
    }, [url]);

    return { data, loading, error };
}

// Usage
function UserProfile({ userId }) {
    const { data: user, loading, error } = useFetch(`/api/users/${userId}`);
    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error}</p>;
    return <h1>{user.name}</h1>;
}
```

**Why it exists:** Without `useFetch`, every component that fetches data repeats the same loading/error/data pattern → 20 lines per component. `useFetch` encapsulates it → one line to use.

**Where it's used:** Every component that fetches API data — user profiles, dashboards, search results, product lists.

**What goes wrong without it:**
- Forgetting the `cancelled` flag → if the component unmounts before fetch completes → `setState` on unmounted component → warning + memory leak.
- No error handling → network errors crash the component. Always handle errors.
- URL as dependency → every URL change triggers a new fetch. If URL is an object → new reference every render → infinite fetches. Use a string or memoize.

---

## useLocalStorage Hook

**What:** Sync state with localStorage — persists across page reloads.

```jsx
function useLocalStorage(key, initialValue) {
    const [value, setValue] = useState(() => {
        try {
            const stored = localStorage.getItem(key);
            return stored ? JSON.parse(stored) : initialValue;
        } catch {
            return initialValue;
        }
    });

    useEffect(() => {
        try {
            localStorage.setItem(key, JSON.stringify(value));
        } catch {
            // localStorage might be full or disabled
        }
    }, [key, value]);

    return [value, setValue];
}

// Usage
function Settings() {
    const [theme, setTheme] = useLocalStorage('theme', 'light');
    return (
        <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
            Theme: {theme}
        </button>
    );
    // Theme persists across page reloads
}
```

**Why it exists:** Without `useLocalStorage`, you'd manually read/write localStorage in every component → repetitive. This hook makes localStorage behave like state → automatic persistence.

**Where it's used:** Theme preferences, user settings, shopping carts, form drafts, recently viewed items.

**What goes wrong without it:**
- `localStorage` is synchronous → reading large data blocks the main thread. Don't store large objects.
- `JSON.parse` on corrupted data → throws. Always wrap in try/catch.
- `localStorage` is not available in SSR (Next.js) → `localStorage is not defined`. Check `typeof window !== 'undefined'`.

---

## useDebounce Hook

**What:** Delay a rapidly changing value until the user stops changing it.

```jsx
function useDebounce(value, delay) {
    const [debouncedValue, setDebouncedValue] = useState(value);

    useEffect(() => {
        const timer = setTimeout(() => {
            setDebouncedValue(value);
        }, delay);

        return () => clearTimeout(timer);  // clear on value change
    }, [value, delay]);

    return debouncedValue;
}

// Usage: search input that only searches after user stops typing
function Search() {
    const [query, setQuery] = useState("");
    const debouncedQuery = useDebounce(query, 500);

    useEffect(() => {
        if (debouncedQuery) {
            fetchResults(debouncedQuery);  // only runs 500ms after last keystroke
        }
    }, [debouncedQuery]);

    return <input value={query} onChange={e => setQuery(e.target.value)} />;
}
```

**Why it exists:** Without debounce, every keystroke triggers a search → 10 requests for "javascript" (j, ja, jav, ...). Debounce waits for the user to stop typing → 1 request for "javascript".

**Where it's used:** Search inputs, auto-save, resize handlers, scroll handlers, any rapidly-firing event.

**What goes wrong without it:**
- Forgetting to clear the timeout → multiple timers running → debounced value updates multiple times. Always `clearTimeout` in the cleanup.
- `delay` in dependency array → if delay changes, timer resets. Usually delay is a constant → fine.
- Debouncing a value that's needed immediately → first render has the non-debounced value. Handle the initial state correctly.

---

## useToggle Hook

**What:** A simple hook for boolean toggle state.

```jsx
function useToggle(initialValue = false) {
    const [value, setValue] = useState(initialValue);

    const toggle = useCallback(() => setValue(v => !v), []);
    const setTrue = useCallback(() => setValue(true), []);
    const setFalse = useCallback(() => setValue(false), []);

    return { value, toggle, setTrue, setFalse };
}

// Usage
function Modal() {
    const { value: isOpen, toggle, setFalse } = useToggle(false);

    return (
        <>
            <button onClick={toggle}>Open/Close</button>
            {isOpen && (
                <div className="modal">
                    <button onClick={setFalse}>Close</button>
                    <p>Modal content</p>
                </div>
            )}
        </>
    );
}
```

**Why it exists:** Without `useToggle`, you write `const [isOpen, setIsOpen] = useState(false)` and `onClick={() => setIsOpen(!isOpen)}` everywhere → repetitive. `useToggle` provides a clean API.

**Where it's used:** Modals, dropdowns, accordions, show/hide toggles, expand/collapse.

**What goes wrong without it:**
- Using `setValue(!value)` instead of `setValue(v => !v)` → stale closure if `value` changed since last render. Always use the functional update form.
- Forgetting `useCallback` on the toggle function → new function every render → breaks `React.memo` children.

---

## useEventListener Hook

**What:** A reusable hook for adding event listeners with cleanup.

```jsx
function useEventListener(eventName, handler, element = window) {
    const savedHandler = useRef(handler);

    useEffect(() => {
        savedHandler.current = handler;  // always have the latest handler
    }, [handler]);

    useEffect(() => {
        if (!element?.addEventListener) return;

        const eventListener = (event) => savedHandler.current(event);
        element.addEventListener(eventName, eventListener);

        return () => element.removeEventListener(eventName, eventListener);
    }, [eventName, element]);
}

// Usage
function App() {
    useEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });
    return <div>Press Escape</div>;
}
```

**Why it exists:** Without this hook, every component that listens to events writes the same add/remove listener boilerplate → repetitive and error-prone (forgetting cleanup → leaks).

**Where it's used:** Keyboard shortcuts, click-outside detection, scroll handlers, resize handlers, mouse tracking.

**What goes wrong without it:**
- Not saving the handler in a ref → the listener uses the initial handler (stale closure) → old state values.
- Forgetting cleanup → listener stays active after unmount → memory leak, state updates on unmounted component.
- `element` could be null (during initial render) → check before adding listener.

---

## Composing Custom Hooks

**What:** Custom hooks can use other custom hooks → composition.

```jsx
function useFetchUser(userId) {
    const { data, loading, error } = useFetch(`/api/users/${userId}`);
    return { user: data, loading, error };
}

function useUserSearch(query) {
    const debouncedQuery = useDebounce(query, 300);
    const { data, loading } = useFetch(`/api/search?q=${debouncedQuery}`);
    return { results: data, loading };
}

// Composing multiple hooks in one component
function UserDashboard({ userId }) {
    const { user, loading: userLoading } = useFetchUser(userId);
    const [searchQuery, setSearchQuery] = useState("");
    const { results, loading: searchLoading } = useUserSearch(searchQuery);

    // ...
}
```

**Why it exists:** Without composition, you'd write one giant hook with all logic → hard to maintain. Composition lets you build complex behavior from simple, focused hooks → modular, testable.

**Where it's used:** Complex features — dashboards, search interfaces, real-time data, multi-step forms.

**What goes wrong without it:**
- Over-composing → hooks calling hooks calling hooks → hard to trace data flow. Keep composition to 2-3 levels.
- Circular dependencies: hook A uses hook B, hook B uses hook A → infinite loop. Design hooks to be one-directional.
- Each composed hook has its own state → multiple independent states. If they need to share state, lift it up or use context.
