"""
LESSON 08 — Recursion & Backtracking
MEDIUM P03 — Letter Case Permutation
============================================

CONCEPT:
  Include/skip generalizes to "branch once per OPTION": for each
  character, letters fork into lower/upper branches while digits have
  only one option — recurse straight through. 2^(#letters) results.
  char.isalpha() / char.lower() / char.upper() do the work.

PROBLEM:
  Write `letter_case_permutation(s: str) -> list` returning every
  version of s where each LETTER may be lower or upper (digits fixed).
  letter_case_permutation("a1b2") -> {"a1b2","a1B2","A1b2","A1B2"} in
  any order. letter_case_permutation("123") -> ["123"].

TRY THIS INPUT:
  ```python
  print(sorted(letter_case_permutation("a1b2")))
  print(sorted(letter_case_permutation("3z4")))
  print(letter_case_permutation("123"))
  ```

EXPECTED OUTPUT:
  ```
  ['A1B2', 'A1b2', 'a1B2', 'a1b2']
  ['3Z4', '3z4']
  ['123']
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
