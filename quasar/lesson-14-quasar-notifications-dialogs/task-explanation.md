# Lesson 14 — Quasar Notifications & Dialogs

## What you'll learn
- Notify plugin (types, positions, actions, undo)
- Dismissing notifications programmatically
- Dialog plugin (confirm, prompt, options)
- Custom dialog components
- QBottomSheet (mobile action menus)
- QAjaxBar (loading bar)
- Combining notifications and dialogs (complete UX flows)

## Lesson

### Notify with action
```js
$q.notify({
    message: 'Deleted',
    actions: [{ label: 'Undo', handler: () => undo() }],
    timeout: 5000,
})
```

### Dialog
```js
$q.dialog({ title: 'Confirm', cancel: true })
  .onOk(() => doAction())
```

### Custom dialog
```js
$q.dialog({ component: MyDialog, componentProps: { data } })
  .onOk(result => handleResult(result))
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.vue` — Create a component with 4 buttons that show different notification types (positive, negative, warning, info). Each notification has a custom message, icon, and position.
2. `easy/p02-solve.vue` — Create a delete confirmation flow: button opens a dialog, confirm triggers a "deleted" notification with an Undo action (5s timeout). Cancel shows a "cancelled" notification.
3. `easy/p03-solve.vue` — Create a prompt dialog: button opens a dialog with a text input. On OK, show a notification with the entered text. Validate that the input is not empty.

### Medium
4. `medium/p01-solve.vue` — Create a loading flow: button starts a persistent "Loading..." notification (timeout=0), simulates a 3-second operation, then dismisses the loading and shows a success notification. Use the dismiss function.
5. `medium/p02-solve.vue` — Create a bottom sheet with 4 actions (Share, Copy, Edit, Delete). On select, show a notification with the selected action. Use `$q.bottomSheet`. Style for mobile.
6. `medium/p03-solve.vue` — Create a custom dialog component: a dialog with a form (name, email). Use `$q.dialog({ component: CustomFormDialog })`. On OK, emit the form data. Show a notification with the data.

### Hard
7. `hard/p01-solve.vue` — Build a complete CRUD feedback system: a composable `useCrudNotifications` that wraps create/update/delete operations with consistent notifications. Include: success (positive), error (negative), delete with undo (5s), and loading states.
8. `hard/p02-solve.vue` — Build a multi-step dialog wizard: a custom dialog component with 3 steps (form, review, confirm). Navigation between steps. On finish, emit the collected data. Include validation per step. Close on cancel.
9. `hard/p03-solve.vue` — Build a notification center: a component that shows a bell icon with a badge count. Clicking opens a dropdown with all notifications. Notifications can be marked as read. Include different types (info, warning, error). Persist read state to localStorage.

### How to work
- Write your complete Vue/Quasar solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
