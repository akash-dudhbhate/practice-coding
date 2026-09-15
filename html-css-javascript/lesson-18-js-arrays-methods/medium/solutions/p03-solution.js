// Lesson 18 — Medium P03: Remove duplicates
function removeDuplicates(arr) {
  return [...new Set(arr)];
}
// Alternative with filter + indexOf:
function removeDuplicatesAlt(arr) {
  return arr.filter((item, index) => arr.indexOf(item) === index);
}
console.log(removeDuplicates([1, 2, 2, 3, 4, 4, 5])); // [1, 2, 3, 4, 5]
