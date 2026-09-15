# Lesson 09 — Intuition Checks

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
