// Lesson 16 — Hard P02: Safe math
function safeMath(operation, a, b) {
  if (typeof a !== "number" || typeof b !== "number") return "Invalid input";
  if (operation === "divide" && b === 0) return "Cannot divide by zero";
  let result;
  switch (operation) {
    case "add": result = a + b; break;
    case "subtract": result = a - b; break;
    case "multiply": result = a * b; break;
    case "divide": result = a / b; break;
    default: return "Unknown operation";
  }
  if (!isFinite(result) || Math.abs(result) > Number.MAX_SAFE_INTEGER) return "Number too large";
  return result;
}
console.log(safeMath("divide", 10, 0));  // "Cannot divide by zero"
console.log(safeMath("add", "5", 3));    // "Invalid input"
console.log(safeMath("add", 5, 3));      // 8
