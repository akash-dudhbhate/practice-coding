/**
LESSON 16 — JavaScript Variables & Types
=========================================

PROBLEM: Safe Number Parsing (Medium)
Write parseNumber(str) that converts strings without surprises.

TRY THIS:
  - "" -> 0, "42" -> parseInt, "3.14" -> parseFloat,
    "42px" -> 42 (leading digits), anything else -> NaN.
  - Use regex tests + parseInt/parseFloat/Number appropriately.

EXPECTED OUTPUT:
  parseNumber("42") === 42      parseNumber("3.14") === 3.14
  parseNumber("abc") is NaN     parseNumber("") === 0
  parseNumber("42px") === 42

TEST: node medium/p03-solve.js

CHECK: python3 check.py medium/p03
*/

// TODO: Write your complete solution from scratch below.
