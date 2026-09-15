# Lesson 16 — Coding Check

## Easy

### p01-solve.js — Person variables
- [ ] `name` is a const string
- [ ] `age` is a const number
- [ ] `isStudent` is a const boolean
- [ ] `hobbies` is a const array
- [ ] Greeting uses template literals with ${}
- [ ] Output: "Hello, I'm [name], I'm [age] years old."

### p02-solve.js — String transform
- [ ] "hello" → "OLLEH (length: 5)"
- [ ] String is uppercased
- [ ] String is reversed
- [ ] Length is included in output
- [ ] Uses string methods (toUpperCase, split, reverse, join)

### p03-solve.js — isTruthy
- [ ] 0 → false
- [ ] "" → false
- [ ] null → false
- [ ] undefined → false
- [ ] NaN → false
- [ ] false → false
- [ ] [] → true (empty array is truthy)
- [ ] {} → true (empty object is truthy)
- [ ] "0" → true (non-empty string)
- [ ] "false" → true (non-empty string)

## Medium

### p01-solve.js — formatPrice
- [ ] formatPrice(1234.5, "USD") → "$1,234.50"
- [ ] Uses toFixed(2) for decimals
- [ ] Uses template literals
- [ ] Handles large numbers (1000000 → "$1,000,000.00")
- [ ] Currency symbol is included

### p02-solve.js — coerceDemo
- [ ] coerceDemo("5", 5) returns an object
- [ ] addition: "55" (string concatenation)
- [ ] subtraction: 0 (string coerced to number)
- [ ] equality: true (loose equality with coercion)
- [ ] strictEquality: false (different types)
- [ ] Object has all 4 properties

### p03-solve.js — parseNumber
- [ ] "42" → 42 (number)
- [ ] "3.14" → 3.14 (float)
- [ ] "abc" → NaN
- [ ] "" → 0 or NaN (document your choice)
- [ ] "42px" → 42 (parseInt extracts leading number)
- [ ] Uses parseInt, parseFloat, and Number correctly

## Hard

### p01-solve.js — deepTypeCheck
- [ ] null → "null" (not "object")
- [ ] [] → "array" (not "object")
- [ ] {} → "object"
- [ ] "hello" → "string"
- [ ] 42 → "number"
- [ ] true → "boolean"
- [ ] undefined → "undefined"
- [ ] function(){} → "function"
- [ ] Uses Array.isArray() and === null

### p02-solve.js — safeMath
- [ ] safeMath("add", 5, 3) → 8
- [ ] safeMath("divide", 10, 0) → "Cannot divide by zero"
- [ ] safeMath("add", "abc", 3) → "Invalid input"
- [ ] safeMath("multiply", 5, 3) → 15
- [ ] safeMath("subtract", 10, 3) → 7
- [ ] Handles all 4 operations (add, subtract, multiply, divide)
- [ ] Returns error messages for invalid inputs

### p03-solve.js — analyzeString
- [ ] Returns object with all properties
- [ ] original: the input string
- [ ] length: correct character count
- [ ] wordCount: correct word count (split by spaces)
- [ ] charCount (no spaces): correct count
- [ ] reversed: string reversed
- [ ] isPalindrome: true for "racecar", false for "hello"
- [ ] mostFrequentChar: correct character
- [ ] wordList: array of words
