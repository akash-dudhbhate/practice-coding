"""
LESSON 03 — Hashing (Dict & Set Patterns)
HARD P03 — LRU Cache (dict + ordering)
============================================

CONCEPT:
  A dict alone can't tell you what's oldest; a list alone can't look
  up in O(1). Combine them: a dict maps key -> node, and a
  doubly-linked list keeps usage order (most recent at the head).
  get/put move the node to the head; eviction removes the tail.
  All operations O(1).

PROBLEM:
  Implement class `LRUCache`:
    - `LRUCache(capacity)` — fixed-size cache
    - `get(key)` — return the value, or -1 if absent. Counts as a use.
    - `put(key, value)` — insert or update; evicts the least recently
      used item if over capacity.
  Aim for O(1) per operation.

TRY THIS INPUT:
  ```python
  c = LRUCache(2)
  c.put(1, 1); c.put(2, 2)
  print(c.get(1))   # 1  -> order becomes: 1 (recent), 2
  c.put(3, 3)       # evicts 2
  print(c.get(2))   # -1
  c.put(4, 4)       # evicts 1
  print(c.get(1))   # -1
  print(c.get(3))   # 3
  print(c.get(4))   # 4
  ```

EXPECTED OUTPUT:
  ```
  1
  -1
  -1
  3
  4
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
