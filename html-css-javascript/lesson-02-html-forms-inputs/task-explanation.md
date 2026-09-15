# Lesson 02 — HTML Forms & Input Types

## What you'll learn
- How to build forms with `<form>`, `<label>`, `<input>`, `<select>`, `<textarea>`.
- The different `<input>` types and when to use each.
- Built-in HTML validation (`required`, `min`, `max`, `pattern`).
- How the `name` attribute sends data to the server.

## Lesson

Forms are how users send data to a website. Every login, search, comment, and checkout is a form.

### The basic form
```html
<form action="/submit" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required />
  <button type="submit">Send</button>
</form>
```
- `action` = where the data goes.
- `method` = how it's sent (`GET` or `POST`).
- Each `<label for="...">` must match its input's `id`.

### Choosing the right input type
The `type` attribute gives users the right keyboard and free validation:
```html
type="email"    -> validates email format
type="password" -> hides characters
type="number"   -> numeric keyboard, min/max
type="date"     -> date picker
type="checkbox" -> select multiple
type="radio"    -> select one (grouped by name)
```

### Dropdowns and text areas
```html
<select name="country">
  <option value="us">United States</option>
</select>

<textarea name="message" rows="4"></textarea>
```

### Validation
```html
<input type="number" min="1" max="100" required />
<input type="text" pattern="[A-Za-z]{3}" title="3 letters only" />
```

### Key rules
- Every input needs a `<label>` with `for` matching the input's `id`.
- Every input that should be submitted needs a `name` attribute.
- Radio buttons share the same `name` to group them.
- Use `placeholder` as a hint, never as a replacement for a label.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete HTML from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.html` — A login form with email + password inputs, labels, and a submit button.
2. `easy/p02-solve.html` — A contact form with text input, email input, textarea, and submit button.
3. `easy/p03-solve.html` — A signup form with text, email, password, and a checkbox for terms.

### Medium
4. `medium/p01-solve.html` — A survey form with radio buttons, checkboxes, and a select dropdown.
5. `medium/p02-solve.html` — A product order form with number input (min/max), select for size, checkboxes for extras.
6. `medium/p03-solve.html` — A registration form with validation: required fields, email pattern, password minlength, number range.

### Hard
7. `hard/p01-solve.html` — A complete checkout form: shipping address, payment fields, validation, proper labels and grouping.
8. `hard/p02-solve.html` — A job application form with file upload, date picker, textarea cover letter, select for position, radio for availability.
9. `hard/p03-solve.html` — A settings/preferences form with grouped fieldsets, checkboxes, radios, selects, and a reset button.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete HTML from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Open the file in a browser to check it renders correctly.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
