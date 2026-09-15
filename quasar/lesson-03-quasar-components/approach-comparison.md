# Lesson 03 — Approach Comparison

## Problem: Form Input

### Approach 1: HTML input
```vue
<input type="text" v-model="text" class="my-input" />
```
**Cons:** No styling, no validation, no labels.

### Approach 2: q-input
```vue
<q-input v-model="text" label="Name" :rules="[val => !!val || 'Required']" />
```

**Winner:** Approach 2 — styled, validated, accessible.

---

## Problem: Card Layout

### Approach 1: Custom divs
```vue
<div class="card">
  <div class="card-header">Title</div>
  <div class="card-body">Content</div>
</div>
```

### Approach 2: q-card
```vue
<q-card>
  <q-card-section><div class="text-h6">Title</div></q-card-section>
  <q-card-section>Content</q-card-section>
</q-card>
```

**Winner:** Approach 2 — Material Design, consistent.
