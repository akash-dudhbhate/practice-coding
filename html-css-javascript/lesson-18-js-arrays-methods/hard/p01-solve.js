/**
LESSON 18 — JavaScript Arrays & Methods
========================================

PROBLEM: Analyze Grades (Hard)
Write analyzeGrades(students) — one pipeline, top 3 only.

TRY THIS:
  - .map each student to { ...s, avg, grade } where avg comes from
    scores.reduce and grade from a ternary chain (A/B/C/D/F).
  - .filter to keep avg >= 60, .sort by avg descending,
    .slice(0, 3) for the top 3.

EXPECTED OUTPUT (4 students, one failing):
  Returns the 3 passing students sorted best-first, each with avg
  and grade added.

TEST: node hard/p01-solve.js

CHECK: python3 check.py hard/p01
*/

// TODO: Write your complete solution from scratch below.
