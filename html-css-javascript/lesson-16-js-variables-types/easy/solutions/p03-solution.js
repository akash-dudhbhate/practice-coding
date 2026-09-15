// Lesson 16 — Easy P03: Truthy/falsy check
function isTruthy(value) {
  return Boolean(value);
}
console.log(isTruthy(0));        // false
console.log(isTruthy(""));      // false
console.log(isTruthy(null));    // false
console.log(isTruthy(undefined)); // false
console.log(isTruthy(NaN));     // false
console.log(isTruthy(false));   // false
console.log(isTruthy([]));      // true
console.log(isTruthy({}));      // true
console.log(isTruthy("0"));     // true
console.log(isTruthy("false")); // true
