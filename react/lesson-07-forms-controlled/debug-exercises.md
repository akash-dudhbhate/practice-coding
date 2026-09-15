# Lesson 07 — Debug Exercises

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
