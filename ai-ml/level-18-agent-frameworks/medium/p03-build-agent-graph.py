"""
LEVEL 18 — Agent Frameworks
MEDIUM P03 — Build Agent Graph (assemble the machine)
========================================

CONCEPT:
  The canonical agent shape — four nodes in a line:

      input ──► plan ──► execute ──► output

      input:    read the task into the state
      plan:     decide the steps
      execute:  do the work
      output:   format the answer

  Each node also appends its own name to state["trace"] — the trace
  list is your free execution log (frameworks call this "observability").

PROBLEM:
  Write `build_agent_graph()` that returns a Graph wired as above.
  Since each file is standalone, include the Graph class from
  medium/p01 in this file too.

  Node behavior (each takes state dict, returns state dict):
    - "input":   state["input"] = state["task"];  trace += "input"
    - "plan":    state["plan"] = ["step1", "step2"]; trace += "plan"
    - "execute": state["result"] = f"executed: {state['input']}"; trace += "execute"
    - "output":  state["output"] = state["result"]; trace += "output"

  Edges: input→plan, plan→execute, execute→output.

TRY THIS INPUT:
  ```python
  g = build_agent_graph()
  result = g.run({"task": "summarize notes"})
  print(result["trace"])
  print(result["output"])
  ```

EXPECTED OUTPUT:
  ```
  ['input', 'plan', 'execute', 'output']
  executed: summarize notes
  ```

HINT:
  Every node does `state = dict(state)` (or use {**s, ...}), appends to
  s.get("trace", []), then does its job. Wire with three add_edge calls.

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch. Include the Graph class here.


# === TEST ===
# g = build_agent_graph()
# print(g.run({"task": "x"})["trace"])
