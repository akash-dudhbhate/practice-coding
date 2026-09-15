# Lesson 17 — Concepts Explained (Zustand State Management)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Zustand?

**What:** Zustand is a small, fast, and scalable state management library for React. It uses a simple store with no boilerplate.

```jsx
import { create } from 'zustand';

// Create a store
const useCounterStore = create((set) => ({
    count: 0,
    increment: () => set((state) => ({ count: state.count + 1 })),
    decrement: () => set((state) => ({ count: state.count - 1 })),
    reset: () => set({ count: 0 }),
}));

// Use it in any component — no Provider needed!
function Counter() {
    const count = useCounterStore((state) => state.count);
    const increment = useCounterStore((state) => state.increment);

    return (
        <>
            <p>{count}</p>
            <button onClick={increment}>+</button>
        </>
    );
}
```

**Why it exists:** Without Zustand, you use Context + useReducer (verbose, all consumers re-render) or Redux (lots of boilerplate: actions, reducers, dispatch, providers). Zustand is minimal — one store, one hook, no provider.

**Where it's used:** App-wide state — auth, cart, theme, notifications. Any state shared across multiple components.

**What goes wrong without it:**
- Forgetting to install: `npm install zustand`.
- Calling `set` without the function form: `set({ count: 5 })` → works but doesn't have access to previous state. Use `set((state) => ({ count: state.count + 1 }))` for updates based on previous state.
- Selecting the entire store: `const store = useCounterStore()` → re-renders on ANY state change. Select only what you need.

---

## Selectors (Performance)

**What:** Selectors pick specific pieces of state → component only re-renders when that piece changes.

```jsx
// BAD: selects entire store → re-renders on any change
const store = useCounterStore();
const count = store.count;
const increment = store.increment;

// GOOD: selects only what's needed → re-renders only when count changes
const count = useCounterStore((state) => state.count);
const increment = useCounterStore((state) => state.increment);

// Multiple values with shallow comparison
import { shallow } from 'zustand/shallow';
const { count, increment } = useCounterStore(
    (state) => ({ count: state.count, increment: state.increment }),
    shallow
);
```

**Why it exists:** Without selectors, every state change re-renders all consuming components → performance issues. Selectors ensure components only re-render when their specific data changes.

**Where it's used:** Every Zustand store usage — always select only what you need.

**What goes wrong without it:**
- Selector returning a new object every time: `(state) => ({ a: state.a, b: state.b })` → new reference → re-renders every state change. Use `shallow` comparator.
- Selector with complex logic → runs on every state change → can be slow. Keep selectors simple.
- Selecting a function: `(state) => state.increment` → stable reference (set once) → never causes re-render. Safe to select functions.

---

## Store with Async Actions

**What:** Zustand stores can have async actions (API calls).

```jsx
const useUserStore = create((set, get) => ({
    user: null,
    loading: false,
    error: null,

    fetchUser: async (userId) => {
        set({ loading: true, error: null });
        try {
            const response = await fetch(`/api/users/${userId}`);
            const user = await response.json();
            set({ user, loading: false });
        } catch (error) {
            set({ error: error.message, loading: false });
        }
    },

    // Access current state with get()
    updateUser: (updates) => {
        const currentUser = get().user;
        if (!currentUser) return;
        set({ user: { ...currentUser, ...updates } });
    },
}));
```

**Why it exists:** Without async support in the store, you'd manage loading/error states in components → scattered. Zustand centralizes async logic in the store → components stay simple.

**Where it's used:** Data fetching, auth flows, any async operation that updates global state.

**What goes wrong without it:**
- Forgetting `set` after async operation → state doesn't update → UI stale.
- `get()` → access current state outside of `set`. Useful for reading state in actions without depending on stale closures.
- No error handling → unhandled promise rejection → silent failure. Always try/catch async actions.

---

## Multiple Slices

**What:** Organize a large store into slices (separate create functions merged together).

```jsx
const createCounterSlice = (set) => ({
    count: 0,
    increment: () => set((state) => ({ count: state.count + 1 })),
    decrement: () => set((state) => ({ count: state.count - 1 })),
});

const createAuthSlice = (set) => ({
    user: null,
    login: (user) => set({ user }),
    logout: () => set({ user: null }),
});

const createThemeSlice = (set) => ({
    theme: 'light',
    toggleTheme: () => set((state) => ({
        theme: state.theme === 'light' ? 'dark' : 'light',
    })),
});

// Combine slices into one store
const useStore = create((...a) => ({
    ...createCounterSlice(...a),
    ...createAuthSlice(...a),
    ...createThemeSlice(...a),
}));

// Usage — all slices available in one store
function Component() {
    const count = useStore((s) => s.count);
    const user = useStore((s) => s.user);
    const theme = useStore((s) => s.theme);
    // ...
}
```

**Why it exists:** Without slices, a large store is one giant object → hard to maintain. Slices split it by concern → each slice is small and focused → easier to test and understand.

**Where it's used:** Medium to large apps with multiple state domains (auth, cart, theme, notifications).

**What goes wrong without it:**
- Slice actions can't call each other directly → they don't know about other slices. Use `get()` to access cross-slice state.
- Naming collisions: two slices with `loading` → one overwrites the other. Prefix names: `authLoading`, `cartLoading`.
- Over-slicing → too many tiny slices → overhead. Group related state.

---

## Persisting State (localStorage)

**What:** Save store state to localStorage → persists across page reloads.

```jsx
import { persist } from 'zustand/middleware';

const useCartStore = create(
    persist(
        (set) => ({
            items: [],
            addItem: (item) => set((state) => ({
                items: [...state.items, item],
            })),
            removeItem: (id) => set((state) => ({
                items: state.items.filter(item => item.id !== id),
            })),
            clear: () => set({ items: [] }),
        }),
        {
            name: 'cart-storage',  // localStorage key
            // Only persist specific fields
            partialize: (state) => ({ items: state.items }),
        }
    )
);
// Cart items survive page reload
```

**Why it exists:** Without persistence, cart/theme/preferences are lost on reload → bad UX. `persist` middleware automatically saves and restores state → seamless.

**Where it's used:** Shopping carts, theme preferences, user settings, auth tokens, recently viewed items.

**What goes wrong without it:**
- Persisting everything → large localStorage → slow. Use `partialize` to persist only what's needed.
- Functions are NOT persisted (only state). Don't worry — actions are recreated on each load.
- SSR (Next.js): localStorage is not available on server → hydration mismatch. Use `skipHydration: true` and hydrate manually.

---

## Middleware (devtools, immer)

**What:** Zustand supports middleware to enhance stores.

```jsx
import { devtools, immer } from 'zustand/middleware';

// Devtools: Redux DevTools integration
const useStore = create(
    devtools(
        (set) => ({
            count: 0,
            increment: () => set((state) => ({ count: state.count + 1 })),
        }),
        { name: 'CounterStore' }  // shows in DevTools
    )
);

// Immer: mutate state directly (no spread needed)
const useTodoStore = create(
    immer((set) => ({
        todos: [],
        addTodo: (text) => set((state) => {
            state.todos.push({ id: Date.now(), text, done: false });  // direct mutation!
        }),
        toggleTodo: (id) => set((state) => {
            const todo = state.todos.find(t => t.id === id);
            if (todo) todo.done = !todo.done;  // direct mutation!
        }),
    }))
);
```

**Why it exists:** Devtools → debug state changes in Redux DevTools extension. Immer → write mutable-looking code that's actually immutable → cleaner for nested updates.

**Where it's used:** Devtools in development (remove in production). Immer for complex nested state (todos, trees, deeply nested objects).

**What goes wrong without it:**
- Devtools in production → performance overhead. Conditionally enable: `process.env.NODE_ENV === 'development'`.
- Immer: can't return nothing from `set` with immer. Must either mutate OR return a new state, not both.
- Middleware order matters: `persist(devtools(immer(...)))` → outer wraps inner. Order affects behavior.

---

## Zustand vs Context vs Redux

**What:** When to use which:

| Zustand | Context | Redux |
|---------|---------|-------|
| Small, fast, no provider | Built-in, no library | Mature, ecosystem |
| Selectors prevent re-renders | All consumers re-render on change | Fine-grained selectors |
| Simple API | Verbose for complex state | Lots of boilerplate |
| Good for medium apps | Good for simple global state | Good for large apps |

**Why it exists:** Each has trade-offs. Zustand hits a sweet spot: simpler than Redux, more performant than Context (selectors), no provider needed.

**Where it's used:** Zustand for most apps. Context for simple state (theme). Redux for very large apps with complex state interactions.

**What goes wrong without it:**
- Using Context for frequently changing state → all consumers re-render → performance issues. Use Zustand.
- Using Redux for simple state → over-engineering → unnecessary complexity. Use Zustand.
- Mixing Zustand and Context → confusing. Pick one for global state.
