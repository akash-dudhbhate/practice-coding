"""
LESSON 16 — REST APIs
EASY P01 — Get GitHub User
============================================

CONCEPT:
  `requests.get(url)` fetches a URL; `.raise_for_status()` turns
  HTTP errors into exceptions; `.json()` parses the response body.

PROBLEM:
  Write a function `get_user(username)` that fetches
  `https://api.github.com/users/{username}` and returns the parsed
  JSON dict.

TRY THIS INPUT:
  ```python
  user = get_user("torvalds")
  print(user["name"])
  ```

EXPECTED OUTPUT:
  ```
  Linus Torvalds
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
