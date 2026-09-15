// Lesson 17 — Hard P03: Counter with closures
function createCounter(start = 0) {
  let value = start;
  return {
    increment: () => ++value,
    decrement: () => --value,
    reset: () => { value = start; return value; },
    getValue: () => value,
  };
}
const c1 = createCounter(10);
const c2 = createCounter(0);
console.log(c1.increment()); // 11
console.log(c1.increment()); // 12
console.log(c2.increment()); // 1
console.log(c1.getValue());  // 12
console.log(c1.reset());     // 10
