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

   ```
   EXPECTED CONSOLE OUTPUT:
   multiply(5, 3) -> 15
   multiply(5)    -> 5      <- default parameter b = 1
   ```
2. `easy/p02-solve.js` — Write a function `formatName(first, last)` using destructuring. Accept an object `{first, last}`. Return "First LAST" (last name uppercased).

   ```
   EXPECTED CONSOLE OUTPUT:
   formatName({ first: "Akash", last: "dev" }) -> "Akash DEV"
   ```
3. `easy/p03-solve.js` — Write a function `classifyNumber(n)` using if/else: positive, negative, or zero. Then rewrite it as a ternary expression.

   ```
   EXPECTED CONSOLE OUTPUT:
   classifyNumber(5)  -> "positive"
   classifyNumber(-3) -> "negative"
   classifyNumber(0)  -> "zero"
   ```

### Medium
4. `medium/p01-solve.js` — Write a function `sumAll(...nums)` using rest parameters. Returns the sum of all arguments. Test with 3+ numbers.

   ```
   EXPECTED CONSOLE OUTPUT:
   sumAll(1, 2, 3, 4, 5) -> 15
   sumAll()              -> 0
   ```
5. `medium/p02-solve.js` — Write a function `mergeObjects(obj1, obj2)` using spread. Returns a merged object where obj2's properties override obj1's. Test with overlapping keys.

   ```
   EXPECTED CONSOLE OUTPUT:
   mergeObjects({ a: 1, b: 2 }, { b: 3, c: 4 })
     -> { a: 1, b: 3, c: 4 }      <- obj2's "b" wins
   ```
6. `medium/p03-solve.js` — Write a function `getDayType(day)` using switch. Returns "Weekend" for Saturday/Sunday, "Weekday" for Monday-Friday, "Invalid" for anything else. Don't forget break statements.

   ```
   EXPECTED CONSOLE OUTPUT:
   getDayType("Saturday") -> "Weekend"
   getDayType("Monday")   -> "Weekday"
   getDayType("Funday")   -> "Invalid"
   ```

### Hard
7. `hard/p01-solve.js` — Write a function `calculateGrade(scores)` that takes an array of scores, drops the lowest (using spread + sort or Math.min), and returns a letter grade (A/B/C/D/F) based on the average. Use destructuring, spread, and ternary.

   ```
   EXPECTED CONSOLE OUTPUT:
   calculateGrade([85, 90, 78, 92]) -> "B"
   (lowest score 78 dropped; average of the rest = 89)
   ```
8. `hard/p02-solve.js` — Write a function `analyzeData(data)` that takes an array of user objects `{name, age, city}`. Use destructuring in the function params. Return: average age, users per city, oldest user. Use for...of and spread.

   ```
   EXPECTED CONSOLE OUTPUT:
   { averageAge: 30,
     usersPerCity: { Mumbai: 2, Delhi: 1 },
     oldestUser: { name: "Charlie", age: 35, city: "Mumbai" } }
   ```
9. `hard/p03-solve.js` — Write a function `createCounter(start = 0)` that returns an object with methods: increment, decrement, reset, getValue. Use closures (the inner functions access `start`). Demonstrate with two independent counters.

   ```
   EXPECTED CONSOLE OUTPUT:
   const c = createCounter(10)
   c.increment() -> 11   c.increment() -> 12
   c.decrement() -> 11   c.reset() -> 10   <- back to start value
   (a second counter counts from its own start, independently)
   ```

### How to work
- Write your complete JavaScript solution.
- Remove the TODO comment when done.
- Test with `node <filename>` or in browser console.
