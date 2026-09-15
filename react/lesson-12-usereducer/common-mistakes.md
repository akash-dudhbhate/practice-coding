# Lesson 12 — Common Mistakes

## Mistake 01: Mutating state in reducer
```jsx
// WRONG
state.count++;
return state;
// CORRECT
return { ...state, count: state.count + 1 };
```

## Mistake 02: No default case
```jsx
// WRONG — undefined for unknown action
switch (action.type) {
  case "add": return ...;
}
// CORRECT
switch (action.type) {
  case "add": return ...;
  default: return state;
}
```

## Mistake 03: Side effects in reducer
```jsx
// WRONG — reducer must be pure
function reducer(state, action) {
  if (action.type === "fetch") {
    fetchData(); // side effect!
  }
}
// CORRECT — side effects in useEffect
```

## Mistake 04: Using useReducer for simple state
```jsx
// OVERKILL for a counter
const [count, dispatch] = useReducer(counterReducer, 0);
// SIMPLER
const [count, setCount] = useState(0);
```

## Mistake 05: Not extracting reducer
```jsx
// WRONG — inline reducer, hard to test
const [state, dispatch] = useReducer((state, action) => { ... }, initial);
// CORRECT — extracted, testable
function reducer(state, action) { ... }
```
