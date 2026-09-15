# Lesson 02 — Intuition Checks

## Check 01: useState returns
```jsx
const [state, setState] = useState(0);
```
What are the two elements of the array?
<details><summary>Answer</summary>
`state` — current value. `setState` — function to update it. Array destructuring assigns names.
</details>

## Check 02: Async state updates
```jsx
const [count, setCount] = useState(0);
const handleClick = () => {
  setCount(1);
  console.log(count); // ?
};
```
<details><summary>Answer</summary>
Prints `0` — state updates are async. `count` doesn't change until re-render. Use the value passed to setCount or useEffect.
</details>

## Check 03: Functional updates
```jsx
setCount(count + 1);  // A
setCount(c => c + 1); // B
```
<details><summary>Answer</summary>
A uses the current `count` from closure (may be stale). B uses the latest state from React. Use B when updating based on previous state.
</details>

## Check 04: Object state
```jsx
setUser({ name: "B" }); // What happens to age?
```
<details><summary>Answer</summary>
`age` is lost — `setUser` replaces the entire object, doesn't merge. Use spread: `setUser({ ...user, name: "B" })`.
</details>

## Check 05: Initial state function
```jsx
const [data, setData] = useState(() => expensiveComputation());
```
<details><summary>Answer</summary>
Lazy initialization — function runs only on first render. Use when initial state is expensive to compute. Without `() =>`, it runs on every render.
</details>
