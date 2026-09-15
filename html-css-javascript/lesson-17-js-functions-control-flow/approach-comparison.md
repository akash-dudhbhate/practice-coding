# Lesson 17 — Approach Comparison

## Problem: Callback Function

### Approach 1: Regular function
```javascript
button.addEventListener("click", function() {
  console.log(this); // the button
});
```

### Approach 2: Arrow function
```javascript
button.addEventListener("click", () => {
  console.log(this); // outer scope
});
```

**Winner:** Depends. Arrow when you want outer `this`. Regular when you need the element as `this`.

---

## Problem: Multiple Conditions

### Approach 1: if/else chain
```javascript
if (x === "a") return 1;
else if (x === "b") return 2;
else if (x === "c") return 3;
```

### Approach 2: Object lookup
```javascript
const map = { a: 1, b: 2, c: 3 };
return map[x];
```

**Winner:** Approach 2 — cleaner, O(1), easy to extend.
