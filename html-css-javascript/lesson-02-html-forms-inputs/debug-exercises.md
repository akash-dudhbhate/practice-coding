# Lesson 02 — Debug Exercises

## Debug 01 (Easy): Missing Label
```html
<input type="text" name="username">
```
<details><summary>Answer</summary>
**Bug:** No label — screen readers can't identify the field.
**Fix:** `<label for="username">Username</label><input id="username" type="text" name="username">`.
</details>

## Debug 02 (Medium): Wrong Input Type
```html
<input type="text" name="email">
```
<details><summary>Answer</summary>
**Bug:** `type="text"` doesn't validate email or show email keyboard on mobile.
**Fix:** `type="email"` for validation and better mobile UX.
</details>

## Debug 03 (Hard): Form Without Action
```html
<form method="post">
  <input name="data">
  <button>Submit</button>
</form>
```
<details><summary>Answer</summary>
**Bug:** No `action` attribute — form submits to the current page, which may not handle it.
**Fix:** `<form action="/submit" method="post">`.
</details>
