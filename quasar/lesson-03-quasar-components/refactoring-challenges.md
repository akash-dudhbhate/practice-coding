# Lesson 03 — Refactoring Challenges

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
