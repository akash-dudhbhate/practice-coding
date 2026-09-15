# Lesson 17 — JS Functions & Control Flow

## What you'll learn
- Function declarations vs expressions vs arrow functions
- Default parameters and rest parameters
- Spread operator (arrays and objects)
- Destructuring (arrays and objects)
- if/else and switch statements
- Ternary operator
- Loops (for, while, for...of, for...in)
- break and continue

## Lesson

### Arrow function
```javascript
const add = (a, b) => a + b;
const greet = (name = "Guest") => `Hello, ${name}`;
```

### Destructuring
```javascript
const { name, age } = user;
const [first, ...rest] = [1, 2, 3, 4];
```

### Spread
```javascript
const newArr = [...oldArr, newItem];
const newObj = { ...oldObj, key: newValue };
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.js` — Write an arrow function `multiply(a, b = 1)` that returns a * b. Test with multiply(5, 3) and multiply(5).
2. `easy/p02-solve.js` — Write a function `formatName(first, last)` using destructuring. Accept an object `{first, last}`. Return "First LAST" (last name uppercased).
3. `easy/p03-solve.js` — Write a function `classifyNumber(n)` using if/else: positive, negative, or zero. Then rewrite it as a ternary expression.

### Medium
4. `medium/p01-solve.js` — Write a function `sumAll(...nums)` using rest parameters. Returns the sum of all arguments. Test with 3+ numbers.
5. `medium/p02-solve.js` — Write a function `mergeObjects(obj1, obj2)` using spread. Returns a merged object where obj2's properties override obj1's. Test with overlapping keys.
6. `medium/p03-solve.js` — Write a function `getDayType(day)` using switch. Returns "Weekend" for Saturday/Sunday, "Weekday" for Monday-Friday, "Invalid" for anything else. Don't forget break statements.

### Hard
7. `hard/p01-solve.js` — Write a function `calculateGrade(scores)` that takes an array of scores, drops the lowest (using spread + sort or Math.min), and returns a letter grade (A/B/C/D/F) based on the average. Use destructuring, spread, and ternary.
8. `hard/p02-solve.js` — Write a function `analyzeData(data)` that takes an array of user objects `{name, age, city}`. Use destructuring in the function params. Return: average age, users per city, oldest user. Use for...of and spread.
9. `hard/p03-solve.js` — Write a function `createCounter(start = 0)` that returns an object with methods: increment, decrement, reset, getValue. Use closures (the inner functions access `start`). Demonstrate with two independent counters.

### How to work
- Write your complete JavaScript solution.
- Remove the TODO comment when done.
- Test with `node <filename>` or in browser console.
