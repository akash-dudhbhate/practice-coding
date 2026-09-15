// Lesson 18 — Hard P01: Analyze grades
function analyzeGrades(students) {
  return students
    .map(s => {
      const avg = s.scores.reduce((a, b) => a + b, 0) / s.scores.length;
      return { ...s, avg, grade: avg >= 90 ? "A" : avg >= 80 ? "B" : avg >= 70 ? "C" : avg >= 60 ? "D" : "F" };
    })
    .filter(s => s.avg >= 60)
    .sort((a, b) => b.avg - a.avg)
    .slice(0, 3);
}
console.log(analyzeGrades([
  { name: "Alice", scores: [90, 85, 92] },
  { name: "Bob", scores: [55, 60, 58] },
  { name: "Charlie", scores: [95, 88, 91] },
  { name: "Diana", scores: [70, 75, 72] },
]));
