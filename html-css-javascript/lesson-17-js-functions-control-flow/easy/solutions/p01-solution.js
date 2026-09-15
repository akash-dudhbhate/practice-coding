// Lesson 17 — Easy P01: Arrow function with default param
const multiply = (a, b = 1) => a * b;
console.log(multiply(5, 3)); // 15
console.log(multiply(5));    // 5
