"""
LESSON 13 — Graphs: BFS & DFS
EASY P02 — BFS Traversal Order
============================================

CONCEPT:
  BFS explores in RINGS around the source: level 0 = start, level 1 =
  everything 1 hop away, level 2 = 2 hops... A deque gives FIFO order:
  popleft() serves the oldest (= closest) vertex first. Mark each
  vertex `seen` when you ENQUEUE it — marking at pop time lets the
  same vertex enter the queue many times.

PROBLEM:
  Write `bfs_order(adj, start) -> list` returning the order in which a
  queue-based BFS first visits each vertex. `adj` is a dict of lists;
  explore neighbors in their stored order. A disconnected graph returns
  only the start's component. Single vertex returns [start].

TRY THIS INPUT:
  ```python
  adj = {0:[1,2], 1:[0,3], 2:[0,4,5], 3:[1], 4:[2], 5:[2]}
  print(bfs_order(adj, 0))
  print(bfs_order({0:[]}, 0))
  print(bfs_order({0:[1], 1:[0], 2:[]}, 0))   # 2 is disconnected
  ```

EXPECTED OUTPUT:
  ```
  [0, 1, 2, 3, 4, 5]
  [0]
  [0, 1]
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
