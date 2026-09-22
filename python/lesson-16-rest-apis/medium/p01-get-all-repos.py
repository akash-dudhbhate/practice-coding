"""
LESSON 16 — REST APIs
MEDIUM P01 — Get ALL Repos (pagination)
============================================

CONCEPT:
  APIs paginate: you get up to N items per page and must keep asking
  for the next page until a short/empty page arrives.

PROBLEM:
  Write a function `get_all_repos(username)` that fetches ALL repos
  for a GitHub user using `per_page=100` and `page` params, looping
  until a page returns fewer than 100 items. Return a list of repo
  names.

TRY THIS INPUT:
  ```python
  print(len(get_all_repos("torvalds")))
  ```

EXPECTED OUTPUT:
  ```
  <all repos count>
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
