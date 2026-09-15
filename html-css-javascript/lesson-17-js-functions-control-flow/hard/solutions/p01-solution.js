// Lesson 17 — Hard P01: Calculate grade with destructuring and spread
function calculateGrade(scores) {
  const [...sorted] = scores.sort((a, b) => a - b);
  sorted.shift(); // drop lowest
  const avg = sorted.reduce((s, n) => s + n, 0) / sorted.length;
  return avg >= 90 ? "A" : avg >= 80 ? "B" : avg >= 70 ? "C" : avg >= 60 ? "D" : "F";
}
console.log(calculateGrade([85, 90, 78, 92])); // drops 78, avg = 89 → B
