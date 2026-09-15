# Lesson 16 — Common Mistakes

## Mistake 01: Using var
```javascript
// WRONG — function scoped, hoisted
var x = 5;
// CORRECT — block scoped
let x = 5;
const y = 10;
```

## Mistake 02: == instead of ===
```javascript
// WRONG — type coercion
if (x == "5") {}
// CORRECT — strict equality
if (x === "5") {}
```

## Mistake 03: let when const works
```javascript
// WRONG — doesn't change
let PI = 3.14159;
// CORRECT
const PI = 3.14159;
```

## Mistake 04: Confusing null and undefined
```javascript
// null — intentionally empty
// undefined — not yet assigned
let x;        // undefined
let y = null; // explicitly null
```

## Mistake 05: Not checking for NaN properly
```javascript
// WRONG — NaN !== NaN
if (x === NaN) {}
// CORRECT
if (Number.isNaN(x)) {}
```
