# lesson-17-js-functions-control-flow — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Function declarations vs expressions
```javascript
function foo() {}        // declaration — hoisted
const bar = function(){}; // expression — not hoisted
const baz = () => {};    // arrow — no this, no arguments
```
<details><summary>Answer</summary>
Declarations are hoisted (can call before definition). Expressions are not. Arrow functions have no `this` binding.
</details>

## Check 02: Default parameters
```javascript
function greet(name = "Guest") {
  return `Hello, ${name}`;
}
console.log(greet());
```
<details><summary>Answer</summary>
`Hello, Guest` — default parameter used when argument is undefined.
</details>

## Check 03: Rest parameters
```javascript
function sum(...nums) {
  return nums.reduce((a, b) => a + b, 0);
}
console.log(sum(1, 2, 3));
```
<details><summary>Answer</summary>
`6` — `...nums` collects all arguments into an array. Replaces the old `arguments` object.
</details>

## Check 04: Ternary
```javascript
const status = age >= 18 ? "adult" : "minor";
```
<details><summary>Answer</summary>
If condition is true, value is "adult", else "minor". Shorthand for if/else.
</details>

## Check 05: Short-circuit evaluation
```javascript
const name = user?.name ?? "Anonymous";
```
<details><summary>Answer</summary>
Optional chaining (`?.`) — if user is null/undefined, doesn't throw. Nullish coalescing (`??`) — provides default for null/undefined. If user exists, use user.name, else "Anonymous".
</details>

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: Arrow functions for methods
```javascript
// WRONG — this is wrong
const obj = {
  greet: () => this.name  // this is not obj
};
// CORRECT
const obj = {
  greet() { return this.name; }
};
```

## Mistake 02: Missing break in switch
```javascript
// WRONG — falls through
switch (x) {
  case 1: doSomething();
  case 2: doOther();
}
// CORRECT
switch (x) {
  case 1: doSomething(); break;
  case 2: doOther(); break;
}
```

## Mistake 03: var in loops
```javascript
// WRONG — closure captures same i
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// CORRECT
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
```

## Mistake 04: Deeply nested if/else
```javascript
// WRONG — callback hell / nesting
// CORRECT — early returns
function process(x) {
  if (!x) return;
  if (x < 0) return;
  // main logic
}
```

## Mistake 05: Not using default parameters
```javascript
// VERBOSE
function greet(name) {
  name = name || "Guest";
  return `Hello, ${name}`;
}
// BETTER
function greet(name = "Guest") {
  return `Hello, ${name}`;
}
```

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

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
