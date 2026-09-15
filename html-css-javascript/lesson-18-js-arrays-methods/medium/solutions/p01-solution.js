// Lesson 18 — Medium P01: Chain map, filter, sort
function processNumbers(nums) {
  return nums
    .map(n => n * 2)
    .filter(n => n > 10)
    .sort((a, b) => a - b);
}
console.log(processNumbers([3, 7, 1, 8, 5, 12]));
// map: [6,14,2,16,10,24] → filter >10: [14,16,24] → sort: [14,16,24]
