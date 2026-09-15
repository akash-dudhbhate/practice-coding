# Lesson 09 — Common Mistakes

## Mistake 01: Overusing useMemo
```jsx
// WRONG — useMemo overhead > computation cost
const sum = useMemo(() => a + b, [a, b]);
// CORRECT — just compute it
const sum = a + b;
```

## Mistake 02: Missing dependencies
```jsx
// WRONG — stale value
const data = useMemo(() => filter(items, query), [items]);
// CORRECT
const data = useMemo(() => filter(items, query), [items, query]);
```

## Mistake 03: useCallback without memoized child
```jsx
// WRONG — no benefit if child isn't memoized
const handleClick = useCallback(() => {}, []);
<MyComponent onClick={handleClick} /> // not wrapped in React.memo
```

## Mistake 04: Using useMemo for side effects
```jsx
// WRONG — useMemo is for computing values, not side effects
const data = useMemo(() => { fetchData(); }, []);
// CORRECT — use useEffect
useEffect(() => { fetchData(); }, []);
```

## Mistake 05: Recreating objects every render
```jsx
// WRONG — new object every render
<Component style={{ color: "red" }} />
// CORRECT — stable reference
const style = useMemo(() => ({ color: "red" }), []);
<Component style={style} />
```
