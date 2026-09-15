# Lesson 01 — Approach Comparison

## Problem: Create Button

### Approach 1: HTML button
```vue
<button class="btn-primary" @click="handle">Save</button>
```
**Cons:** Need to style, no Material Design, inconsistent.

### Approach 2: q-btn
```vue
<q-btn label="Save" color="primary" icon="save" @click="handle" />
```

**Winner:** Approach 2 — styled, consistent, accessible.

---

## Problem: Project Setup

### Approach 1: Manual Vue + Quasar
```bash
npm install vue quasar
# configure manually
```

### Approach 2: Quasar CLI
```bash
quasar create my-app
```

**Winner:** Approach 2 — handles everything, best practices.
