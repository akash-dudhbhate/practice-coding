# Lesson 17 — Common Mistakes

## Mistake 01: Arrow functions for methods
```javascript
// WRONG — this is wrong
const obj = {
  greet: () => this.name  // this is not obj
};
// CORRECT
const obj = {
  greet() { return this.name; }
};
```

## Mistake 02: Missing break in switch
```javascript
// WRONG — falls through
switch (x) {
  case 1: doSomething();
  case 2: doOther();
}
// CORRECT
switch (x) {
  case 1: doSomething(); break;
  case 2: doOther(); break;
}
```

## Mistake 03: var in loops
```javascript
// WRONG — closure captures same i
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// CORRECT
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
```

## Mistake 04: Deeply nested if/else
```javascript
// WRONG — callback hell / nesting
// CORRECT — early returns
function process(x) {
  if (!x) return;
  if (x < 0) return;
  // main logic
}
```

## Mistake 05: Not using default parameters
```javascript
// VERBOSE
function greet(name) {
  name = name || "Guest";
  return `Hello, ${name}`;
}
// BETTER
function greet(name = "Guest") {
  return `Hello, ${name}`;
}
```
