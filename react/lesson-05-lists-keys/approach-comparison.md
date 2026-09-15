# Lesson 05 — Approach Comparison

## Problem: Render List

### Approach 1: for loop
```jsx
const elements = [];
for (let item of items) {
  elements.push(<li key={item.id}>{item.name}</li>);
}
return <ul>{elements}</ul>;
```

### Approach 2: map
```jsx
return <ul>{items.map(item => <li key={item.id}>{item.name}</li>)}</ul>;
```

**Winner:** Approach 2 — declarative, idiomatic React.

---

## Problem: Key Strategy

### Approach 1: Index
```jsx
key={index}
```
**Cons:** Breaks on reorder/insert/delete.

### Approach 2: ID
```jsx
key={item.id}
```

**Winner:** Approach 2 — always use stable unique IDs.
