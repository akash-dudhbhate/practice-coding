"""
LESSON 18 — Advanced Mix
HARD P01 — Word Search II (Trie-accelerated)
============================================

CONCEPT:
  Grid DFS + a trie of the dictionary. From every cell, DFS in 4
  directions spelling a path; the trie tells you in O(1) whether the
  path is still a PREFIX of any word — if not, the branch dies. Checking
  each word separately re-walks shared prefixes thousands of times.
  Mark cells visited during recursion and RESTORE them after (other
  paths need them). Store the word itself at trie leaves; delete on
  find so duplicates aren't reported.

PROBLEM:
  Write a function
  `find_words(board: list[list[str]], words: list[str]) -> list[str]`
  returning the SORTED list of words that can be spelled on the board:
  consecutive letters on horizontally/vertically adjacent cells, no cell
  used twice within one word. Cells are single lowercase letters.

TRY THIS INPUT:
  ```python
  board = [["o","a","a","n"],
           ["e","t","a","e"],
           ["i","h","k","r"],
           ["i","f","l","v"]]
  print(find_words(board, ["oath","pea","eat","rain"]))
  print(find_words([["a","b"],["c","d"]], ["abcb"]))
  print(find_words([["a"]], ["a"]))
  ```

EXPECTED OUTPUT:
  ```
  ['eat', 'oath']
  []
  ['a']
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
