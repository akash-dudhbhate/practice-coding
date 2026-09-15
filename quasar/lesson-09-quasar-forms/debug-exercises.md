# Lesson 09 — Debug Exercises

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
