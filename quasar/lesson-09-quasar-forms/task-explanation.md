# Lesson 09 — Quasar Forms

## What you'll learn
- QForm and QInput (forms with validation)
- Validation rules (sync and async)
- QSelect, QToggle, QCheckbox, QRadio, QSlider
- Form submission and reset
- QEditor (rich text)
- QFile (file upload)
- Form layout best practices

## Lesson

### Basic form
```vue
<q-form @submit="onSubmit">
    <q-input v-model="name" :rules="[val => !!val || 'Required']" />
    <q-btn type="submit" label="Submit" />
</q-form>
```

### Select
```vue
<q-select v-model="country" :options="countries" emit-value map-options />
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.vue` — Create a login form with email and password fields. Add validation (email required + format, password required + min 6 chars). On submit, show a notification with the values.
2. `easy/p02-solve.vue` — Create a form with QSelect (country), QToggle (notifications), QCheckbox (terms), and QRadio (gender). Display the form state below the form.
3. `easy/p03-solve.vue` — Create a form with submit and reset buttons. On reset, clear all fields and validation errors. Use `formRef.resetValidation()`.

### Medium
4. `medium/p01-solve.vue` — Create a registration form with sections: Personal Info (name, email), Address (street, city, zip), Preferences (newsletter toggle, theme select). Use a 2-column layout on desktop, 1-column on mobile.
5. `medium/p02-solve.vue` — Create a form with async validation: username field that checks if the username is available (simulate API call with setTimeout). Show "checking..." while validating, "available" or "taken" as the result.
6. `medium/p03-solve.vue` — Create a file upload form using QFile. Allow multiple images (jpg, png). Show file previews. Validate file size (max 5MB). Show a notification for rejected files.

### Hard
7. `hard/p01-solve.vue` — Build a multi-step form wizard: 3 steps (personal, contact, review). Each step has its own validation. Navigation: next (validates current step), back, and submit on the last step. Show a progress indicator.
8. `hard/p02-solve.vue` — Build a dynamic form: a form where users can add/remove fields (e.g., "add another phone number"). Each added field has validation. Submit collects all dynamic fields. Include add and remove buttons.
9. `hard/p03-solve.vue` — Build a form with a rich text editor (QEditor) and live preview. User writes in the editor, preview shows the rendered HTML below. Include a save button that stores the content and a clear button that resets. Sanitize the HTML before display.

### How to work
- Write your complete Vue/Quasar solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
