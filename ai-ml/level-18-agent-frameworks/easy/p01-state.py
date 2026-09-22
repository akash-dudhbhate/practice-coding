"""
LEVEL 18 — Agent Frameworks
EASY P01 — State (the shared scratchpad)
========================================

CONCEPT:
  In a graph agent, ONE state object flows through every node.
  Each node reads what it needs and writes its results back.
  Frameworks like LangGraph call this the "graph state" — it's
  how the plan node talks to the tool node without ever meeting.

  We add a `.history` list that records every write. That's the
  seed of "checkpointing" — replaying/auditing what the agent did.

PROBLEM:
  Write a `State` class with:
    - `State(initial=None)` — wrap a dict (default: empty dict)
    - `.get(key, default=None)` — read a key
    - `.set(key, value)` — write a key AND append (key, value) to .history
    - `.history` — a list of (key, value) tuples, in write order

TRY THIS INPUT:
  ```python
  s = State({"task": "build a graph"})
  s.set("plan", ["step1", "step2"])
  s.set("step", 1)
  print(s.get("task"))
  print(s.get("missing", "nope"))
  print(s.history)
  ```

EXPECTED OUTPUT:
  ```
  build a graph
  nope
  [('plan', ['step1', 'step2']), ('step', 1)]
  ```

HINT:
  Keep the data in self.data (a plain dict). .history is a list
  that .set() appends to — the initial dict does NOT count as writes.

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# s = State({"task": "x"})
# s.set("a", 1)
# print(s.get("a"), s.history)
