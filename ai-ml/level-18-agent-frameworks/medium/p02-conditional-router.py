"""
LEVEL 18 — Agent Frameworks
MEDIUM P02 — Conditional Router (the decision function)
========================================

CONCEPT:
  A router is a plain function `state -> "node_name"`. It doesn't touch
  the state — it just LOOKS at it and picks which node runs next.

  This one tiny mechanism powers almost everything "agentic":
    - tool selection:   state["kind"] == "math"  -> "calc_node"
    - error handling:   "error" in state         -> "handle_error"
    - loops:            not state["verified"]    -> "tools"  (back edge!)
    - human gates:      state["needs_approval"]  -> "ask_human"

PROBLEM:
  Write `conditional_router(state)` that returns:
    - "handle_error"  if state has a truthy "error" key
    - "finish"        else if state has a truthy "done" key
    - "continue"      otherwise

TRY THIS INPUT:
  ```python
  print(conditional_router({"error": "tool crashed"}))
  print(conditional_router({"done": True}))
  print(conditional_router({"done": False, "step": 2}))
  print(conditional_router({}))
  ```

EXPECTED OUTPUT:
  ```
  handle_error
  finish
  continue
  continue
  ```

HINT:
  Check "error" FIRST — an error should override a done flag.

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(conditional_router({"error": "x", "done": True}))
