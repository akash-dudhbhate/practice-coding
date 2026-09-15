# Lesson 01 — Approach Comparison

## Problem: Greeting Component

### Approach 1: props object
```jsx
function Greeting(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

### Approach 2: Destructured props
```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}</h1>;
}
```

**Winner:** Approach 2 — cleaner, explicit about what props are used.

---

## Problem: Multiple Elements

### Approach 1: Wrapper div
```jsx
return <div><h1>A</h1><p>B</p></div>;
```
**Cons:** Extra DOM node, may break flexbox/grid.

### Approach 2: Fragment
```jsx
return <><h1>A</h1><p>B</p></>;
```

**Winner:** Approach 2 — no extra DOM node.
