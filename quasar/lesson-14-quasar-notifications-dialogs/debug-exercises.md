# Lesson 14 — Debug Exercises

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
