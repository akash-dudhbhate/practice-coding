# Lesson 10 — Intuition Checks

## Check 01: Custom hook naming
Why must custom hooks start with `use`?
<details><summary>Answer</summary>
React's linter checks for the `use` prefix to enforce Rules of Hooks. Also signals to other developers that it's a hook.
</details>

## Check 02: Rules of Hooks
What are the two rules?
<details><summary>Answer</summary>
1. Only call hooks at the top level (not in loops, conditions, nested functions).
2. Only call hooks from React functions (components or other hooks).
</details>

## Check 03: Hook composition
```jsx
function useUserData(id) {
  const user = useUser(id);
  const posts = usePosts(user?.id);
  return { user, posts };
}
```
<details><summary>Answer</summary>
Custom hooks can call other hooks. This is composition — building complex logic from simpler hooks.
</details>

## Check 04: Return value
```jsx
function useToggle() {
  const [on, setOn] = useState(false);
  return [on, setOn]; // array
}
// or
function useToggle() {
  const [on, setOn] = useState(false);
  return { on, toggle: () => setOn(!on) }; // object
}
```
<details><summary>Answer</summary>
Both work. Array return (like useState) allows renaming. Object return is more explicit. Choose based on usage.
</details>

## Check 05: Hook reusability
What makes a good custom hook?
<details><summary>Answer</summary>
Reusable logic, clear interface (params and return), handles its own state/effects, composable with other hooks. Examples: useFetch, useLocalStorage, useDebounce.
</details>
