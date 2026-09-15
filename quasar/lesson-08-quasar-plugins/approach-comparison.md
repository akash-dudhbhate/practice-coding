# Lesson 08 — Approach Comparison

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
