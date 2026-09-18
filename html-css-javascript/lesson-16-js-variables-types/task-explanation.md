# Lesson 16 — JS Variables & Data Types

## What you'll learn
- let vs const vs var
- JavaScript data types (primitives vs objects)
- Type coercion (implicit conversion)
- == vs === (loose vs strict equality)
- Template literals (backticks, interpolation)
- String methods (toUpperCase, split, replace, etc.)
- Number methods and Math object
- Truthy/falsy values
- typeof operator

## Lesson

### Variables
```javascript
const name = "Akash";  // can't reassign
let count = 0;         // can reassign
```

### Template literals
```javascript
`Hello, ${name}! You are ${age} years old.`
```

### Strict equality
```javascript
if (value === "expected") { ... }  // always use ===
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.js` — Declare variables for a person (name, age, isStudent, hobbies array). Use `const` and `let` appropriately. Print a greeting using template literals.

   ```
   EXPECTED CONSOLE OUTPUT:
   Hello, my name is Akash. I am 25 years old. Student: true.
   Hobbies: coding, reading, gaming.
   ```
2. `easy/p02-solve.js` — Write a function that takes a string and returns it uppercased, reversed, and with its length. Example: "hello" → "OLLEH (length: 5)".

   ```
   EXPECTED CONSOLE OUTPUT:
   OLLEH (length: 5)
   ```
3. `easy/p03-solve.js` — Write a function `isTruthy(value)` that returns true if the value is truthy, false if falsy. Test with: 0, "", null, undefined, NaN, false, [], {}, "0", "false".

   ```
   EXPECTED CONSOLE OUTPUT:
   false   <- 0, "", null, undefined, NaN, false
   true    <- [], {}, "0", "false"
   ```

### Medium
4. `medium/p01-solve.js` — Write a function `formatPrice(amount, currency)` that takes a number and currency code, returns formatted string. Example: `formatPrice(1234.5, "USD")` → "$1,234.50". Use `toFixed` and template literals.

   ```
   EXPECTED CONSOLE OUTPUT:
   formatPrice(1234.5, "USD")  -> "$1,234.50"
   formatPrice(99.999, "EUR")  -> "EUR 100.00"  (or euro sign)
   ```
5. `medium/p02-solve.js` — Write a function `coerceDemo(a, b)` that demonstrates type coercion: returns an object with `addition: a + b`, `subtraction: a - b`, `equality: a == b`, `strictEquality: a === b`. Test with ("5", 5).

   ```
   EXPECTED CONSOLE OUTPUT:
   coerceDemo("5", 5) ->
   { addition: "55", subtraction: 0,
     equality: true, strictEquality: false }
   ```
6. `medium/p03-solve.js` — Write a function `parseNumber(str)` that safely converts a string to a number. Handle: "42" → 42, "3.14" → 3.14, "abc" → NaN, "" → 0, "42px" → 42. Use parseInt, parseFloat, and Number appropriately.

   ```
   EXPECTED CONSOLE OUTPUT:
   parseNumber("42")   -> 42     parseNumber("3.14") -> 3.14
   parseNumber("abc")  -> NaN    parseNumber("")     -> 0
   parseNumber("42px") -> 42
   ```

### Hard
7. `hard/p01-solve.js` — Write a function `deepTypeCheck(value)` that returns the "real" type of any value. Handle the typeof null/array bugs: null → "null", [] → "array", {} → "object", etc. Use Array.isArray and === null.

   ```
   EXPECTED CONSOLE OUTPUT:
   null -> "null"        [] -> "array"       {} -> "object"
   "hi" -> "string"    42 -> "number"      undefined -> "undefined"
   a function -> "function"
   ```
8. `hard/p02-solve.js` — Write a function `safeMath(operation, a, b)` that performs arithmetic safely. Handle: division by zero → "Cannot divide by zero", non-number inputs → "Invalid input", overflow → "Number too large". Return result or error message.

   ```
   EXPECTED CONSOLE OUTPUT:
   safeMath("divide", 10, 0) -> "Cannot divide by zero"
   safeMath("add", "5", 3)     -> "Invalid input"
   safeMath("add", 5, 3)       -> 8
   ```
9. `hard/p03-solve.js` — Write a function `analyzeString(str)` that returns an object with: original string, length, word count, character count (no spaces), reversed, isPalindrome (boolean), most frequent character, and word list. Use string methods.

   ```
   EXPECTED CONSOLE OUTPUT:
   analyzeString("race car") ->
   { original: "race car", length: 8, wordCount: 2,
     charCount: 7 (no spaces), reversed: "rac ecar",
     isPalindrome: true, mostFrequentChar: <a char>,
     words: ["race", "car"] }
   ```

### How to work
- Write your complete JavaScript solution.
- Remove the TODO comment when done.
- Test with `node <filename>` or in browser console.
