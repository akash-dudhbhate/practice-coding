# lesson-14-quasar-notifications-dialogs — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Notify options
```javascript
$q.notify({
  message: "Saved!",
  type: "positive",
  position: "top-right",
  timeout: 3000,
  actions: [{ label: "Undo", color: "white", handler: undo }]
});
```
<details><summary>Answer</summary>
`type` — positive/negative/warning/info. `position` — top/bottom/top-right. `timeout` — ms before dismiss. `actions` — buttons in notification.
</details>

## Check 02: Dialog types
```javascript
$q.dialog({ title: "Title", message: "Message", cancel: true, persistent: true });
```
<details><summary>Answer</summary>
`cancel` — show cancel button. `persistent` — can't dismiss by clicking outside. `ok` — custom OK button.
</details>

## Check 03: Loading bar
```javascript
$q.loadingBar.start();
await fetchData();
$q.loadingBar.stop();
```
<details><summary>Answer</summary>
Top progress bar. Start/stop for async operations. Shows progress without blocking UI.
</details>

## Check 04: Bottom sheet
```javascript
$q.bottomSheet({
  actions: [
    { label: "Share", icon: "share", id: "share" },
    { label: "Delete", icon: "delete", id: "delete" }
  ]
}).onOk(action => { /* action.id */ });
```
<details><summary>Answer</summary>
Mobile-style action sheet. List of actions with icons. User selects one. Good for mobile UX.
</details>

## Check 05: Persistent notification
```javascript
const notif = $q.notify({ message: "Uploading...", timeout: 0 });
// later
notif(); // dismiss
```
<details><summary>Answer</summary>
`timeout: 0` — stays until dismissed. Returns dismiss function. Good for long operations.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01: Notify Not Registered
```javascript
$q.notify("Hello"); // $q.notify is undefined
```
<details><summary>Answer</summary>
**Bug:** Notify plugin not in quasar.config.js.
**Fix:** `framework: { plugins: ["Notify"] }`.
</details>

## Debug 02: Dialog Not Awaited
```javascript
$q.dialog({ title: "Confirm" });
// code continues immediately
```
<details><summary>Answer</summary>
**Bug:** Dialog is async, code doesn't wait for user response.
**Fix:** Use `.onOk()`: `$q.dialog({...}).onOk(() => { /* after confirm */ })`.
</details>

## Debug 03: Multiple Notifications Stacking
```javascript
$q.notify("A");
$q.notify("B");
$q.notify("C"); // 3 toasts stack up
```
<details><summary>Answer</summary>
**Issue:** Multiple notifications clutter screen.
**Fix:** Use `group: false` to prevent grouping, or `timeout` to auto-dismiss.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Not registering plugins
```javascript
// quasar.config.js
framework: { plugins: ["Notify", "Dialog"] }
```

## Mistake 02: Using alert/confirm
```javascript
// WRONG
alert("Error"); confirm("Sure?");
// CORRECT
$q.notify({ type: "negative", message: "Error" });
$q.dialog({ title: "Sure?", cancel: true });
```

## Mistake 03: Not dismissing loading
```javascript
// WRONG — stuck loading
$q.loading.show(); await fetch();
// CORRECT
try { $q.loading.show(); await fetch(); }
finally { $q.loading.hide(); }
```

## Mistake 04: Too many notifications
```javascript
// Use group or timeout to prevent clutter
```

## Mistake 05: Not handling dialog cancel
```javascript
$q.dialog({...}).onOk(doIt).onCancel(() => {});
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): alert/confirm
### Before
```javascript
alert("Error"); if (confirm("Sure?")) doIt();
```
### After
```javascript
$q.notify({ type: "negative", message: "Error" });
$q.dialog({ title: "Sure?", cancel: true }).onOk(doIt);
```

## Refactor 02 (Medium): Not Dismissing Loading
### Before
```javascript
$q.loading.show(); await fetch();
```
### After
```javascript
try { $q.loading.show(); await fetch(); } finally { $q.loading.hide(); }
```

## Refactor 03 (Hard: Not Handling Cancel
### Before
```javascript
$q.dialog({ title: "Delete?" }).onOk(deleteIt);
```
### After
```javascript
$q.dialog({ title: "Delete?", cancel: true }).onOk(deleteIt).onCancel(() => {});
```

---

## Approach Comparison — different ways to solve it

## Problem: User Feedback

### Approach 1: alert
```javascript
alert("Done!");
```

### Approach 2: $q.notify
```javascript
$q.notify({ message: "Done!", type: "positive" });
```

**Winner:** Approach 2 — non-blocking, styled.

---

## Problem: Confirmation

### Approach 1: confirm
```javascript
if (confirm("Delete?")) deleteIt();
```

### Approach 2: $q.dialog
```javascript
$q.dialog({ title: "Delete?", cancel: true }).onOk(deleteIt);
```

**Winner:** Approach 2 — async, styled, customizable.
