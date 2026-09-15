# Lesson 02 — Coding Check

Use this to verify your solutions before asking me to review. Open each HTML file in a browser to check it renders correctly.

## Easy

### p01-solve.html (Login form)
- [ ] Has `<form>` with `action` and `method` attributes.
- [ ] Email input with `type="email"`, `id="email"`, `name="email"`.
- [ ] Password input with `type="password"`, `id="password"`, `name="password"`.
- [ ] Each input has a `<label>` with `for` matching the input's `id`.
- [ ] Submit button (`<button type="submit">`).
- [ ] Clicking the label text focuses the corresponding input.
- [ ] Submitting with an empty email shows browser validation error (add `required`).

### p02-solve.html (Contact form)
- [ ] Text input for name with label.
- [ ] Email input with `type="email"` and label.
- [ ] `<textarea>` for message with label, `name="message"`, `rows` set.
- [ ] Submit button.
- [ ] All inputs have `name` attributes.
- [ ] Textarea has a closing `</textarea>` tag.

### p03-solve.html (Signup form with checkbox)
- [ ] Text input for name, email input, password input — all labeled.
- [ ] Checkbox for "I agree to terms" with `<label>` wrapping or `for`/`id` link.
- [ ] Checkbox has `name` and `value` attributes.
- [ ] Submit button.
- [ ] All inputs have `name` attributes.

## Medium

### p01-solve.html (Survey with radios, checkboxes, select)
- [ ] Radio buttons grouped by same `name` (e.g. `name="rating"`).
- [ ] Each radio has a unique `id` and a `<label>` with matching `for`.
- [ ] Checkboxes for multi-select (e.g. `name="features"`).
- [ ] `<select>` with at least 3 `<option>` elements, each with a `value`.
- [ ] Select has a label and a placeholder/empty first option.
- [ ] Submit button present.

### p02-solve.html (Product order form)
- [ ] Number input with `min`, `max`, and `name` for quantity.
- [ ] `<select>` for size (S/M/L) with `value` on each option.
- [ ] Checkboxes for extras, each with `name` and `value`.
- [ ] All inputs labeled.
- [ ] Submit button present.
- [ ] Number input rejects letters (type="number" enforced).

### p03-solve.html (Registration with validation)
- [ ] Name field with `required`.
- [ ] Email field with `type="email"` and `required`.
- [ ] Password field with `minlength="8"` and `required`.
- [ ] Age field with `type="number"`, `min="13"`, `max="120"`.
- [ ] Submit button.
- [ ] Submitting empty form shows browser validation errors.
- [ ] Submitting invalid email shows format error.

## Hard

### p01-solve.html (Checkout form)
- [ ] Shipping address: text inputs for street, city, state, zip (all labeled, all named).
- [ ] Payment: card number (text or tel), expiry (date or text), CVV (number with min/max length).
- [ ] All fields have `required` where appropriate.
- [ ] Uses `<fieldset>` and `<legend>` to group "Shipping" and "Payment" sections.
- [ ] Submit button labeled "Place Order".
- [ ] Every input has a `<label>` with matching `for`/`id`.

### p02-solve.html (Job application form)
- [ ] File input with `type="file"`, `name="resume"`, and label.
- [ ] Date input with `type="date"` for availability date.
- [ ] `<textarea>` for cover letter with label and `name`.
- [ ] `<select>` for position with at least 3 options and values.
- [ ] Radio buttons for availability (full-time/part-time), grouped by `name`.
- [ ] Submit button present.
- [ ] All inputs labeled and named.

### p03-solve.html (Settings form with reset)
- [ ] Uses `<fieldset>`/`<legend>` to group settings categories.
- [ ] Checkboxes for notification preferences (each with name + value).
- [ ] Radio buttons for theme (light/dark), grouped by `name`.
- [ ] `<select>` for language preference.
- [ ] Submit button (`type="submit"`) AND reset button (`type="reset"`).
- [ ] Reset button clears all inputs to defaults when clicked.
- [ ] All inputs labeled and named.

## How to verify

Open each file in a browser:
```bash
xdg-open easy/p01-solve.html
```
- Click each label — the correct input should focus.
- Try submitting an empty form — browser validation should block it (if `required` is set).
- Try submitting invalid data (wrong email format, number out of range) — browser should show errors.
- For radios: selecting one should deselect others in the same group.
- For reset button: clicking it should clear all fields.
