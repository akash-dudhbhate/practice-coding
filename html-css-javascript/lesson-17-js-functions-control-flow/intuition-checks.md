# Lesson 17 — Intuition Checks

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
