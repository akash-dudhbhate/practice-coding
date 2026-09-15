// Lesson 16 — Medium P02: Type coercion demo
function coerceDemo(a, b) {
  return {
    addition: a + b,
    subtraction: a - b,
    equality: a == b,
    strictEquality: a === b,
  };
}
console.log(coerceDemo("5", 5));
// { addition: "55", subtraction: 0, equality: true, strictEquality: false }
