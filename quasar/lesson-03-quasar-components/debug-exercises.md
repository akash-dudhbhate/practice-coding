# Lesson 03 — Debug Exercises

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
