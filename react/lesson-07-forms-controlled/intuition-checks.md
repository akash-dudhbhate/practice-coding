# Lesson 07 — Intuition Checks

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
