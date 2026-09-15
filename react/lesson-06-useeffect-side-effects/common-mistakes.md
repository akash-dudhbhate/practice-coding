# Lesson 06 — Common Mistakes

## Mistake 01: Infinite loop
```jsx
// WRONG — no deps, runs every render
useEffect(() => { setCount(c => c + 1); });
// CORRECT
useEffect(() => { setCount(c => c + 1); }, []);
```

## Mistake 02: Missing dependencies
```jsx
// WRONG — stale data
useEffect(() => { fetch(id); }, []);
// CORRECT
useEffect(() => { fetch(id); }, [id]);
```

## Mistake 03: No cleanup
```jsx
// WRONG — memory leak
useEffect(() => {
  const timer = setInterval(tick, 1000);
}, []);
// CORRECT
useEffect(() => {
  const timer = setInterval(tick, 1000);
  return () => clearInterval(timer);
}, []);
```

## Mistake 04: Async useEffect
```jsx
// WRONG — can't be async
useEffect(async () => { await fetch(); }, []);
// CORRECT
useEffect(() => { fetch(); }, []);
```

## Mistake 05: Over-fetching
```jsx
// WRONG — fetches on every render
useEffect(() => { fetch(); });
// CORRECT — fetch once
useEffect(() => { fetch(); }, []);
```
