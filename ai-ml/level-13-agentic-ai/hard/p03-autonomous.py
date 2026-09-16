"""
LEVEL 13 — Agentic AI
HARD P03 — Autonomous Goal Decomposition
========================================

CONCEPT:
  The most advanced agent pattern: give it a high-level goal,
  it decomposes into sub-goals and assigns them to tools.

    "Research a topic and write a summary"
    → Goal: Research a topic and write a summary
      Action 1: search for information
      Action 2: analyze results
      Action 3: summarize findings

PROBLEM:
  Write `autonomous_agent(goal)` that:
    1. Decomposes the goal into ordered actions
    2. Returns a list of action strings

  Rules:
    - "research" in goal → ["search for information", "analyze results", "summarize findings"]
    - "build" in goal → ["plan structure", "write code", "test it"]
    - "analyze" in goal → ["collect data", "run analysis", "report results"]

TRY THIS INPUT:
  ```python
  actions = autonomous_agent("research a topic and write a summary")
  for i, a in enumerate(actions):
      print(f"Action {i+1}: {a}")
  ```

EXPECTED OUTPUT:
  ```
  Action 1: search for information
  Action 2: analyze results
  Action 3: summarize findings
  ```

HINT:
  Match keywords in the goal to the right action sequence.

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# for a in autonomous_agent("research a topic"):
#     print(a)
