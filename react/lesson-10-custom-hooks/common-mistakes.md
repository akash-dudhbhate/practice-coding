# Lesson 10 — Common Mistakes

## Mistake 01: Not starting with "use"
```jsx
// WRONG — linter won't check it
function fetchData() { useState(...); }
// CORRECT
function useFetchData() { useState(...); }
```

## Mistake 02: Conditional hooks
```jsx
// WRONG — violates Rules of Hooks
if (enabled) useState(0);
// CORRECT — always call, conditionally use
const [state, setState] = useState(0);
if (!enabled) return null;
```

## Mistake 03: Hooks outside components
```jsx
// WRONG — can't call at module level
const data = useFetch("/api");
// CORRECT — call inside component
function App() { const data = useFetch("/api"); }
```

## Mistake 04: Not returning values
```jsx
// WRONG — useless hook
function useCounter() {
  const [count, setCount] = useState(0);
}
// CORRECT
function useCounter() {
  const [count, setCount] = useState(0);
  return { count, increment: () => setCount(c => c + 1) };
}
```

## Mistake 05: Mixing concerns
```jsx
// WRONG — hook does too much
function useEverything() {
  // auth, data fetching, UI state, analytics
}
// BETTER — separate hooks
function useAuth() { ... }
function useData() { ... }
```
