# Lesson 08 — Quasar Plugins

## What you'll learn
- What Quasar plugins are ($q global utilities)
- Notify plugin (toast notifications)
- Dialog plugin (confirmations and prompts)
- Dark mode plugin (theme toggling)
- Platform plugin (OS/browser detection)
- Screen plugin (responsive breakpoints)
- Loading plugin (spinner overlays)
- AppFullscreen plugin (fullscreen mode)

## Lesson

### Notify
```js
import { useQuasar } from 'quasar'
const $q = useQuasar()
$q.notify({ message: 'Saved!', type: 'positive' })
```

### Dialog
```js
$q.dialog({ title: 'Confirm', message: 'Delete?', cancel: true })
  .onOk(() => deleteItem())
```

### Dark mode
```js
$q.dark.toggle()
$q.dark.set(true)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.vue` — Create a component with a button that shows a notification using `$q.notify`. Show 4 types: positive, negative, warning, info. Each on a separate button.
2. `easy/p02-solve.vue` — Create a component with a dark mode toggle button. Use `$q.dark.toggle()`. Display the current dark mode state (`$q.dark.isActive`).
3. `easy/p03-solve.vue` — Create a component that detects the platform using `$q.platform`. Display whether the user is on mobile/desktop, iOS/Android, and the browser name.

### Medium
4. `medium/p01-solve.vue` — Create a delete confirmation flow: button triggers `$q.dialog` with confirm/cancel. On confirm, show a "deleted" notification. On cancel, show a "cancelled" notification.
5. `medium/p02-solve.vue` — Create a responsive grid component using `$q.screen`. Show 1 column on xs, 2 on sm, 3 on md+. Display the current breakpoint name. Use `q-card` for grid items.
6. `medium/p03-solve.vue` — Create a form submission flow: show loading spinner during "save" (use `$q.loading`), simulate a 2-second async operation, then show success or error notification. Always hide loading in `finally`.

### Hard
7. `hard/p01-solve.vue` — Build a complete notification system: a composable `useNotifications` that wraps `$q.notify` with presets (success, error, warning, info). Each preset has default colors, icons, and timeout. Include an "undo" action for delete notifications.
8. `hard/p02-solve.vue` — Build a platform-aware component: detect platform and screen size. On mobile, show a bottom sheet menu. On desktop, show a dropdown menu. Use `$q.platform` and `$q.screen` together. Include at least 4 menu items.
9. `hard/p03-solve.vue` — Build a settings panel: dark mode toggle (persisted to localStorage), notification position selector (top/bottom/top-right), and loading spinner color picker. All settings should be persisted and applied on app load.

### How to work
- Write your complete Vue/Quasar solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
