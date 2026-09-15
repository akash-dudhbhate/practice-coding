# Lesson 08 — Common Mistakes

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
