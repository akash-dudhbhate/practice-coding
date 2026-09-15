# Lesson 17 — Common Mistakes

## Mistake 01: Selecting entire store
```jsx
// WRONG — re-renders on any change
const { count } = useStore();
// CORRECT — select specific
const count = useStore(s => s.count);
```

## Mistake 02: Mutating state
```jsx
// WRONG
state.count++;
// CORRECT
set(state => ({ count: state.count + 1 }));
```

## Mistake 03: Store inside component
```jsx
// WRONG — recreated every render
function App() {
  const store = create(...);
}
// CORRECT — module level
const useStore = create(...);
```

## Mistake 04: No selector optimization
```jsx
// WRONG — new object every render
const { count, name } = useStore(s => ({ count: s.count, name: s.name }));
// CORRECT — separate selectors
const count = useStore(s => s.count);
const name = useStore(s => s.name);
// or use shallow
const { count, name } = useStore(s => ({ count: s.count, name: s.name }), shallow);
```

## Mistake 05: Not using persist for important state
```jsx
// State lost on refresh
// Use persist middleware for user preferences
```
