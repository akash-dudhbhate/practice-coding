# Lesson 12 — Refactoring Challenges

## Refactor 01 (Easy): useReducer for Simple Toggle
### Before
```jsx
const [state, dispatch] = useReducer((s, a) => a === "toggle" ? !s : s, false);
```
### After
```jsx
const [isOpen, setIsOpen] = useState(false);
```

## Refactor 02 (Medium): Complex useState Logic
### Before
```jsx
const [loading, setLoading] = useState(false);
const [data, setData] = useState(null);
const [error, setError] = useState(null);
function fetch() {
  setLoading(true); setError(null);
  api.get().then(setData).catch(setError).finally(() => setLoading(false));
}
```
### After
```jsx
const [state, dispatch] = useReducer(reducer, { loading: false, data: null, error: null });
function fetch() {
  dispatch({ type: "start" });
  api.get().then(d => dispatch({ type: "success", data: d }))
    .catch(e => dispatch({ type: "error", error: e }));
}
```

## Refactor 03 (Hard): Reducer in Component
### Before
```jsx
function Component() {
  const [state, dispatch] = useReducer((state, action) => { /* 50 lines */ }, initial);
}
```
### After
```jsx
// Extract to separate file
export const reducer = (state, action) => { /* ... */ };
```
