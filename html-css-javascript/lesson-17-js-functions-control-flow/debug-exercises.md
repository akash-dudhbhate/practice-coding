# Lesson 17 — Debug Exercises

## Debug 01 (Easy): Arrow Function this
```javascript
const obj = {
  name: "Akash",
  greet: () => console.log(this.name)
};
obj.greet();
```
<details><summary>Answer</summary>
**Bug:** Arrow functions don't have their own `this`. `this` is the outer scope (window/undefined). Prints undefined.
**Fix:** Use regular function: `greet() { console.log(this.name); }`.
</details>

## Debug 02 (Medium): Switch Missing Break
```javascript
switch (day) {
  case "Monday":
    console.log("Start of week");
  case "Tuesday":
    console.log("Day 2");
}
```
<details><summary>Answer</summary>
**Bug:** Missing `break` — falls through. On Monday, prints both messages.
**Fix:** Add `break;` after each case.
</details>

## Debug 03 (Hard): Closure in Loop
```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
```
<details><summary>Answer</summary>
**Bug:** Prints 3, 3, 3. `var` is function-scoped — all callbacks share the same `i` (which is 3 by the time they run).
**Fix:** Use `let i` (block-scoped) or IIFE.
</details>
