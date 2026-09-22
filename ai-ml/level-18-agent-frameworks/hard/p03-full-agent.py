"""
LEVEL 18 — Agent Frameworks
HARD P03 — Full Agent (everything together)
========================================

CONCEPT:
  Now assemble a real agent graph with a CYCLE:

      parse ──► plan ──► tools ──► verify ──► respond
                          ▲          │
                          └─ retry ──┘ (if not verified and attempts < 2)

      parse:    decide which tool the task needs
      plan:     write the step list
      tools:    run the tool, count attempts
      verify:   did the tool produce a real result?
      respond:  format the final answer

  The retry is JUST a conditional edge on "verify":
      if not verified and attempts < 2 → back to "tools" else → "respond"
  That one router function IS the agent's self-correction.

PROBLEM:
  Write `full_agent(task)` that builds and runs this Graph, and returns
  the final state dict. Include the Graph class in this file (standalone).

  Node specs (each appends its name to state["trace"]):
    - "parse":   task contains "calculate"/"compute" → kind="math",
                 state["expr"] = the math part after that word;
                 contains "search" → kind="search", state["query"] = rest;
                 anything else → kind="unknown"
    - "plan":    state["plan"] = ["parse", "use " + kind, "verify", "respond"]
    - "tools":   TOOLS = {"math": safe-eval state["expr"],
                          "search": f"Results for: {state['query']}"}
                 kind="unknown" → tool_result stays None.
                 increments state["attempts"]; sets state["tool_result"]
    - "verify":  state["verified"] = tool_result is not None
    - "respond": verified → state["response"] = f"Result: {tool_result}"
                 else      → state["response"] = f"Failed after {attempts} attempts"
    - math eval: only allow chars in "0123456789+-*/(). " then eval with
                 empty builtins; a bad expr → tool_result = None

TRY THIS INPUT:
  ```python
  r = full_agent("calculate 6 * 7")
  print(r["response"]); print(r["verified"]); print(r["trace"])
  bad = full_agent("fly to the moon")
  print(bad["response"]); print(bad["attempts"])
  ```

EXPECTED OUTPUT:
  ```
  Result: 42
  True
  ['parse', 'plan', 'tools', 'verify', 'respond']
  Failed after 2 attempts
  2
  ```

HINT:
  Reuse the Graph from medium/p01. The only new move is
  add_conditional("verify", router) where router returns "tools" or
  "respond" — a back-edge creating the retry cycle.

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch. Include the Graph class here.


# === TEST ===
# r = full_agent("calculate 2 + 2")
# print(r["response"], r["trace"])
