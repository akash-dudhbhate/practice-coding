# Lesson 16 — Approach Comparison

## Problem: Variable Declaration

### Approach 1: var
```javascript
var x = 5;
```
**Cons:** Function-scoped, hoisted, error-prone.

### Approach 2: let/const
```javascript
const x = 5;
let y = 10;
```
**Pros:** Block-scoped, temporal dead zone, safer.

**Winner:** Approach 2 — always use const/let, never var.

---

## Problem: String Concatenation

### Approach 1: + operator
```javascript
const msg = "Hello, " + name + "! You are " + age + " years old.";
```

### Approach 2: Template literals
```javascript
const msg = `Hello, ${name}! You are ${age} years old.`;
```

**Winner:** Approach 2 — readable, supports multi-line.
