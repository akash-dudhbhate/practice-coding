// Lesson 16 — Easy P02: Uppercase, reverse, length
function transform(str) {
  const upper = str.toUpperCase();
  const reversed = upper.split("").reverse().join("");
  return `${reversed} (length: ${str.length})`;
}
console.log(transform("hello")); // OLLEH (length: 5)
