# Lesson 08 — Debug Exercises

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
