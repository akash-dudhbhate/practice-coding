# Lesson 12 — Approach Comparison

## Problem: Form with Validation

### Approach 1: Multiple useState
```jsx
const [values, setValues] = useState({});
const [errors, setErrors] = useState({});
const [touched, setTouched] = useState({});
```
**Cons:** Hard to keep in sync, complex update logic.

### Approach 2: useReducer
```jsx
const [state, dispatch] = useReducer(formReducer, {
  values: {}, errors: {}, touched: {}
});
```
**Pros:** Centralized logic, testable, all state transitions in one place.

**Winner:** Approach 2 for complex forms. Approach 1 for simple forms.

---

## Problem: State Management

### Approach 1: useState
```jsx
const [count, setCount] = useState(0);
```

### Approach 2: useReducer
```jsx
const [count, dispatch] = useReducer((s, a) => a === "inc" ? s + 1 : s, 0);
```

**Winner:** Approach 1 — simpler for independent values. Don't over-engineer.
