# Lesson 18 — Approach Comparison

## Problem: Transform Array

### Approach 1: for loop
```javascript
const result = [];
for (let i = 0; i < arr.length; i++) {
  result.push(arr[i] * 2);
}
```

### Approach 2: map
```javascript
const result = arr.map(x => x * 2);
```

**Winner:** Approach 2 — declarative, immutable, chainable.

---

## Problem: Unique Values

### Approach 1: filter + indexOf
```javascript
arr.filter((x, i) => arr.indexOf(x) === i);
```

### Approach 2: Set
```javascript
[...new Set(arr)];
```

**Winner:** Approach 2 — cleaner, faster.
