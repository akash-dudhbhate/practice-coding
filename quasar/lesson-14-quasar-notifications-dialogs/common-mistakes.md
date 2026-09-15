# Lesson 14 — Common Mistakes

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
