# Lesson 07 — Approach Comparison

## Problem: Form State

### Approach 1: Individual useState
```jsx
const [name, setName] = useState("");
const [email, setEmail] = useState("");
```

### Approach 2: Single state object
```jsx
const [form, setForm] = useState({ name: "", email: "" });
```

### Approach 3: useReducer
```jsx
const [form, dispatch] = useReducer(formReducer, initialForm);
```

**Winner:** Approach 1 for 2-3 fields. Approach 2 for many fields. Approach 3 for complex validation.

---

## Problem: Form Library

### Approach 1: Manual controlled
```jsx
const [form, setForm] = useState({});
```

### Approach 2: React Hook Form
```jsx
const { register, handleSubmit } = useForm();
```

**Winner:** Approach 2 for production — less code, better performance, built-in validation.
