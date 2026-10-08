"""
LESSON 17 — Greedy & Intervals
HARD P02 — Gas Station
============================================

CONCEPT:
  Two facts make it one pass: (1) if total gas < total cost, NO start
  works — return -1. (2) If your tank goes negative at station i, no
  station inside the failed stretch can be the answer either — you'd
  arrive there with <= 0 tank and face the same deficit. Restart the
  candidate at i+1. This greedy skip is what turns O(n^2) simulation
  into O(n).

PROBLEM:
  Write a function
  `can_complete_circuit(gas: list[int], cost: list[int]) -> int`.
  gas[i] is fuel gained at station i; cost[i] is fuel spent driving to
  station i+1 (wrapping around). Return the starting station index that
  completes one full loop with an empty starting tank, or -1 if none.
  If an answer exists it is unique.

TRY THIS INPUT:
  ```python
  print(can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]))
  print(can_complete_circuit([2,3,4], [3,4,3]))
  print(can_complete_circuit([5,1,2,3,4], [4,4,1,5,1]))
  print(can_complete_circuit([3,1,1], [1,2,2]))
  ```

EXPECTED OUTPUT:
  ```
  3
  -1
  4
  0
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
