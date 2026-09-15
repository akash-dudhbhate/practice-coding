# Lesson 19 — Refactoring Challenges

## Refactor 01 (Easy): Callback Instead of Promise
### Before
```javascript
navigator.geolocation.getCurrentPosition(pos => { ... });
```
### After
```javascript
const pos = await new Promise((res, rej) =>
  navigator.geolocation.getCurrentPosition(res, rej)
);
```

## Refactor 02 (Medium): Manual Interval
### Before
```javascript
setInterval(() => { if (done) clearInterval(id); }, 1000);
```
### After
```javascript
const check = async () => {
  while (!done) await new Promise(r => setTimeout(r, 1000));
};
```

## Refactor 03 (Hard): No AbortController
### Before
```javascript
const res = await fetch(url); // can't cancel
```
### After
```javascript
const ctrl = new AbortController();
setTimeout(() => ctrl.abort(), 5000);
const res = await fetch(url, { signal: ctrl.signal });
```
