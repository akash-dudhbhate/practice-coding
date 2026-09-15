# Lesson 08 — Intuition Checks

## Check 01: What are Quasar plugins?
<details><summary>Answer</summary>
JavaScript utilities accessed via `$q`: Notify, Dialog, Loading, BottomSheet, AppFullscreen, DarkMode, Screen, Cookies, etc. Not Vue plugins — Quasar-specific.
</details>

## Check 02: Notify
```javascript
$q.notify({ message: "Saved!", type: "positive", position: "top" });
```
<details><summary>Answer</summary>
Shows toast notification. `type`: positive, negative, warning, info. `position`: top, bottom, top-right, etc. Auto-dismisses after timeout.
</details>

## Check 03: Dialog
```javascript
$q.dialog({ title: "Delete?", message: "Are you sure?", cancel: true })
  .onOk(() => deleteItem())
  .onCancel(() => console.log("cancelled"));
```
<details><summary>Answer</summary>
Programmatic dialog. Returns chainable API. `onOk`, `onCancel`, `onDismiss`. Good for confirmations.
</details>

## Check 04: Loading
```javascript
$q.loading.show({ message: "Saving..." });
// do work
$q.loading.hide();
```
<details><summary>Answer</summary>
Full-screen loading spinner. Always hide in finally block. Can customize spinner, message.
</details>

## Check 05: Registering plugins
```javascript
// quasar.config.js
framework: {
  plugins: ["Notify", "Dialog", "Loading"]
}
```
<details><summary>Answer</summary>
Must list plugins in config. Otherwise `$q.notify` etc. not available. Restart dev server after changing.
</details>
