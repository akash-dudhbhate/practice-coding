"""
LESSON 14 — Graph Algorithms
HARD P02 — Network Delay Time
============================================

CONCEPT:
  A signal leaves node k and travels edges at their weight-speed.
  "How long until every node hears it?" = the MAXIMUM of the shortest
  times from k to each node — a Dijkstra problem: run Dijkstra from k,
  take max(dist). Any unreachable node means the signal never arrives
  everywhere -> -1. Watch the indexing: nodes are 1..n, not 0..n-1.

PROBLEM:
  Write `network_delay_time(times, n, k) -> int`. times holds directed
  pairs (u, v, w): signal takes w to travel u -> v. Return the max
  shortest-path time, or -1 if some node never receives the signal.
  1 <= u, v <= n (one-indexed!).

TRY THIS INPUT:
  ```python
  print(network_delay_time([(2,1,1),(2,3,1),(3,4,1)], 4, 2))
  print(network_delay_time([(1,2,1)], 2, 1))
  print(network_delay_time([(1,2,1)], 2, 2))
  print(network_delay_time([(1,2,1),(2,3,2),(1,3,4)], 3, 1))
  ```

EXPECTED OUTPUT:
  ```
  2
  1
  -1
  3
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
