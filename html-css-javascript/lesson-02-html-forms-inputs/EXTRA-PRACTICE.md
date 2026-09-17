# lesson-02-html-forms-inputs — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: GET vs POST
When should you use POST instead of GET?
<details><summary>Answer</summary>
POST for: sensitive data (passwords), large data, data that changes server state. GET for: retrieving data, search queries, bookmarkable URLs.
</details>

## Check 02: required attribute
```html
<input type="text" name="name" required>
```
What does `required` do?
<details><summary>Answer</summary>
Browser prevents form submission if the field is empty. Client-side validation. Always also validate server-side.
</details>

## Check 03: Label association
```html
<label>Username: <input type="text"></label>
<label for="email">Email:</label> <input id="email" type="email">
```
Which is correct?
<details><summary>Answer</summary>
Both work. First wraps the input. Second uses `for`/`id` association. The `for`/`id` approach is more flexible (label and input don't need to be adjacent).
</details>

## Check 04: Button type
```html
<button onclick="submit()">Submit</button>
```
What's the default type?
<details><summary>Answer</summary>
`type="submit"` — clicking it submits the form. Use `type="button"` if you don't want form submission, or `type="reset"` to clear the form.
</details>

## Check 05: placeholder vs label
Why not use placeholder instead of label?
<details><summary>Answer</summary>
Placeholder disappears on input, has low contrast, isn't read by all screen readers, and disappears on focus. Always use a label. Placeholder is a hint, not a label.
</details>

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: No label
```html
<!-- WRONG -->
<input type="text" placeholder="Username">

<!-- CORRECT -->
<label for="username">Username</label>
<input id="username" type="text" name="username">
```

## Mistake 02: Wrong input type
```html
<!-- WRONG -->
<input type="text" name="phone">
<input type="text" name="date">

<!-- CORRECT -->
<input type="tel" name="phone">
<input type="date" name="date">
```

## Mistake 03: No server-side validation
```html
<!-- WRONG — only client-side -->
<input type="email" required>
```
Always validate server-side too — client-side can be bypassed.

## Mistake 04: Forgetting name attribute
```html
<!-- WRONG — data not sent -->
<input type="text" id="username">

<!-- CORRECT -->
<input type="text" id="username" name="username">
```

## Mistake 05: Using placeholder as label
```html
<!-- WRONG -->
<input type="text" placeholder="Enter your name">

<!-- CORRECT -->
<label for="name">Name</label>
<input id="name" type="text" placeholder="John Doe">
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Repeated Properties
### Before
```css
.btn { padding: 10px; margin: 5px; border: 1px solid #ccc; }
.card { padding: 10px; margin: 5px; border: 1px solid #ccc; }
```
### After
```css
.btn, .card { padding: 10px; margin: 5px; border: 1px solid #ccc; }
```

## Refactor 02 (Medium): Magic Numbers
### Before
```css
.box { margin: 23px; padding: 17px; width: 347px; }
```
### After
```css
:root { --spacing: 16px; --width: 350px; }
.box { margin: var(--spacing); padding: var(--spacing); width: var(--width); }
```

## Refactor 03 (Hard): Over-Specific Selectors
### Before
```css
body div.container main section article p.text { color: blue; }
```
### After
```css
.text { color: blue; }

---

## Approach Comparison — different ways to solve it

## Problem: Login Form

### Approach 1: Basic
```html
<form action="/login" method="post">
  <input type="text" name="username">
  <input type="password" name="password">
  <button>Login</button>
</form>
```
**Cons:** No labels, no validation.

### Approach 2: Accessible
```html
<form action="/login" method="post">
  <label for="username">Username</label>
  <input id="username" type="text" name="username" required>
  <label for="password">Password</label>
  <input id="password" type="password" name="password" required minlength="8">
  <button type="submit">Login</button>
</form>
```
**Pros:** Labels, validation, proper types.

**Winner:** Approach 2 — accessible and validated.

---

## Problem: File Upload

### Approach 1: Basic input
```html
<input type="file" name="upload">
```

### Approach 2: With attributes
```html
<label for="upload">Choose file</label>
<input id="upload" type="file" name="upload" accept="image/*" multiple>
```

**Winner:** Approach 2 — `accept` filters file types, `multiple` allows multiple files.
