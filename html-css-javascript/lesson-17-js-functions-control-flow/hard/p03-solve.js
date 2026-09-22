/**
LESSON 17 — JavaScript Functions & Control Flow
================================================

PROBLEM: Counter Closure (Hard)
Write createCounter(start = 0) returning {increment, decrement,
reset, getValue} — state lives in a closure.

TRY THIS:
  - let value = start; return an object of arrow functions that
    read/mutate value.
  - increment/decrement return the new value; reset returns start;
    getValue reads it.
  - Create two counters and show they're independent.

EXPECTED OUTPUT:
  const c = createCounter(10);
  c.increment() -> 11; c.increment() -> 12; c.reset() -> 10
  A second counter starts at its own start value.

TEST: node hard/p03-solve.js

CHECK: python3 check.py hard/p03
*/

// TODO: Write your complete solution from scratch below.
