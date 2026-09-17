/**
LESSON 16 — JavaScript Variables & Types
EASY P02 — Transform a String
============================================

CONCEPT:
  Strings have built-in methods: .toUpperCase() changes case,
  .split("") turns a string into an array of characters, and
  template literals (`${}`) embed values inside a string.

PROBLEM:
  Write a function `transform(str)` that returns the string
  uppercased, reversed, with its ORIGINAL length appended:
  "REVERSED (length: N)".

TRY THIS INPUT:
  ```js
  console.log(transform("hello"));
  ```

EXPECTED OUTPUT:
  ```
  OLLEH (length: 5)
  ```

HINT:
  upper = str.toUpperCase();
  reversed = upper.split("").reverse().join("");
  then build the final string with a template literal.

CHECK: python3 check.py easy/p02
*/
// TODO: Write your complete solution from scratch below.
