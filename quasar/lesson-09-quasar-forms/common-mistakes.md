# Lesson 09 — Common Mistakes

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
