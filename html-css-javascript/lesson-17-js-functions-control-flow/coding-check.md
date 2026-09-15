# Lesson 17 — Coding Check

## Easy

### p01-solve.js — multiply with default
- [ ] `multiply(5, 3)` returns 15
- [ ] `multiply(5)` returns 5 (default b=1)
- [ ] `multiply(5, 0)` returns 0
- [ ] Uses arrow function syntax
- [ ] Uses default parameter

### p02-solve.js — formatName with destructuring
- [ ] Accepts an object `{first, last}`
- [ ] Uses destructuring in parameters
- [ ] Returns "First LAST" format
- [ ] Last name is uppercased
- [ ] formatName({first: "Akash", last: "Dev"}) → "Akash DEV"

### p03-solve.js — classifyNumber
- [ ] classifyNumber(5) → "positive"
- [ ] classifyNumber(-3) → "negative"
- [ ] classifyNumber(0) → "zero"
- [ ] if/else version works correctly
- [ ] Ternary version works correctly
- [ ] Both versions return the same results

## Medium

### p01-solve.js — sumAll with rest params
- [ ] `sumAll(1, 2, 3)` returns 6
- [ ] `sumAll(1, 2, 3, 4, 5)` returns 15
- [ ] `sumAll()` returns 0
- [ ] Uses `...nums` rest parameter
- [ ] Works with any number of arguments

### p02-solve.js — mergeObjects with spread
- [ ] Merges two objects
- [ ] obj2 properties override obj1 for same keys
- [ ] Original objects are not modified
- [ ] mergeObjects({a:1, b:2}, {b:3, c:4}) → {a:1, b:3, c:4}
- [ ] Uses spread operator

### p03-solve.js — getDayType with switch
- [ ] "Saturday" → "Weekend"
- [ ] "Sunday" → "Weekend"
- [ ] "Monday" → "Weekday"
- [ ] "Friday" → "Weekday"
- [ ] "InvalidDay" → "Invalid"
- [ ] Uses switch with break statements
- [ ] Has default case

## Hard

### p01-solve.js — calculateGrade
- [ ] Drops the lowest score
- [ ] Calculates average of remaining scores
- [ ] Average >= 90 → "A"
- [ ] Average >= 80 → "B"
- [ ] Average >= 70 → "C"
- [ ] Average >= 60 → "D"
- [ ] Average < 60 → "F"
- [ ] Uses destructuring, spread, and ternary

### p02-solve.js — analyzeData
- [ ] Takes array of {name, age, city} objects
- [ ] Uses destructuring in function parameters
- [ ] Returns average age (number)
- [ ] Returns users per city (object: {city: count})
- [ ] Returns oldest user (object or name)
- [ ] Uses for...of loop
- [ ] Uses spread where appropriate

### p03-solve.js — createCounter closure
- [ ] `createCounter(10)` returns object with methods
- [ ] `counter.increment()` increases value by 1
- [ ] `counter.decrement()` decreases value by 1
- [ ] `counter.reset()` returns to start value
- [ ] `counter.getValue()` returns current value
- [ ] Two counters are independent (don't share state)
- [ ] Uses closures (inner functions access outer variable)
