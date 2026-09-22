/**
LESSON 16 — JavaScript Variables & Types
=========================================

PROBLEM: Safe Math (Hard)
Write safeMath(operation, a, b) — arithmetic that can't crash.

TRY THIS:
  - Non-number inputs -> "Invalid input".
  - "divide" by 0 -> "Cannot divide by zero".
  - add/subtract/multiply/divide via switch; unknown op ->
    "Unknown operation".
  - Result not finite / beyond MAX_SAFE_INTEGER -> "Number too large".

EXPECTED OUTPUT:
  safeMath("divide", 10, 0)  === "Cannot divide by zero"
  safeMath("add", "5", 3)    === "Invalid input"
  safeMath("add", 5, 3)      === 8

TEST: node hard/p02-solve.js

CHECK: python3 check.py hard/p02
*/

// TODO: Write your complete solution from scratch below.
