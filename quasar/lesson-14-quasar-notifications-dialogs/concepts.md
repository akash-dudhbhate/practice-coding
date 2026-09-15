# Lesson 14 — Concepts Explained (Quasar Notifications & Dialogs)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Notify Plugin (Detailed)

**What:** Display toast notifications with various types, positions, and actions buttons.

```js
import { useQuasar } from 'quasar'
const $q = useQuasar()

// Basic types
$q.notify('Simple message')
$q.notify({ type: 'positive', message: 'Success!' })
$q.notify({ type: 'negative', message: 'Error!' })
$q.notify({ type: 'warning', message: 'Warning!' })
$q.notify({ type: 'info', message: 'Info!' })

// With position
$q.notify({ message: 'Top notification', position: 'top' })
$q.notify({ message: 'Bottom-left', position: 'bottom-left' })

// With action button
$q.notify({
    message: 'Item deleted',
    color: 'negative',
    actions: [
        { label: 'Undo', color: 'white', handler: () => undoDelete() }
    ],
    timeout: 5000,  // 5 seconds to undo
})

// Persistent (no auto-dismiss)
$q.notify({
    message: 'Processing...',
    timeout: 0,  // stays until dismissed
    closeBtn: true,
})
```

**Why it exists:** Notifications provide feedback without blocking the user → non-intrusive. Different types (positive/negative/warning) → instant visual recognition. Action buttons → undo mistakes.

**Where it's used:** After every CRUD operation, form submission, error, or important event.

**What goes wrong without it:**
- `timeout: 0` without `closeBtn` → notification stays forever → user stuck. Always add a close button.
- Too many notifications → spam → user ignores them. Batch notifications or use a single summary.
- Not dismissing after action → "Processing..." stays after done. Dismiss programmatically.

---

## Dismissing Notifications Programmatically

**What:** Control when notifications close.

```js
// Create a notification and get a dismiss function
const dismiss = $q.notify({
    message: 'Loading...',
    timeout: 0,  // persistent
})

// Later, dismiss it
setTimeout(() => {
    dismiss()  // closes the notification
}, 3000)

// With async operations
const dismiss = $q.notify({ message: 'Saving...', timeout: 0 })
try {
    await saveData()
    dismiss()
    $q.notify({ type: 'positive', message: 'Saved!' })
} catch (error) {
    dismiss()
    $q.notify({ type: 'negative', message: 'Error!' })
}
```

**Why it exists:** Some notifications shouldn't auto-dismiss (loading, processing). You need to control when they close → dismiss programmatically → clean UX.

**Where it's used:** Loading states, multi-step operations, progress indicators.

**What goes wrong without it:**
- Forgetting to call `dismiss()` → notification stays forever → user confused.
- Dismissing before the new notification → flicker. Dismiss after showing the result.
- Error in try block after dismiss → dismiss not called → use `finally`.

---

## Dialog Plugin (Detailed)

**What:** Modal dialogs for confirmations, prompts, custom content.

```js
// Confirmation
$q.dialog({
    title: 'Delete Item',
    message: 'Are you sure you want to delete this item?',
    ok: { label: 'Delete', color: 'negative', unelevated: true },
    cancel: true,
    persistent: true,
}).onOk(() => {
    deleteItem()
})

// Prompt (text input)
$q.dialog({
    title: 'New Folder',
    message: 'Enter folder name:',
    prompt: {
        model: '',
        type: 'text',
        isValid: val => val.length > 0 || 'Name required',
    },
    cancel: true,
}).onOk(name => {
    createFolder(name)
})

// Options (radio selection)
$q.dialog({
    title: 'Select Option',
    message: 'Choose one:',
    options: {
        type: 'radio',
        model: 'option1',
        items: [
            { label: 'Option 1', value: 'option1' },
            { label: 'Option 2', value: 'option2' },
        ]
    },
    cancel: true,
}).onOk(val => {
    console.log('Selected:', val)
})
```

**Why it exists:** Dialogs interrupt the user for important decisions → can't be ignored. More forceful than notifications → for destructive actions, critical choices.

**Where it's used:** Delete confirmations, prompts, critical decisions, when you need a response before continuing.

**What goes wrong without it:**
- `persistent: true` → can't close by clicking outside or Esc → user must choose. Use for critical actions only.
- Not handling `onCancel` → user cancels but code assumes they confirmed → bug.
- Dialog inside dialog → confusing UX. Avoid nesting.

---

## Custom Dialog Components

**What:** Use your own Vue component as a dialog.

```js
// Custom dialog
$q.dialog({
    component: CustomDialogComponent,
    componentProps: {
        title: 'Custom Dialog',
        data: someData,
    },
}).onOk(payload => {
    console.log('Dialog returned:', payload)
})

// CustomDialogComponent.vue
<template>
    <q-dialog ref="dialog" @hide="onDialogHide">
        <q-card class="q-pa-md">
            <h3>{{ title }}</h3>
            <p>{{ data }}</p>
            <q-btn label="OK" @click="onOK" color="primary" />
            <q-btn label="Cancel" @click="onCancel" flat />
        </q-card>
    </q-dialog>
</template>

<script setup>
import { ref } from 'vue'
const props = defineProps(['title', 'data'])
const emit = defineEmits(['ok', 'hide'])

function onOK() {
    emit('ok', { result: 'confirmed' })
    dialogRef.value.hide()
}
function onCancel() {
    dialogRef.value.hide()
}
function onDialogHide() {
    emit('hide')
}
const dialogRef = ref(null)
</script>
```

**Why it exists:** Built-in dialogs (confirm, prompt) are limited. Custom dialogs → any UI → complex forms, images, charts inside a modal → unlimited flexibility.

**Where it's used:** Complex forms in a modal, image viewers, multi-step wizards in a dialog.

**What goes wrong without it:**
- Not emitting `ok` → `onOk` handler never fires → caller doesn't know the result.
- Not calling `hide()` → dialog stays open → user stuck.
- Forgetting `@hide` → dialog doesn't emit hide → caller can't clean up.

---

## QBottomSheet

**What:** A bottom sheet menu (common on mobile).

```js
$q.bottomSheet({
    title: 'Choose action',
    actions: [
        { label: 'Share', icon: 'share', id: 'share' },
        { label: 'Copy', icon: 'content_copy', id: 'copy' },
        { label: 'Delete', icon: 'delete', color: 'negative', id: 'delete' },
    ],
}).onOk(action => {
    console.log('Selected:', action.id)
})
```

**Why it exists:** On mobile, bottom sheets are more ergonomic than dialogs (thumb-friendly). Quasar provides this → native mobile feel → better UX on phones.

**Where it's used:** Mobile action menus, share sheets, item options.

**What goes wrong without it:**
- Using bottom sheet on desktop → unusual UX. Use dialogs or menus on desktop.
- Too many actions → long sheet → scroll. Limit to 5-7 actions.
- Not handling `onCancel` → user dismisses by swiping down → no handler → fine (no action needed).

---

## Loading Bar (QAjaxBar)

**What:** A loading bar at the top of the page (like YouTube/GitHub).

```vue
<!-- In AppLayout -->
<q-ajax-bar
    position="top"
    color="primary"
    size="5px"
    skip-hijack
/>

<!-- Triggers automatically on fetch/XHR -->
<!-- Or manually: -->
<script setup>
import { useQuasar } from 'quasar'
const $q = useQuasar()

$q.loadingBar.start()
// ... async operation ...
$q.loadingBar.stop()
</script>
```

**Why it exists:** Shows the user that something is loading → sets expectations → less perceived wait. QAjaxBar auto-detects XHR/fetch → zero configuration.

**Where it's used:** Every app with API calls → page loads, data fetches, route changes.

**What goes wrong without it:**
- Not calling `stop()` → bar stays at 100% → looks stuck. Always stop in `finally`.
- `skip-hijack` → prevents Quasar from delaying DOM updates during loading → usually what you want.
- Multiple start calls → bar fills multiple times. Match starts with stops.

---

## Combining Notifications and Dialogs

**What:** Use both together for a complete UX flow.

```js
async function deleteItem(item) {
    // Step 1: Confirm with dialog
    $q.dialog({
        title: 'Delete Item',
        message: `Delete "${item.name}"?`,
        ok: { color: 'negative', label: 'Delete' },
        cancel: true,
    }).onOk(async () => {
        // Step 2: Show loading
        const dismiss = $q.notify({ message: 'Deleting...', timeout: 0 })

        try {
            await api.delete(`/items/${item.id}`)

            // Step 3: Success with undo
            dismiss()
            $q.notify({
                type: 'positive',
                message: 'Item deleted',
                actions: [
                    { label: 'Undo', handler: () => undoDelete(item) }
                ],
                timeout: 5000,
            })
        } catch (error) {
            dismiss()
            $q.notify({ type: 'negative', message: 'Delete failed' })
        }
    })
}
```

**Why it exists:** Real-world flows combine multiple feedback types: dialog (confirm) → loading (wait) → notification (result). Understanding how to chain them → complete, polished UX.

**Where it's used:** Every destructive or multi-step operation.

**What goes wrong without it:**
- Not dismissing the loading notification before showing the result → two notifications overlap.
- Undo in the notification → needs the original item data → pass it to the handler.
- Not handling the cancel case → user cancels but loading shows → stuck. Only start loading after `onOk`.
