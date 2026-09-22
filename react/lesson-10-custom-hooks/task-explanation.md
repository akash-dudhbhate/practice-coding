# Lesson 10 — Custom Hooks

## What you'll learn
- Creating custom hooks (reusable logic)
- Rules of custom hooks (use prefix, top-level calls)
- useFetch hook (data fetching with loading/error)
- useLocalStorage hook (persistent state)
- useDebounce hook (delay rapid changes)
- useToggle hook (boolean state)
- useEventListener hook (event cleanup)
- Composing custom hooks

## Lesson

### Custom hook structure
```jsx
function useSomething(initial) {
    const [value, setValue] = useState(initial);
    useEffect(() => { /* logic */ }, [deps]);
    return value;
}
```

### useFetch
```jsx
const { data, loading, error } = useFetch("/api/users");
```

### useDebounce
```jsx
const debouncedQuery = useDebounce(query, 500);
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create a `useToggle` hook that returns `{value, toggle, setTrue, setFalse}`. Use it in a component to show/hide a text.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-----------+
   | [ Hide ]  |                 <- button toggles
   +-----------+
   Toggle content visible!       <- <p> appears/disappears
   ```
2. `easy/p02-solve.jsx` — Create a `useCounter` hook that returns `{count, increment, decrement, reset}`. Use it in a component with buttons.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Count: 1                              <- <p>
   +-----+ +-----+ +-------+
   | +1  | | -1  | | Reset |
   +-----+ +-----+ +-------+
   ```
3. `easy/p03-solve.jsx` — Create a `useWindowSize` hook that returns `{width, height}`. Display the window size and update on resize.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Window: 1024 x 768            <- <p> updates live on resize
   ```

### Medium
4. `medium/p01-solve.jsx` — Create a `useFetch` hook that takes a URL and returns `{data, loading, error}`. Use it to fetch and display data from a public API (e.g., JSONPlaceholder).

   WHAT IT SHOULD LOOK LIKE:
   ```
   Loading...    ->    Leanne Graham       <- name
                       Sincere@april.biz   <- email
   ```
5. `medium/p02-solve.jsx` — Create a `useLocalStorage` hook that syncs state with localStorage. Use it to persist a theme (light/dark) and a username across page reloads.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------+
   | ############################ |   <- dark div when theme=dark
   | [ Toggle theme ]             |
   | Name: [ Akash___________ ]   |
   +------------------------------+
   (theme + name survive a page reload)
   ```
6. `medium/p03-solve.jsx` — Create a `useDebounce` hook. Use it in a search component that only fetches results 500ms after the user stops typing.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | lean                 |    <- fetch fires ~500ms after
   +----------------------+       typing stops (once!)
   * Leanne Graham
   * Leanne Smith                 <- results <ul>
   ```

### Hard
7. `hard/p01-solve.jsx` — Create a `useEventListener` hook that attaches/detaches event listeners with cleanup. Use it for: Escape key to close modal, click outside to close dropdown, and scroll position tracking.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------+
   |         +----------------+   |
   |         |  MODAL         |   |   <- modal; Escape closes it
   |         |  [x]           |   |
   |         +----------------+   |
   +------------------------------+
   CONSOLE: scrollY: 320 ...      <- scroll tracking
   ```
8. `hard/p02-solve.jsx` — Create a `useForm` hook that manages form state: values, errors, handleChange, handleSubmit, validate. Use it in a registration form with name, email, password, and confirm password fields.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Name:     [_______________]  Name is required      <- red
   Email:    [a@b.com________]
   Password: [***************]
   Confirm:  [*******________]  Passwords must match  <- red
   [ Register ]   -> alert "Registered: <name>" when valid
   ```
9. `hard/p03-solve.jsx` — Compose multiple hooks: create `useUserDashboard` that uses `useFetch` (user data), `useDebounce` (search), and `useLocalStorage` (preferences). Display a dashboard with user info, search, and saved preferences.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------------+
   | DASHBOARD (dark theme)  [Toggle ]  |   <- theme persists
   | User: Leanne Graham                |   <- useFetch card
   | Email: Sincere@april.biz           |
   | Search: [erv_______________]       |   <- debounced
   |   * Ervin Howell                   |   <- results list
   +------------------------------------+
   ```

### How to work
- Write your complete React hook + component solution.
- Remove the TODO comment when done.
- Test by importing into a React app or using a sandbox.
