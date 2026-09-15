# Lesson 09 — Approach Comparison

## Problem: Expensive Calculation

### Approach 1: useMemo
```jsx
const result = useMemo(() => expensiveCalc(data), [data]);
```

### Approach 2: Compute every render
```jsx
const result = expensiveCalc(data);
```

**Winner:** Approach 1 — only when calculation is actually expensive. Measure first.

---

## Problem: Callback to Memoized Child

### Approach 1: useCallback
```jsx
const handleClick = useCallback(() => { ... }, [deps]);
<MemoizedChild onClick={handleClick} />
```

### Approach 2: Regular function
```jsx
const handleClick = () => { ... };
<MemoizedChild onClick={handleClick} />
```

**Winner:** Approach 1 — prevents child re-render when only the callback reference changes.
