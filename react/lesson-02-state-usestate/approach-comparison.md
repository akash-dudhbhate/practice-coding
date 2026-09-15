# Lesson 02 — Approach Comparison

## Problem: Toggle State

### Approach 1: Boolean state
```jsx
const [isOpen, setIsOpen] = useState(false);
const toggle = () => setIsOpen(!isOpen);
```

### Approach 2: Functional update
```jsx
const toggle = () => setIsOpen(prev => !prev);
```

**Winner:** Approach 2 — safer, avoids stale closure issues.

---

## Problem: Form State

### Approach 1: Individual states
```jsx
const [name, setName] = useState("");
const [email, setEmail] = useState("");
const [age, setAge] = useState(0);
```

### Approach 2: Object state
```jsx
const [form, setForm] = useState({ name: "", email: "", age: 0 });
const update = (field) => (e) => setForm({ ...form, [field]: e.target.value });
```

**Winner:** Approach 2 for many fields. Approach 1 for 2-3 fields.
