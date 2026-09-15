# Lesson 07 — Common Mistakes

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
