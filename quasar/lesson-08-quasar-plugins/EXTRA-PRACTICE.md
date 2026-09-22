# lesson-08-quasar-plugins — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Plugin Not Registered
```javascript
// quasar.config.js
framework: { plugins: [] }  // Notify not listed
```
```javascript
this.$q.notify("Hello"); // error
```
<details><summary>Answer</summary>
**Bug:** Notify plugin not registered in config.
**Fix:** `framework: { plugins: ["Notify"] }`.
</details>

## Debug 02 (Medium: Dialog Without Promise
```javascript
this.$q.dialog({
  title: "Confirm",
  cancel: true,
  persistent: true
}).onOk(() => { /* handle */ });
// no onCancel
```
<details><summary>Answer</summary>
**Issue:** No cancel handler — user cancels, nothing happens (may be intended, but usually want to handle).
**Fix:** Add `.onCancel(() => { ... })`.
</details>

## Debug 03 (Hard: Loading Not Stopped
```javascript
this.$q.loading.show();
await fetchData();
// forgot this.$q.loading.hide()
```
<details><summary>Answer</summary>
**Bug:** Loading indicator never hidden.
**Fix:** Use try/finally: `try { await fetchData(); } finally { this.$q.loading.hide(); }`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Not registering plugins
```javascript
// WRONG — not in config
framework: { plugins: [] }
// CORRECT
framework: { plugins: ["Notify", "Dialog"] }
```

## Mistake 02: Not hiding loading
```javascript
// WRONG — stays forever
$q.loading.show();
await fetch();
// CORRECT
try { $q.loading.show(); await fetch(); }
finally { $q.loading.hide(); }
```

## Mistake 03: Using alert instead of Notify
```javascript
// WRONG — blocks UI
alert("Saved!");
// CORRECT
$q.notify("Saved!");
```

## Mistake 04: Not handling dialog cancel
```javascript
// Add onCancel for complete UX
$q.dialog({...}).onOk(...).onCancel(...);
```

## Mistake 05: Not restarting after config change
```bash
# After changing quasar.config.js plugins
# Restart: quasar dev
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): alert
### Before
```javascript
alert("Saved!");
```
### After
```javascript
$q.notify({ message: "Saved!", type: "positive" });
```

## Refactor 02 (Medium): confirm
### Before
```javascript
if (confirm("Delete?")) deleteItem();
```
### After
```javascript
$q.dialog({ title: "Delete?", cancel: true }).onOk(deleteItem);
```

## Refactor 03 (Hard: No Loading Cleanup
### Before
```javascript
$q.loading.show();
await fetchData();
// forgot hide
```
### After
```javascript
try { $q.loading.show(); await fetchData(); }
finally { $q.loading.hide(); }
```

---

## Approach Comparison — different ways to solve it

## Problem: Show Notification

### Approach 1: alert
```javascript
alert("Saved!");
```
**Cons:** Blocks UI, ugly, not dismissible.

### Approach 2: $q.notify
```javascript
$q.notify({ message: "Saved!", type: "positive" });
```

**Winner:** Approach 2 — non-blocking, styled, auto-dismiss.

---

## Problem: Confirmation

### Approach 1: confirm
```javascript
if (confirm("Delete?")) deleteItem();
```
**Cons:** Blocks, ugly, not customizable.

### Approach 2: $q.dialog
```javascript
$q.dialog({ title: "Delete?", cancel: true }).onOk(deleteItem);
```

**Winner:** Approach 2 — async, styled, customizable.
