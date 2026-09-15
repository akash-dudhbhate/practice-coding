# Lesson 01 — Refactoring Challenges

## Refactor 01 (Easy): HTML Button
### Before
```vue
<button class="btn-primary" @click="save">Save</button>
```
### After
```vue
<q-btn label="Save" color="primary" icon="save" @click="save" />
```

## Refactor 02 (Medium): Manual Setup
### Before
```bash
npm install vue quasar
# configure manually
```
### After
```bash
quasar create my-app
```

## Refactor 03 (Hard): No Layout System
### Before
```vue
<div class="header">...</div>
<div class="sidebar">...</div>
<div class="content">...</div>
```
### After
```vue
<q-layout view="hHh lpR fFf">
  <q-header>...</q-header>
  <q-drawer>...</q-drawer>
  <q-page-container><q-page>...</q-page></q-page-container>
</q-layout>
```
