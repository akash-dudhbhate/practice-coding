# Lesson 02 — Intuition Checks

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
