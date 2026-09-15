# Lesson 18 — Common Mistakes

## Mistake 01: forEach when you need map
```javascript
// WRONG — returns undefined
const doubled = arr.forEach(x => x * 2);
// CORRECT
const doubled = arr.map(x => x * 2);
```

## Mistake 02: Mutating with map
```javascript
// WRONG — mutates original
arr.map(obj => { obj.x = 1; return obj; });
// CORRECT
arr.map(obj => ({ ...obj, x: 1 }));
```

## Mistake 03: sort without compare function
```javascript
// WRONG — sorts as strings
[10, 2, 1].sort(); // [1, 10, 2]
// CORRECT
[10, 2, 1].sort((a, b) => a - b); // [1, 2, 10]
```

## Mistake 04: Not spreading
```javascript
// WRONG — nested array
const combined = [arr1, arr2];
// CORRECT
const combined = [...arr1, ...arr2];
```

## Mistake 05: Chaining after forEach
```javascript
// WRONG — forEach returns undefined
arr.forEach(x => x * 2).filter(...);
// CORRECT — use map
arr.map(x => x * 2).filter(...);
```
