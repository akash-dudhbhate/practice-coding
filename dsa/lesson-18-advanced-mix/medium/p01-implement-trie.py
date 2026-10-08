"""
LESSON 18 — Advanced Mix
MEDIUM P01 — Implement Trie
============================================

CONCEPT:
  A trie node = {char: child} dict + is_end flag. insert() walks/creates
  one node per character and marks the final node is_end=True. search()
  requires path exists AND is_end (a mere prefix is not a word).
  startsWith() requires only the path. That is_end vs path-existence
  distinction IS the data structure.

PROBLEM:
  Implement a class `Trie` with three methods:
    insert(word: str) -> None        add word
    search(word: str) -> bool        True iff word was inserted
    startsWith(prefix: str) -> bool  True iff some inserted word starts with prefix

TRY THIS INPUT:
  ```python
  trie = Trie()
  trie.insert("apple")
  print(trie.search("apple"))
  print(trie.search("app"))
  print(trie.startsWith("app"))
  trie.insert("app")
  print(trie.search("app"))
  print(trie.startsWith("apples"))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  True
  True
  False
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
