# Lesson 14 — Approach Comparison

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
