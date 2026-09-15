// Lesson 16 — Hard P01: Deep type check
function deepTypeCheck(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
console.log(deepTypeCheck(null));      // "null"
console.log(deepTypeCheck([]));        // "array"
console.log(deepTypeCheck({}));        // "object"
console.log(deepTypeCheck("hi"));      // "string"
console.log(deepTypeCheck(42));        // "number"
console.log(deepTypeCheck(undefined)); // "undefined"
console.log(deepTypeCheck(() => {}));  // "function"
