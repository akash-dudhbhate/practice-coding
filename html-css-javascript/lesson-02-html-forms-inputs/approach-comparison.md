# Lesson 02 — Approach Comparison

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
