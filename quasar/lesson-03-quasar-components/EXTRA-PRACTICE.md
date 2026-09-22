# lesson-03-quasar-components — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Component categories
What types of components does Quasar offer?
<details><summary>Answer</summary>
Buttons, forms, navigation, layout, cards, tables, dialogs, notifications, loading, media, chips, badges, expansion items, tabs, timelines, etc. 100+ components.
</details>

## Check 02: v-model on inputs
```vue
<q-input v-model="text" />
<q-select v-model="selected" />
<q-toggle v-model="checked" />
```
<details><summary>Answer</summary>
All form components support v-model. Two-way binding — input updates state, state updates input.
</details>

## Check 03: Color system
```vue
<q-btn color="primary" />
<q-card class="bg-secondary text-white" />
```
<details><summary>Answer</summary>
Quasar has color tokens: primary, secondary, accent, positive, negative, info, warning. Also arbitrary: `bg-red-5`, `text-blue-3`. Configured in quasar.config.js.
</details>

## Check 04: Slots
```vue
<q-card>
  <template #header>My Header</template>
  <q-card-section>Content</q-card-section>
  <template #actions>
    <q-btn label="OK" />
  </template>
</q-card>
```
<details><summary>Answer</summary>
Slots customize component parts. `#header`, `#actions` are named slots. Default slot for main content.
</details>

## Check 05: Dark mode
```vue
<q-dark style="background: #000">
```
<details><summary>Answer</summary>
`$q.dark.set(true)` programmatically. Or use `class="q-dark"`. Quasar components automatically adapt to dark mode.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Wrong Prop Type
```vue
<q-input :value="text" />
```
<details><summary>Answer</summary>
**Bug:** q-input uses `v-model`, not `:value`.
**Fix:** `<q-input v-model="text" />`.
</details>

## Debug 02 (Medium: Missing Label
```vue
<q-input v-model="email" />
```
<details><summary>Answer</summary>
**Issue:** No label — user doesn't know what the field is for.
**Fix:** `<q-input v-model="email" label="Email" />`.
</details>

## Debug 03 (Hard: Wrong Icon Format
```vue
<q-icon name="fa-user" />
```
<details><summary>Answer</summary>
**Bug:** `fa-user` is Font Awesome format. Quasar uses Material by default: `person`.
**Fix:** `<q-icon name="person" />` or install Font Awesome and use `img:fa-user`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Using :value instead of v-model
```vue
<!-- WRONG -->
<q-input :value="text" />
<!-- CORRECT -->
<q-input v-model="text" />
```

## Mistake 02: Missing labels
```vue
<!-- WRONG — no context -->
<q-input v-model="email" />
<!-- CORRECT -->
<q-input v-model="email" label="Email" />
```

## Mistake 03: Not using Quasar components
```vue
<!-- WRONG — custom HTML -->
<div class="card">...</div>
<!-- CORRECT -->
<q-card>...</q-card>
```

## Mistake 04: Wrong icon names
```vue
<!-- WRONG — Font Awesome format -->
<q-icon name="fa-user" />
<!-- CORRECT — Material format -->
<q-icon name="person" />
```

## Mistake 05: Not using slots
```vue
<!-- WRONG — can't customize -->
<q-card>...</q-card>
<!-- CORRECT — use slots -->
<q-card>
  <template #header>Custom Header</template>
</q-card>
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Custom Input
### Before
```vue
<input type="text" v-model="text" class="my-input" />
```
### After
```vue
<q-input v-model="text" label="Name" />
```

## Refactor 02 (Medium): Manual Card
### Before
```vue
<div class="card"><div class="header">Title</div><div class="body">Content</div></div>
```
### After
```vue
<q-card>
  <q-card-section><div class="text-h6">Title</div></q-card-section>
  <q-card-section>Content</q-card-section>
</q-card>
```

## Refactor 03 (Hard): No Slots
### Before
```vue
<q-card><div class="custom-header">My Header</div></q-card>
```
### After
```vue
<q-card><template #header>My Header</template></q-card>
```

---

## Approach Comparison — different ways to solve it

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
