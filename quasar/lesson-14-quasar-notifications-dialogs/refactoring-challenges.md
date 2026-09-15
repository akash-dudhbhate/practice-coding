# Lesson 14 — Refactoring Challenges

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
