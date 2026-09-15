# Lesson 02 — Refactoring Challenges

## Refactor 01 (Easy): CSS Fixed Header
### Before
```css
.header { position: fixed; top: 0; width: 100%; }
```
### After
```vue
<q-header elevated>...</q-header>
```

## Refactor 02 (Medium): Manual Drawer Toggle
### Before
```javascript
const drawerOpen = ref(false);
function toggleDrawer() { drawerOpen.value = !drawerOpen.value; }
```
### After
```vue
<q-drawer v-model="drawerOpen" />
<q-btn @click="drawerOpen = !drawerOpen" />
```

## Refactor 03 (Hard): No Responsive Drawer
### Before
```vue
<q-drawer :breakpoint="0" v-model="open" />
```
### After
```vue
<q-drawer :breakpoint="500" v-model="open" />
```
