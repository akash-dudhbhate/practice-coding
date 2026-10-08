"""
LESSON 13 — Graphs: BFS & DFS
HARD P01 — Word Ladder (BFS on an Implicit Graph)
============================================

CONCEPT:
  Words are vertices; two words are neighbors when they differ by
  exactly one letter. Nobody hands you an edge list — the graph is
  IMPLICIT, discovered as you go. The trick: a word's neighbors all
  share a wildcard pattern. "hot" matches *ot, h*t, ho* — bucket every
  word by its L patterns, and each lookup lists ALL neighbors in one
  shot instead of O(N) pairwise diffs per vertex. Then plain BFS:
  fewest transformations = fewest hops = word count in the ladder.

PROBLEM:
  Write `ladder_length(begin, end, word_list) -> int` — the number of
  words in the shortest ladder begin→end (counting both), or 0 if
  impossible / end not in word_list. All words same length. A word
  can't repeat in a ladder (use seen).

TRY THIS INPUT:
  ```python
  print(ladder_length("hit", "cog",
                      ["hot","dot","dog","lot","log","cog"]))
  print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]))
  print(ladder_length("hit", "lot", ["hit","hot","lot"]))
  print(ladder_length("hot", "dog", ["hot","dog"]))   # diff = 2
  ```

EXPECTED OUTPUT:
  ```
  5
  0
  3
  0
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
