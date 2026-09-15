# Lesson 13 — Refactoring Challenges

## Refactor 01 (Easy): Inline Validation
### Before
```html
<input onblur="validateEmail(this.value)" />
```
### After
```html
<input id="email" required type="email" />
<script>email.addEventListener("blur", validateEmail);</script>
```

## Refactor 02 (Medium): Manual Validation
### Before
```javascript
if (email === "") { showError("Email required"); return false; }
if (!email.includes("@")) { showError("Invalid email"); return false; }
```
### After
```html
<input type="email" required />
<!-- Browser handles validation -->
```

## Refactor 03 (Hard): Repeated Validation Logic
### Before
```javascript
function validateForm() {
  if (!name) return false;
  if (!email) return false;
  if (!phone) return false;
  return true;
}
```
### After
```javascript
const required = ["name", "email", "phone"];
const valid = required.every(field => form[field].value.trim());
```
