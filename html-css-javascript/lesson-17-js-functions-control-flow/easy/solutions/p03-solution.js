// Lesson 17 — Easy P03: Classify number with if/else and ternary
// if/else version
function classifyNumber(n) {
  if (n > 0) return "positive";
  else if (n < 0) return "negative";
  else return "zero";
}
// ternary version
const classifyNumberTernary = (n) => (n > 0 ? "positive" : n < 0 ? "negative" : "zero");
console.log(classifyNumber(5));   // positive
console.log(classifyNumber(-3));  // negative
console.log(classifyNumber(0));   // zero
