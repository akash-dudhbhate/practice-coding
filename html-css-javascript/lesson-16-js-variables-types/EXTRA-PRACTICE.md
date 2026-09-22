# lesson-16-js-variables-types — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Constructor Function
### Before
```javascript
function User(name) { this.name = name; }
User.prototype.greet = function() { return "Hi " + this.name; };
```
### After
```javascript
class User {
  constructor(name) { this.name = name; }
  greet() { return `Hi ${this.name}`; }
}
```

## Refactor 02 (Medium): Prototype Methods
### Before
```javascript
function Animal(type) { this.type = type; }
Animal.prototype.sound = function() { return "..."; };
```
### After
```javascript
class Animal {
  constructor(type) { this.type = type; }
  sound() { return "..."; }
}
```

## Refactor 03 (Hard): Deep Inheritance
### Before
```javascript
class A {} class B extends A {} class C extends B {} class D extends C {}
```
### After
```javascript
class D { constructor() { this.a = new A(); this.b = new B(); } }
```

---

## Approach Comparison — different ways to solve it

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
