# Lesson 17 — Concepts Explained (JS Functions & Control Flow)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Function Declarations vs Expressions

**What:** Two ways to define functions in JavaScript.

```javascript
// Function declaration — hoisted (can be called before definition)
function greet(name) {
    return `Hello, ${name}`;
}

// Function expression — NOT hoisted (can't call before definition)
const greet = function(name) {
    return `Hello, ${name}`;
};

// Arrow function (ES6) — concise, no own `this`
const greet = (name) => `Hello, ${name}`;
```

**Why it exists:** Declarations are hoisted (available anywhere in scope) → good for top-level functions. Expressions are not hoisted → good for controlled usage. Arrow functions are concise → good for callbacks.

**Where it's used:** Declarations for main functions. Expressions for functions assigned to variables. Arrow functions for callbacks (map, filter, setTimeout).

**What goes wrong without it:**
- Calling a function expression before declaration → `ReferenceError: Cannot access 'greet' before initialization`.
- Declarations are hoisted → `greet()` works even before `function greet(){}` in the file → can be confusing.
- Arrow functions don't have their own `this` → using them as object methods → `this` refers to outer scope, not the object → bugs.

---

## Arrow Functions

**What:** Concise function syntax with implicit return and no `this` binding.

```javascript
// Regular function
const add = function(a, b) { return a + b; };

// Arrow function — same thing
const add = (a, b) => { return a + b; };

// Implicit return (no braces)
const add = (a, b) => a + b;

// Single parameter (no parens needed)
const square = x => x * x;

// No parameters
const greet = () => "Hello!";

// Returning an object (wrap in parens)
const makeUser = (name, age) => ({ name, age });
```

**Why it exists:** Arrow functions are shorter and don't bind their own `this`. Before arrow functions, callbacks needed `.bind(this)` or `const self = this` workarounds → verbose and error-prone.

**Where it's used:** Callbacks (map, filter, reduce, sort), setTimeout, event handlers, any short function.

**What goes wrong without it:**
- `const obj = { method: () => this.value }` → `this` is NOT the object → `this.value` is undefined. Don't use arrow functions for object methods.
- `const makeUser = (name) => { name }` → returns `undefined` (no return statement). Use `=> ({ name })` for implicit object return.
- Arrow functions can't be used as constructors: `new ArrowFunc()` → `TypeError`.

---

## Default Parameters

**What:** Set default values for function parameters.

```javascript
function greet(name = "Guest", greeting = "Hello") {
    return `${greeting}, ${name}!`;
}

greet()               // "Hello, Guest!"
greet("Akash")        // "Hello, Akash!"
greet("Akash", "Hi")  // "Hi, Akash!"
greet(undefined, "Hi") // "Hi, Guest!" (undefined triggers default)
```

**Why it exists:** Without defaults, missing arguments are `undefined` → `Hello, undefined!` → ugly. Before ES6, you'd write `name = name || "Guest"` → breaks if name is `0` or `""`.

**Where it's used:** Any function with optional parameters.

**What goes wrong without it:**
- `null` does NOT trigger the default: `greet(null)` → `Hello, null!`. Only `undefined` triggers defaults.
- Default parameters are evaluated at call time: `function f(x = expensiveOp())` → `expensiveOp()` runs every call → performance issue.
- Order matters: `function f(a = 1, b)` → `f(undefined, 2)` → `a=1, b=2`. But `f(2)` → `a=2, b=undefined` (no default for b).

---

## Rest Parameters (...args)

**What:** Collect any number of arguments into an array.

```javascript
function sum(...numbers) {
    return numbers.reduce((a, b) => a + b, 0);
}

sum(1, 2, 3)       // 6
sum(1, 2, 3, 4, 5) // 15

// With regular parameters
function greet(greeting, ...names) {
    names.forEach(name => console.log(`${greeting}, ${name}`));
}
greet("Hi", "Akash", "Bob", "Carol");  // "Hi, Akash" "Hi, Bob" "Hi, Carol"
```

**Why it exists:** Before rest parameters, you used `arguments` (an array-like object, not a real array → no `.map()`, `.reduce()`). Rest parameters give a real array → all array methods work.

**Where it's used:** Variadic functions (sum, max, min), function that accepts any number of items, wrapping/proxying functions.

**What goes wrong without it:**
- `arguments` is not an array → `arguments.map()` → `TypeError`. Use rest params or `Array.from(arguments)`.
- Rest parameter must be LAST: `function f(...args, last)` → `SyntaxError`. Only one rest parameter allowed.
- `...` is also spread syntax (different context). `function(...args)` = rest (collect). `callFunc(...arr)` = spread (expand).

---

## Spread Operator (...)

**What:** Expand an array or object into individual elements.

```javascript
// Array spread
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];  // [1, 2, 3, 4, 5]
const copy = [...arr1];         // shallow copy

// Object spread
const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 }; // { a: 1, b: 2, c: 3 }
const merged = { ...obj1, ...obj2 }; // later properties override

// Function arguments
const nums = [3, 1, 2];
Math.max(...nums);  // 3 (same as Math.max(3, 1, 2))
```

**Why it exists:** Without spread, you'd use `.concat()`, `Object.assign()`, or `apply()` → verbose. Spread is cleaner and more readable.

**Where it's used:** Merging arrays/objects, copying arrays, passing array elements as arguments, immutably updating state (React).

**What goes wrong without it:**
- Spread is a SHALLOW copy: `const copy = [...arr]` → nested arrays/objects are still references → mutating copy's nested element mutates original. Use `structuredClone()` for deep copy.
- Object spread: later properties override earlier: `{ ...{a: 1}, a: 2 }` → `{ a: 2 }`. Use this for overrides.
- Spreading `null` or `undefined`: `{ ...null }` → `{}` (no error). `[...null]` → `TypeError`.

---

## Destructuring

**What:** Extract values from arrays or objects into variables.

```javascript
// Array destructuring
const [first, second, third] = [1, 2, 3];
const [a, , c] = [1, 2, 3];      // skip second: a=1, c=3
const [first, ...rest] = [1, 2, 3, 4];  // first=1, rest=[2,3,4]

// Object destructuring
const { name, age } = { name: "Akash", age: 25 };
const { name: fullName } = { name: "Akash" };  // rename: fullName = "Akash"
const { city = "Unknown" } = { name: "Akash" }; // default: city = "Unknown"

// Function parameters
function greet({ name, age = 20 }) {
    return `${name}, ${age}`;
}
greet({ name: "Akash" });  // "Akash, 20"

// Nested destructuring
const { user: { name } } = { user: { name: "Akash" } };
```

**Why it exists:** Without destructuring, you'd write `const name = obj.name; const age = obj.age;` → verbose. Destructuring does it in one line.

**Where it's used:** React (props, state), API responses, function parameters, configuration objects.

**What goes wrong without it:**
- Order matters for arrays: `const [a, b] = [1, 2]` → `a=1, b=2`. Names don't matter, positions do.
- Names matter for objects: `const { name } = obj` → looks for `obj.name`. `const { fullName } = obj` → looks for `obj.fullName` → undefined if not present.
- Destructuring `null` or `undefined` → `TypeError: Cannot destructure property 'x' of 'null'`. Add a default: `const { name } = obj || {}`.

---

## if/else and switch

**What:** Conditional execution.

```javascript
// if/else if/else
if (score >= 90) { grade = "A"; }
else if (score >= 80) { grade = "B"; }
else if (score >= 70) { grade = "C"; }
else { grade = "F"; }

// switch (good for discrete values)
switch (day) {
    case "Monday":
    case "Tuesday":
        console.log("Work");
        break;                    // DON'T FORGET break!
    case "Saturday":
        console.log("Weekend");
        break;
    default:
        console.log("Other");
}
```

**Why it exists:** Without conditionals, code always runs the same way. `if/else` for range checks, `switch` for discrete value matching.

**Where it's used:** Every program — routing, validation, feature flags, user roles.

**What goes wrong without it:**
- Forgetting `break` in switch → falls through to next case → multiple cases execute → bugs. Always use `break` (unless intentional fall-through).
- `switch` uses `===` for comparison → `switch("5")` doesn't match `case 5`. Type must match.
- `if (x = 5)` → assignment, not comparison → always true. Use `===` for comparison.

---

## Ternary Operator

**What:** One-line conditional expression.

```javascript
const message = age >= 18 ? "Adult" : "Minor";
// condition ? valueIfTrue : valueIfFalse

// Nested (avoid deep nesting)
const grade = score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : "F";
```

**Why it exists:** Without ternary, simple conditionals need 4 lines of if/else. Ternary does it in one → cleaner for simple cases.

**Where it's used:** JSX (React), assigning values conditionally, template literals.

**What goes wrong without it:**
- Nested ternaries → `a ? b : c ? d : e` → hard to read. Use if/else for complex logic.
- Ternary is an EXPRESSION (returns a value), not a statement. `if` is a statement. Can't do `if (x) ? a : b` → syntax error.
- Side effects in ternary: `cond ? doX() : doY()` → works but bad practice → use if/else for side effects.

---

## for, while, for...of, for...in

**What:** Loops in JavaScript.

```javascript
// Classic for loop
for (let i = 0; i < 5; i++) { console.log(i); }

// while loop
let i = 0;
while (i < 5) { console.log(i); i++; }

// for...of — iterate values of an array/string/iterable
for (const item of [1, 2, 3]) { console.log(item); }  // 1, 2, 3
for (const char of "hello") { console.log(char); }     // h, e, l, l, o

// for...in — iterate keys of an object (AVOID for arrays)
for (const key in { a: 1, b: 2 }) { console.log(key); }  // "a", "b"
```

**Why it exists:** Different loops for different needs. `for` when you need the index. `for...of` when you just need values. `while` for unknown iteration counts.

**Where it's used:** Every program that processes collections.

**What goes wrong without it:**
- `for...in` on arrays → iterates keys ("0", "1", "2") not values, and includes inherited properties → wrong. Use `for...of` for arrays.
- `for...of` on objects → `TypeError: obj is not iterable`. Use `for...in` or `Object.entries()` for objects.
- Infinite loop: `while (true) { }` without a `break` → freezes the page. Always have an exit condition.

---

## break and continue

**What:** Control loop flow.

```javascript
// break — exit the loop entirely
for (let i = 0; i < 10; i++) {
    if (i === 5) break;    // stops at 5
    console.log(i);         // 0, 1, 2, 3, 4
}

// continue — skip this iteration, go to next
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) continue;  // skip even numbers
    console.log(i);              // 1, 3, 5, 7, 9
}
```

**Why it exists:** Without `break`, you can't exit a loop early (found what you're looking for). Without `continue`, you'd nest everything in an `if` → deep indentation.

**Where it's used:** Search loops (break when found), filtering (continue to skip), validation.

**What goes wrong without it:**
- `break` only exits the INNER loop. In nested loops, outer loop continues. Use labels for outer loop break: `outer: for(...) { for(...) { break outer; } }`.
- `continue` in a `while` loop → if the increment is after `continue`, it's skipped → infinite loop. Always increment before `continue`.
- Overusing `break`/`continue` → hard to follow loop logic. Use them sparingly.
