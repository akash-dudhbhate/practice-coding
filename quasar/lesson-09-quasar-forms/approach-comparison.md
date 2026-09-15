# Lesson 09 — Approach Comparison

## Problem: Form Validation

### Approach 1: Manual validation
```javascript
function submit() {
  if (!email.value) { $q.notify("Email required"); return; }
  if (!email.value.includes("@")) { $q.notify("Invalid"); return; }
}
```

### Approach 2: Quasar rules
```vue
<q-input v-model="email" :rules="[val => !!val || 'Required', val => val.includes('@') || 'Invalid']" />
```

**Winner:** Approach 2 — declarative, per-field, visual feedback.

---

## Problem: Form Submission

### Approach 1: Button onClick
```vue
<q-btn @click="handleSubmit" />
```
**Cons:** Doesn't validate form.

### Approach 2: Form @submit
```vue
<q-form @submit="handleSubmit"><q-btn type="submit" /></q-form>
```

**Winner:** Approach 2 — validates before submit, handles Enter key.
