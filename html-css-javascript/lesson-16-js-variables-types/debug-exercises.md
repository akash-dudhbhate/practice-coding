# Lesson 16 — Debug Exercises

## Debug 01 (Easy): var Hoisting
```javascript
console.log(x);
var x = 5;
```
<details><summary>Answer</summary>
**Bug:** `var` is hoisted but not initialized. Prints `undefined`, not 5.
**Fix:** Use `let`/`const` — they're in the temporal dead zone (throws ReferenceError).
</details>

## Debug 02 (Medium): == vs ===
```javascript
console.log(0 == false);
console.log(0 === false);
```
<details><summary>Answer</summary>
`true`, `false`. `==` does type coercion (0 → false). `===` checks type AND value. Always use `===`.
</details>

## Debug 03 (Hard): const Object Mutation
```javascript
const obj = { x: 1 };
obj.x = 2;
obj = { x: 3 };
```
<details><summary>Answer</summary>
`obj.x = 2` works — const prevents reassignment of the variable, not mutation of the object. `obj = {...}` throws TypeError.
</details>
