# Lesson 14 — Intuition Checks

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
