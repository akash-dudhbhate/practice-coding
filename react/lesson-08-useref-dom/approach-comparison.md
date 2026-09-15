# Lesson 08 — Approach Comparison

## Problem: Focus Input on Mount

### Approach 1: useRef + useEffect
```jsx
const inputRef = useRef();
useEffect(() => { inputRef.current.focus(); }, []);
return <input ref={inputRef} />;
```

### Approach 2: autoFocus attribute
```jsx
<input autoFocus />
```

**Winner:** Approach 2 for simple cases. Approach 1 for conditional focus.

---

## Problem: Store Previous Value

### Approach 1: useRef
```jsx
const prevRef = useRef();
useEffect(() => { prevRef.current = value; });
```

### Approach 2: Custom hook
```jsx
const prevValue = usePrevious(value);
```

**Winner:** Approach 2 — reusable, encapsulated.
