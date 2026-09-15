# Lesson 17 — Refactoring Challenges

## Refactor 01 (Easy): for Loop to Map
### Before
```javascript
const result = [];
for (let i = 0; i < arr.length; i++) result.push(arr[i] * 2);
```
### After
```javascript
const result = arr.map(x => x * 2);
```

## Refactor 02 (Medium): Mutation
### Before
```javascript
arr.sort(); arr.reverse(); arr.push(5);
```
### After
```javascript
const sorted = [...arr].sort().reverse().concat(5);
```

## Refactor 03 (Hard): Chained Loops
### Before
```javascript
let result = [];
for (const x of arr) if (x > 0) result.push(x);
result = result.map(x => x * 2);
const total = result.reduce((s, x) => s + x, 0);
```
### After
```javascript
const total = arr.filter(x => x > 0).map(x => x * 2).reduce((s, x) => s + x, 0);
```
