/**
LESSON 16 — JavaScript Variables & Types
=========================================

PROBLEM: Deep Type Check (Hard)
Write deepTypeCheck(value) returning the REAL type string.

TRY THIS:
  - Handle the famous bugs: null -> "null" (typeof says "object"),
    [] -> "array" (typeof says "object").
  - Use === null and Array.isArray before falling back to typeof.

EXPECTED OUTPUT:
  null -> "null"     [] -> "array"      {} -> "object"
  "hi" -> "string"   42 -> "number"     undefined -> "undefined"
  a function -> "function"

TEST: node hard/p01-solve.js

CHECK: python3 check.py hard/p01
*/

// TODO: Write your complete solution from scratch below.
