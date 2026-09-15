# Lesson 03 — Common Mistakes

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
