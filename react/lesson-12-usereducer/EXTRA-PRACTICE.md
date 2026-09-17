# lesson-12-usereducer — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: useReducer vs useState
When should you use useReducer?
<details><summary>Answer</summary>
When: state has multiple related values, next state depends on previous, complex update logic, you want testable state transitions. Use useState for simple independent values.
</details>

## Check 02: Reducer signature
```jsx
function reducer(state, action) { ... return newState; }
const [state, dispatch] = useReducer(reducer, initialState);
```
<details><summary>Answer</summary>
Reducer: (currentState, action) => newState. Must be pure. dispatch: sends action to reducer.
</details>

## Check 03: Action types
```jsx
dispatch({ type: "increment" });
dispatch({ type: "add", payload: item });
```
<details><summary>Answer</summary>
Actions are objects with `type` (required) and optional payload. Convention: type as string constant, payload for data.
</details>

## Check 04: Immutability
```jsx
return { ...state, count: state.count + 1 };
```
<details><summary>Answer</summary>
Must return NEW object, not mutate. Spread operator creates new object with updated field. React detects change by reference.
</details>

## Check 05: Lazy initialization
```jsx
const [state, dispatch] = useReducer(reducer, initialArg, init);
```
<details><summary>Answer</summary>
`init` function transforms `initialArg` into initial state. Runs once. Use for expensive initialization.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Reducer Not Returning State
```jsx
function reducer(state, action) {
  if (action.type === "increment") {
    state.count++;
  }
  return state;
}
```
<details><summary>Answer</summary>
**Bug:** Mutating state and returning same object. React won't detect change.
**Fix:** `return { ...state, count: state.count + 1 };`.
</details>

## Debug 02 (Medium): Missing Default Case
```jsx
function reducer(state, action) {
  switch (action.type) {
    case "add": return { ...state, items: [...state.items, action.item] };
  }
}
```
<details><summary>Answer</summary>
**Bug:** No default case — unknown action returns undefined, breaks state.
**Fix:** `default: return state;` (or throw error for unknown actions).
</details>

## Debug 03 (Hard): Async in Reducer
```jsx
function reducer(state, action) {
  if (action.type === "fetch") {
    fetch("/api").then(data => { return { ...state, data }; });
  }
  return state;
}
```
<details><summary>Answer</summary>
**Bug:** Reducers must be pure — no side effects. The fetch promise's return doesn't update state.
**Fix:** Fetch in useEffect, then dispatch result: `dispatch({ type: "success", data })`.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

## Problem: Form with Validation

### Approach 1: Multiple useState
```jsx
const [values, setValues] = useState({});
const [errors, setErrors] = useState({});
const [touched, setTouched] = useState({});
```
**Cons:** Hard to keep in sync, complex update logic.

### Approach 2: useReducer
```jsx
const [state, dispatch] = useReducer(formReducer, {
  values: {}, errors: {}, touched: {}
});
```
**Pros:** Centralized logic, testable, all state transitions in one place.

**Winner:** Approach 2 for complex forms. Approach 1 for simple forms.

---

## Problem: State Management

### Approach 1: useState
```jsx
const [count, setCount] = useState(0);
```

### Approach 2: useReducer
```jsx
const [count, dispatch] = useReducer((s, a) => a === "inc" ? s + 1 : s, 0);
```

**Winner:** Approach 1 — simpler for independent values. Don't over-engineer.
