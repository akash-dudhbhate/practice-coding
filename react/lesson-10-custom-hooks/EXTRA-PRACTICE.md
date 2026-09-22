# lesson-10-custom-hooks — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Hook Outside Component
```jsx
function useCounter() { ... }
const count = useCounter(); // at module level
```
<details><summary>Answer</summary>
**Bug:** Hooks can only be called inside components or other hooks.
**Fix:** Call inside a component: `function App() { const count = useCounter(); }`.
</details>

## Debug 02 (Medium): Conditional Hook
```jsx
function useData(enabled) {
  if (enabled) {
    const [data, setData] = useState(null);
  }
}
```
<details><summary>Answer</summary>
**Bug:** Hooks can't be conditional — violates Rules of Hooks.
**Fix:** Always call the hook, conditionally use the value: `const [data, setData] = useState(null); if (!enabled) return null;`.
</details>

## Debug 03 (Hard): Hook Not Returning Value
```jsx
function useFetch(url) {
  useEffect(() => {
    fetch(url).then(setData);
  }, [url]);
}
```
<details><summary>Answer</summary>
**Bug:** Hook doesn't return anything. Useless to caller.
**Fix:** `return { data, loading, error };`.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Logic in Component
### Before
```jsx
function Component() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => { fetch(url).then(r => r.json()).then(setData).finally(() => setLoading(false)); }, []);
}
```
### After
```jsx
function Component() {
  const { data, loading } = useFetch(url);
}
```

## Refactor 02 (Medium): Hook Returns Too Much
### Before
```jsx
const { data, loading, error, refetch, setData, setError, lastUpdated } = useApi();
```
### After
```jsx
const { data, loading, error, refetch } = useApi();
// internal state stays internal
```

## Refactor 03 (Hard): No Hook Reuse
### Before
```jsx
function UserProfile() {
  const [user, setUser] = useState(null);
  useEffect(() => { fetchUser(id).then(setUser); }, [id]);
}
function PostAuthor({ postId }) {
  const [post, setPost] = useState(null);
  const [author, setAuthor] = useState(null);
  useEffect(() => { fetchPost(postId).then(p => { setPost(p); fetchUser(p.authorId).then(setAuthor); }); }, [postId]);
}
```
### After
```jsx
const useFetch = (url) => { /* generic fetch hook */ };
function UserProfile() { const { data: user } = useFetch(`/users/${id}`); }
```

---

## Approach Comparison — different ways to solve it

## Problem: Fetch Data

### Approach 1: useEffect in component
```jsx
function Component() {
  const [data, setData] = useState(null);
  useEffect(() => { fetch(url).then(setData); }, [url]);
}
```

### Approach 2: Custom hook
```jsx
function Component() {
  const { data, loading } = useFetch(url);
}
```

**Winner:** Approach 2 — reusable, cleaner component, testable hook.

---

## Problem: Hook Return Style

### Approach 1: Array
```jsx
const [on, toggle] = useToggle();
```

### Approach 2: Object
```jsx
const { on, toggle } = useToggle();
```

**Winner:** Array for 2 values (like useState). Object for 3+ values or when order isn't obvious.
