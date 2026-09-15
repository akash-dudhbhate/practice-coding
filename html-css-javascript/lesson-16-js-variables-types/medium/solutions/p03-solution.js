// Lesson 16 — Medium P03: Safe number parsing
function parseNumber(str) {
  if (str === "") return 0;
  if (/^-?\d+$/.test(str.trim())) return parseInt(str, 10);
  if (/^-?\d+\.\d+$/.test(str.trim())) return parseFloat(str);
  if (/^-?\d+(\.\d+)?/.test(str.trim())) return parseFloat(str);
  return NaN;
}
console.log(parseNumber("42"));    // 42
console.log(parseNumber("3.14"));  // 3.14
console.log(parseNumber("abc"));   // NaN
console.log(parseNumber(""));      // 0
console.log(parseNumber("42px"));  // 42
