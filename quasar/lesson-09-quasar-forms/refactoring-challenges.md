# Lesson 09 — Refactoring Challenges

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
