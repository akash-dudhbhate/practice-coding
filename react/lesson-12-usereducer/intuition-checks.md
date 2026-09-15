# Lesson 12 — Intuition Checks

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
