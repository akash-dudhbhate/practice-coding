# Lesson 12 — Debug Exercises

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
