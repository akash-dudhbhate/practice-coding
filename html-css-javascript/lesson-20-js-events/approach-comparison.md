# Lesson 20 — Approach Comparison

## Problem: Handle Button Clicks

### Approach 1: Individual listeners
```javascript
buttons.forEach(btn => btn.addEventListener("click", handler));
```
**Cons:** New buttons need new listeners. Performance issues with many buttons.

### Approach 2: Event delegation
```javascript
container.addEventListener("click", (e) => {
  if (e.target.matches(".btn")) handler(e);
});
```
**Pros:** One listener, works for dynamically added buttons.

**Winner:** Approach 2 — event delegation is more efficient and flexible.

---

## Problem: Form Submission

### Approach 1: Submit button click
```javascript
submitBtn.addEventListener("click", validateForm);
```
**Cons:** Doesn't handle Enter key submission.

### Approach 2: Form submit event
```javascript
form.addEventListener("submit", (e) => {
  e.preventDefault();
  validateForm();
});
```
**Pros:** Handles all submission methods (button, Enter key).

**Winner:** Approach 2 — always listen on form submit, not button click.
