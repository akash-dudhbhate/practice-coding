# Lesson 10 — Approach Comparison

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
