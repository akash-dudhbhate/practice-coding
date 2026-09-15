# Lesson 06 — Approach Comparison

## Problem: Fetch on Mount

### Approach 1: useEffect with empty deps
```jsx
useEffect(() => {
  fetch('/api/data').then(setData);
}, []);
```

### Approach 2: React Query
```jsx
const { data } = useQuery('data', () => fetch('/api/data').then(r => r.json()));
```

**Winner:** Approach 2 for production — handles caching, loading, error states. Approach 1 for learning.

---

## Problem: Event Listener

### Approach 1: useEffect
```jsx
useEffect(() => {
  const handler = () => console.log('resize');
  window.addEventListener('resize', handler);
  return () => window.removeEventListener('resize', handler);
}, []);
```

### Approach 2: Custom hook
```jsx
useEventListener('resize', () => console.log('resize'));
```

**Winner:** Approach 2 — reusable, encapsulated.
