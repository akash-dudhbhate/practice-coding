# Lesson 08 — Refactoring Challenges

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
