"""
LESSON 16 — REST APIs
EASY P02 — Get Repo Names
============================================

CONCEPT:
  API responses are often lists of objects — pull out just the field
  you need with a comprehension.

PROBLEM:
  Write a function `get_repos(username)` that fetches
  `https://api.github.com/users/{username}/repos` and returns a
  list of repo names (the "name" field of each repo).

TRY THIS INPUT:
  ```python
  repos = get_repos("torvalds")
  print(len(repos), repos[:2])
  ```

EXPECTED OUTPUT:
  ```
  8 ['linux', 'subsurface-for-dirk']   (approx)
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
