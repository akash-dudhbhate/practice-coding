# Lesson 16 — Intuition Checks

## Check 01: let vs const vs var
When should you use each?
<details><summary>Answer</summary>
- `const` — default, for values that don't get reassigned
- `let` — when you need to reassign (counters, loops)
- `var` — never (legacy, has scoping issues)
</details>

## Check 02: Type coercion
```javascript
console.log("5" + 3);
console.log("5" - 3);
```
<details><summary>Answer</summary>
`"53"` (string concatenation), `2` (numeric subtraction). `+` coerces to string if either operand is string. `-` coerces to number.
</details>

## Check 03: typeof
```javascript
console.log(typeof null);
console.log(typeof []);
console.log(typeof {});
```
<details><summary>Answer</summary>
`"object"`, `"object"`, `"object"`. `typeof null` is a historical bug. Arrays and objects are both "object". Use `Array.isArray()` for arrays.
</details>

## Check 04: Template literals
```javascript
const name = "Akash";
console.log(`Hello, ${name}!`);
```
<details><summary>Answer</summary>
`Hello, Akash!` — template literals use backticks and `${}` for interpolation. Multi-line strings also work.
</details>

## Check 05: Truthy/Falsy
Which values are falsy in JS?
<details><summary>Answer</summary>
`false`, `0`, `""`, `null`, `undefined`, `NaN`, `0n` (BigInt). Everything else is truthy (including `[]`, `{}`, `"0"`).
</details>
