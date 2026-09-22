# lesson-09-quasar-forms — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: q-form
```vue
<q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
  <q-input v-model="name" :rules="[val => !!val || 'Required']" />
  <q-btn type="submit" label="Submit" />
</q-form>
```
<details><summary>Answer</summary>
Wraps form inputs. `@submit` fires after validation passes. `@reset` for reset button. Validates all child inputs.
</details>

## Check 02: Validation rules
```javascript
:rules="[
  val => !!val || 'Required',
  val => val.length >= 3 || 'Min 3 characters',
  val => val.includes('@') || 'Must contain @'
]"
```
<details><summary>Answer</summary>
Array of functions. Each returns true or error message. All must pass. Run on input change and form submit.
</details>

## Check 03: Lazy validation
```vue
<q-input v-model="text" :rules="[...]" lazy-rules />
```
<details><summary>Answer</summary>
`lazy-rules` — validate on first blur, not on every keystroke. Better UX. Without it, validates immediately.
</details>

## Check 04: Form ref validation
```javascript
const formRef = ref(null);
async function submit() {
  const valid = await formRef.value.validate();
  if (!valid) return;
  // proceed
}
```
<details><summary>Answer</summary>
Programmatic validation. `validate()` returns promise. True if all valid. Use for custom submit logic.
</details>

## Check 05: q-select
```vue
<q-select v-model="selected" :options="options" label="Choose" />
```
<details><summary>Answer</summary>
Dropdown select. `options` = array of strings or objects. Supports filtering, multiple, chips, create-new. Very flexible.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: No Validation Rules
```vue
<q-input v-model="email" label="Email" />
```
<details><summary>Answer</summary>
**Issue:** No validation — accepts anything.
**Fix:** `:rules="[val => !!val || 'Required', val => /.+@.+/.test(val) || 'Invalid email']"`.
</details>

## Debug 02 (Medium: Not Using q-form
```vue
<q-input v-model="name" />
<q-btn @click="submit" />
```
<details><summary>Answer</summary>
**Issue:** No form validation orchestration. Can't validate all fields at once.
**Fix:** Wrap in `<q-form @submit="submit">` and use `q-btn type="submit"`.
</details>

## Debug 03 (Hard: Validation Not Triggering
```vue
<q-input v-model="text" :rules="[val => val.length > 3]" />
```
<details><summary>Answer</summary>
**Bug:** Validation only triggers on input change by default. May not validate on submit.
**Fix:** Use `q-form` with `@submit` and call `validate()` method.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: No validation
```vue
<!-- WRONG — accepts anything -->
<q-input v-model="email" />
<!-- CORRECT -->
<q-input v-model="email" :rules="[val => /.+@.+/.test(val) || 'Invalid']" />
```

## Mistake 02: Not wrapping in q-form
```vue
<!-- WRONG — no orchestration -->
<q-input /><q-btn @click="submit" />
<!-- CORRECT -->
<q-form @submit="submit"><q-input /><q-btn type="submit" /></q-form>
```

## Mistake 03: Not using type="submit"
```vue
<!-- WRONG — doesn't trigger form validation -->
<q-btn @click="submit" />
<!-- CORRECT -->
<q-btn type="submit" />
```

## Mistake 04: Not resetting validation
```javascript
formRef.value.resetValidation(); // clear errors after reset
```

## Mistake 05: Complex inline rules
```vue
<!-- HARD TO READ -->
:rules="[val => val && val.length > 3 && val.includes('@') || 'Error']"
<!-- BETTER — extract to function -->
:rules="[validateEmail]"
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Validation
### Before
```vue
<q-input v-model="email" />
```
### After
```vue
<q-input v-model="email" :rules="[val => /.+@.+/.test(val) || 'Invalid']" />
```

## Refactor 02 (Medium): Button onClick
### Before
```vue
<q-btn @click="submit" />
```
### After
```vue
<q-form @submit="submit"><q-btn type="submit" /></q-form>
```

## Refactor 03 (Hard: Manual Validation
### Before
```javascript
if (!email) { $q.notify("Required"); return; }
if (!email.includes("@")) { $q.notify("Invalid"); return; }
```
### After
```vue
<q-input v-model="email" :rules="[v => !!v || 'Required', v => v.includes('@') || 'Invalid']" />
```

---

## Approach Comparison — different ways to solve it

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
