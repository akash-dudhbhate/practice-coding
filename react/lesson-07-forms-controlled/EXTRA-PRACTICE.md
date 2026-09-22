# lesson-07-forms-controlled — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Controlled vs uncontrolled
What's the difference?
<details><summary>Answer</summary>
Controlled — React state is the source of truth (`value` + `onChange`). Uncontrolled — DOM is source of truth (use `ref` to access). Prefer controlled.
</details>

## Check 02: Form submission
```jsx
const handleSubmit = (e) => {
  e.preventDefault();
  console.log(formData);
};
```
<details><summary>Answer</summary>
`e.preventDefault()` stops page reload. Access form data from state, not from the event.
</details>

## Check 03: Multiple inputs
```jsx
const [form, setForm] = useState({ name: "", email: "" });
const handleChange = (e) => {
  setForm({ ...form, [e.target.name]: e.target.value });
};
```
<details><summary>Answer</summary>
Dynamic key update — `name` attribute on input determines which field to update. One handler for all inputs.
</details>

## Check 04: Select
```jsx
<select value={color} onChange={e => setColor(e.target.value)}>
  <option value="red">Red</option>
  <option value="blue">Blue</option>
</select>
```
<details><summary>Answer</summary>
Controlled select — `value` on `<select>`, not on `<option>`. Different from HTML.
</details>

## Check 05: File input
```jsx
<input type="file" onChange={e => setFile(e.target.files[0])} />
```
<details><summary>Answer</summary>
File inputs are always uncontrolled (can't set value for security). Access files via `e.target.files`.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Uncontrolled Input
```jsx
<input type="text" />
```
<details><summary>Answer</summary>
**Issue:** Uncontrolled — React doesn't track the value. Can't validate or transform.
**Fix:** `value={text} onChange={e => setText(e.target.value)}`.
</details>

## Debug 02 (Medium): readOnly Without onChange
```jsx
<input value={text} />
```
<details><summary>Answer</summary>
**Bug:** Controlled input without onChange — React warns and input is read-only.
**Fix:** Add `onChange={e => setText(e.target.value)}` or `readOnly` attribute.
</details>

## Debug 03 (Hard): Checkbox Handler
```jsx
<input type="checkbox" value={isChecked} onChange={e => setIsChecked(e.target.value)} />
```
<details><summary>Answer</summary>
**Bug:** Checkbox uses `checked` not `value`, and `e.target.checked` not `e.target.value`.
**Fix:** `checked={isChecked} onChange={e => setIsChecked(e.target.checked)}`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Uncontrolled inputs
```jsx
// WRONG — React doesn't track
<input type="text" />
// CORRECT — controlled
<input value={text} onChange={e => setText(e.target.value)} />
```

## Mistake 02: value without onChange
```jsx
// WRONG — read-only warning
<input value={text} />
// CORRECT
<input value={text} onChange={e => setText(e.target.value)} />
```

## Mistake 03: Checkbox wrong attributes
```jsx
// WRONG
<input type="checkbox" value={checked} onChange={e => setChecked(e.target.value)} />
// CORRECT
<input type="checkbox" checked={checked} onChange={e => setChecked(e.target.checked)} />
```

## Mistake 04: Not using name attribute for multiple inputs
```jsx
// VERBOSE — separate handler per input
const handleName = e => setName(e.target.value);
const handleEmail = e => setEmail(e.target.value);
// BETTER — one handler
const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });
```

## Mistake 05: Not preventing default
```jsx
// WRONG — page reloads
<form onSubmit={handleSubmit}>
// CORRECT
const handleSubmit = (e) => { e.preventDefault(); ... };
```

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

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
