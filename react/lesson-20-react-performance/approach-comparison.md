# Lesson 20 — Approach Comparison

## Problem: Prevent Unnecessary Re-renders

### Approach 1: React.memo
```jsx
const MemoChild = React.memo(Child);
```

### Approach 2: Move state down
```jsx
// Instead of state in parent, put it in a small component
function Button() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
// Parent doesn't re-render when count changes
```

**Winner:** Approach 2 — often simpler than memo. Only memo when you can't restructure.

---

## Problem: Large List

### Approach 1: Render all
```jsx
{items.map(item => <Row key={item.id} />)}
```
**Cons:** Slow for 1000+ items.

### Approach 2: Pagination
```jsx
{items.slice(0, page * 20).map(...)}
```

### Approach 3: Virtualization
```jsx
<FixedSizeList itemCount={items.length} itemSize={50}>...</FixedSizeList>
```

**Winner:** Approach 3 for 1000+ items. Approach 2 for moderate lists.
