"""
LESSON 03 — Hashing (Dict & Set Patterns)
MEDIUM P02 — Group Anagrams
============================================

CONCEPT:
  Grouping by a key: anagrams share the same "signature" — their
  sorted letters. Map signature -> list of words with
  `groups.setdefault(key, []).append(word)`. One pass, no pairwise
  comparisons.

PROBLEM:
  Write a function `group_anagrams(words: list) -> list` that groups
  words which are anagrams of each other. Return a list of groups
  (each group is a list of strings). Group order doesn't matter.

TRY THIS INPUT:
  ```python
  for g in group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]):
      print(sorted(g))
  ```

EXPECTED OUTPUT:
  ```
  ['ate', 'eat', 'tea']
  ['bat']
  ['nat', 'tan']
  ```
  (group order may differ — the checker sorts before comparing)

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
