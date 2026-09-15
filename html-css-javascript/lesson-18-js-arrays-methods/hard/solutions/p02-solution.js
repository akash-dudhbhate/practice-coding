// Lesson 18 — Hard P02: Flatten and unique
function flattenAndUnique(nestedArr) {
  return [...new Set(nestedArr.flat(Infinity))].sort((a, b) => a - b);
}
console.log(flattenAndUnique([[1, 2], [3, [4, 2]], [1, 5]])); // [1, 2, 3, 4, 5]
