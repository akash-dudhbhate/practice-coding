# Lesson 16 — Concepts Explained (JS Variables & Data Types)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## let vs const vs var

**What:** Three ways to declare variables in JavaScript.

```javascript
let age = 25;          // mutable, block-scoped
age = 26;              // can reassign

const name = "Akash";  // immutable binding, block-scoped
// name = "Bob";       // ERROR: can't reassign const

var old = "legacy";    // mutable, function-scoped (AVOID)
```

**Why it exists:** `var` is the old way — function-scoped, hoisted, causes bugs. `let` and `const` were added in ES6 (2015) to fix `var`'s problems. `const` prevents accidental reassignment. `let` allows reassignment when needed.

**Where it's used:** `const` by default (80% of variables). `let` when you need to reassign (counters, loops). `var` — never in modern code.

**What goes wrong without it:**
- `var` is hoisted → accessible before declaration → `console.log(x); var x = 5;` → `undefined` (not error) → confusing bugs.
- `var` is function-scoped, not block-scoped → `if (true) { var x = 5; } console.log(x);` → `5` (leaks out of block) → bugs.
- `const` object: `const obj = {}; obj.name = "Akash";` → WORKS. `const` prevents reassignment of the VARIABLE, not mutation of the object. Common confusion.

---

## Data Types

**What:** JavaScript has 8 data types:

```javascript
// Primitives (immutable)
let str = "hello";           // String
let num = 42;                // Number (integers and floats)
let big = 9007199254740991n; // BigInt (very large numbers)
let bool = true;             // Boolean
let undef = undefined;       // Undefined (no value assigned)
let nothing = null;          // Null (intentional no value)
let sym = Symbol("id");      // Symbol (unique identifier)

// Non-primitive (mutable, passed by reference)
let obj = {name: "Akash"};   // Object
let arr = [1, 2, 3];         // Array (type of Object)
let func = function(){};     // Function (type of Object)
```

**Why it exists:** Different data needs different types. Text is a string, numbers are numbers, true/false is boolean. Understanding types prevents bugs — you can't do `"hello" * 2` meaningfully.

**Where it's used:** Every variable in JavaScript.

**What goes wrong without it:**
- `typeof null` → `"object"` (a JavaScript bug from 1995, never fixed). Use `=== null` to check for null.
- `typeof []` → `"object"`, not `"array"`. Use `Array.isArray()` to check for arrays.
- `0.1 + 0.2` → `0.30000000000000004` (floating point error). Use `Math.round()` or work in integers.

---

## Type Coercion

**What:** JavaScript automatically converts types in certain operations — often with surprising results.

```javascript
"5" + 3    // "53"  — number coerced to string (concatenation)
"5" - 3    // 2     — string coerced to number (subtraction)
"5" * "2"  // 10    — both coerced to numbers
true + 1   // 2     — true coerced to 1
false + 1  // 1     — false coerced to 0
null + 1   // 1     — null coerced to 0
undefined + 1 // NaN — undefined coerced to NaN
```

**Why it exists:** JavaScript was designed to be "forgiving" — it tries to make operations work instead of throwing errors. This was a design choice that leads to many bugs.

**Where it's used:** Unintentionally, everywhere. Understanding coercion prevents bugs.

**What goes wrong without it:**
- `"5" + 3` → `"53"` not `8` → user sees "53" instead of 8 → bug.
- `if ("0")` → `true` (non-empty string is truthy). `if (0)` → `false`. Know your truthy/falsy values.
- `NaN === NaN` → `false` (NaN is not equal to itself). Use `Number.isNaN()` to check.

---

## == vs ===

**What:**
- `==` (loose equality) — compares values AFTER type coercion.
- `===` (strict equality) — compares values AND types. No coercion.

```javascript
5 == "5"     // true  — "5" coerced to number 5
5 === "5"    // false — different types
0 == false   // true  — false coerced to 0
0 === false  // false — different types
null == undefined  // true  — loose equality treats them as equal
null === undefined // false — different types
```

**Why it exists:** `==` was the original equality operator. `===` was added because `==`'s coercion rules are confusing and cause bugs. Always use `===`.

**Where it's used:** Every comparison. Use `===` everywhere. ESLint rules enforce this.

**What goes wrong without it:**
- `if (value == null)` → true for both `null` AND `undefined` → might be intentional (checking for "no value") or a bug.
- `"" == 0` → `true` (empty string coerced to 0) → unexpected.
- `[] == false` → `true` (complex coercion rules) → very confusing. Always use `===`.

---

## Template Literals

**What:** Template literals use backticks (`` ` ``) instead of quotes. They support interpolation and multi-line strings.

```javascript
const name = "Akash";
const age = 25;

// Interpolation
const greeting = `Hello, ${name}! You are ${age} years old.`;

// Multi-line
const message = `
    Dear ${name},
    Your account is ${age} days old.
    Regards,
    Admin
`;

// Expressions
const result = `Total: ${10 + 20}`;   // "Total: 30"
```

**Why it exists:** Without template literals, you'd use string concatenation: `"Hello, " + name + "! You are " + age + " years old."` → hard to read, error-prone with quotes. Template literals are cleaner.

**Where it's used:** Everywhere strings need dynamic values — greetings, messages, HTML templates, URLs.

**What goes wrong without it:**
- Mixing quotes: `"He said \"hello\""` → escaping is annoying. Template literals: `` `He said "hello"` `` → no escaping needed.
- Multi-line with `\n`: `"Line1\nLine2"` → hard to read. Template literals handle real line breaks.
- Nested backticks: `` `Outer ${`inner`}` `` → works but gets complex. Avoid deep nesting.

---

## String Methods

**What:** Built-in methods for string manipulation.

```javascript
let str = "Hello, World";

str.length              // 12
str.toUpperCase()       // "HELLO, WORLD"
str.toLowerCase()       // "hello, world"
str.includes("World")   // true
str.startsWith("Hello") // true
str.endsWith("World")   // true
str.indexOf("o")        // 4 (first occurrence)
str.replace("World", "JS") // "Hello, JS"
str.split(", ")         // ["Hello", "World"]
str.trim()              // removes whitespace from ends
str.slice(0, 5)         // "Hello" (start, end)
str.substring(0, 5)     // "Hello" (similar to slice)
str.repeat(3)           // "Hello, WorldHello, WorldHello, World"
```

**Why it exists:** Without these methods, you'd write loops to find, replace, or split strings → verbose. Built-in methods are optimized and readable.

**Where it's used:** Form validation, data parsing, URL manipulation, text processing.

**What goes wrong without it:**
- Strings are IMMUTABLE: `str.toUpperCase()` returns a NEW string, doesn't modify `str`. Forgetting to assign: `str.toUpperCase(); console.log(str);` → still lowercase.
- `slice` vs `substring`: `slice(-3)` gets last 3 chars. `substring(-3)` treats -3 as 0. Use `slice`.
- `replace` replaces only the FIRST match. Use `replaceAll()` or regex with `/g` flag for all matches.

---

## Number Methods & Math

**What:** Number manipulation and the Math object.

```javascript
// Number methods
let num = 3.14159;
num.toFixed(2)          // "3.14" (returns string!)
num.toString()          // "3.14159"
parseInt("42px")        // 42 (parses leading number)
parseFloat("3.14abc")   // 3.14
Number("42")            // 42 (strict conversion)

// Math object
Math.round(3.7)         // 4
Math.floor(3.7)         // 3
Math.ceil(3.2)          // 4
Math.max(1, 2, 3)       // 3
Math.min(1, 2, 3)       // 1
Math.random()           // 0-0.999...
Math.floor(Math.random() * 10)  // 0-9 (random integer)
Math.abs(-5)            // 5
Math.pow(2, 3)          // 8 (2^3)
Math.sqrt(16)           // 4
```

**Why it exists:** Without Math, you'd implement rounding, random, and power functions yourself → error-prone. Math provides these optimized.

**Where it's used:** Calculations, games (random), formatting (toFixed), data processing.

**What goes wrong without it:**
- `toFixed(2)` returns a STRING, not a number. `3.14 + "1.00"` → `"3.141.00"` (string concatenation). Convert back: `Number(num.toFixed(2))`.
- `parseInt("3.14")` → `3` (truncates). Use `parseFloat` for decimals.
- `Math.random()` → 0 to 0.999... NEVER returns 1. For 1-10: `Math.floor(Math.random() * 10) + 1`.

---

## Boolean & Truthy/Falsy

**What:** JavaScript values are "truthy" or "falsy" in boolean context.

```javascript
// Falsy values (6 total)
false, 0, "", null, undefined, NaN

// Everything else is truthy
"hello"   // truthy (non-empty string)
1         // truthy (non-zero number)
[]        // truthy (empty array!)
{}        // truthy (empty object!)
"0"       // truthy (non-empty string)
"false"   // truthy (non-empty string)
```

**Why it exists:** Understanding truthy/falsy is essential for `if` conditions. `if (value)` checks if value is truthy. Knowing which values are falsy prevents bugs.

**Where it's used:** Every `if` statement, `while` loop, ternary operator, logical operators (`&&`, `||`).

**What goes wrong without it:**
- `if ([])` → `true` (empty array is truthy) → unexpected if you expected empty array to be falsy. Use `if (arr.length > 0)`.
- `if ("0")` → `true` (non-empty string) → unexpected if you expected "0" to be falsy.
- `if (0)` → `false`. `if ("0")` → `true`. The string "0" is truthy, the number 0 is falsy. Confusing but important.

---

## typeof Operator

**What:** Returns the type of a value as a string.

```javascript
typeof "hello"      // "string"
typeof 42           // "number"
typeof true         // "boolean"
typeof undefined    // "undefined"
typeof null         // "object" (BUG — should be "null")
typeof {}           // "object"
typeof []           // "object" (not "array")
typeof function(){} // "function"
typeof Symbol()     // "symbol"
```

**Why it exists:** Without `typeof`, you can't check a value's type at runtime → can't write type-dependent code. `typeof` is the standard way to check types.

**Where it's used:** Type checking, validation, debugging, conditional logic.

**What goes wrong without it:**
- `typeof null` → `"object"` (a 25-year-old bug). Use `value === null` to check for null.
- `typeof []` → `"object"`. Use `Array.isArray(value)` to check for arrays.
- `typeof` on undeclared variable → `"undefined"` (doesn't throw). This is actually useful for feature detection: `if (typeof jQuery !== "undefined")`.
