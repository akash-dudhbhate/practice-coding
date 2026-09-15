# Lesson 10 — Refactoring Challenges

## Refactor 01 (Easy): Nested Promises
### Before
```javascript
fetch(url).then(res => {
  fetch(url2).then(res2 => {
    // callback hell
  });
});
```
### After
```javascript
const res1 = await fetch(url);
const res2 = await fetch(url2);
```

## Refactor 02 (Medium): No Error Handling
### Before
```javascript
const data = await fetch(url).then(r => r.json());
```
### After
```javascript
try {
  const res = await fetch(url);
  if (!res.ok) throw new Error("Failed");
  const data = await res.json();
} catch (e) { console.error(e); }
```

## Refactor 03 (Hard): Sequential Awaits
### Before
```javascript
const a = await fetch(url1);
const b = await fetch(url2);
```
### After
```javascript
const [a, b] = await Promise.all([fetch(url1), fetch(url2)]);
```
