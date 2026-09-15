# Lesson 17 — Zustand State Management

## What you'll learn
- Zustand basics (create store, use store)
- Selectors (performance optimization)
- Async actions in stores
- Multiple slices (organizing large stores)
- Persisting state (localStorage middleware)
- Middleware (devtools, immer)
- Zustand vs Context vs Redux

## Lesson

### Create store
```jsx
const useStore = create((set) => ({
    count: 0,
    increment: () => set((s) => ({ count: s.count + 1 })),
}));
```

### Use with selector
```jsx
const count = useStore((s) => s.count);
const increment = useStore((s) => s.increment);
```

### Persist
```jsx
const useStore = create(persist((set) => ({...}), { name: 'storage' }));
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create a counter store with `count`, `increment`, `decrement`, `reset`. Use it in a component with selectors. No Provider needed.
2. `easy/p02-solve.jsx` — Create a theme store with `theme` ("light"/"dark") and `toggleTheme`. Use it in 3 components (header, main, footer) — each reads only `theme`.
3. `easy/p03-solve.jsx` — Create a todo store with `todos` array, `addTodo`, `toggleTodo`, `deleteTodo`. Display the list and a form to add todos.

### Medium
4. `medium/p01-solve.jsx` — Create an auth store with async `login(username, password)` and `logout()`. Include `user`, `loading`, and `error` states. Use in a login form and a protected component.
5. `medium/p02-solve.jsx` — Create a cart store with `items`, `addItem`, `removeItem`, `updateQuantity`, `clearCart`, and a computed `total` (use `get()` or calculate in component). Display cart with total.
6. `medium/p03-solve.jsx` — Create a store with `persist` middleware: save theme and user preferences to localStorage. Reload the page → state survives. Use `partialize` to persist only specific fields.

### Hard
7. `hard/p01-solve.jsx` — Create a multi-slice store: `createAuthSlice`, `createCartSlice`, `createThemeSlice`. Combine them. Components consume different slices independently. Show that updating one slice doesn't re-render components selecting other slices.
8. `hard/p02-solve.jsx` — Create a store with `immer` middleware for a nested tree structure (e.g., file system with folders and files). Actions: addFolder, addFile, rename, delete, move. Use direct mutation syntax (no spread).
9. `hard/p03-solve.jsx` — Build a complete e-commerce store: products (fetched), cart, auth, wishlist, notifications. Use slices, persist (cart + wishlist), devtools middleware. Multiple components consume different parts efficiently.

### How to work
- Write your complete React solution.
- Remove the TODO comment when done.
- Test by importing into a React app with zustand installed.
