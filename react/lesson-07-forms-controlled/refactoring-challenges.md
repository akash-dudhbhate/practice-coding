# Lesson 07 — Refactoring Challenges

## Refactor 01 (Easy): Uncontrolled Input
### Before
```jsx
<input ref={inputRef} />
const value = inputRef.current.value;
```
### After
```jsx
const [value, setValue] = useState("");
<input value={value} onChange={e => setValue(e.target.value)} />
```

## Refactor 02 (Medium): Separate State per Field
### Before
```jsx
const [name, setName] = useState("");
const [email, setEmail] = useState("");
const [age, setAge] = useState("");
```
### After
```jsx
const [form, setForm] = useState({ name: "", email: "", age: "" });
const update = e => setForm(f => ({ ...f, [e.target.name]: e.target.value }));
```

## Refactor 03 (Hard): Manual Validation
### Before
```jsx
if (!email) setError("Email required");
else if (!email.includes("@")) setError("Invalid");
else setError("");
```
### After
```jsx
const errors = {
  email: !email ? "Required" : !email.includes("@") ? "Invalid" : "",
};
```
