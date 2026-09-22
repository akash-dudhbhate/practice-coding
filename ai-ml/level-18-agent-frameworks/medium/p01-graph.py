"""
LEVEL 18 — Agent Frameworks
MEDIUM P01 — Graph (the runtime)
========================================

CONCEPT:
  A linear chain can't branch or loop. Real agents need both:
  "if the tool failed, retry; if it worked, respond."

  A Graph = nodes (actions) + edges (decisions):

      .add_node("plan", fn)        register an action
      .add_edge("a", "b")          after a, ALWAYS run b
      .add_conditional("a", router) after a, run router(state) -> next name
      .run(state)                  walk from the entry node to a dead end

  run() loop: execute current node on state → look up next node —
  conditional edge wins over a plain edge → no outgoing edge? STOP,
  that node was the terminal. The first node added is the entry point.

PROBLEM:
  Write a `Graph` class with:
    - `add_node(name, fn)` — register fn under name (first added = entry)
    - `add_edge(frm, to)` — unconditional transition frm → to
    - `add_conditional(frm, router_fn)` — frm → router_fn(state) result
    - `run(state, max_steps=100)` — execute from entry until a node has
      no outgoing edge; return the final state. Raise RuntimeError if
      more than max_steps nodes execute (loop protection).
    - conditional edges take priority over plain edges for the same node

TRY THIS INPUT:
  ```python
  g = Graph()
  g.add_node("start", lambda s: {**s, "n": s["n"] + 1})
  g.add_node("big",   lambda s: {**s, "label": "big"})
  g.add_node("small", lambda s: {**s, "label": "small"})
  g.add_conditional("start", lambda s: "big" if s["n"] > 5 else "small")
  print(g.run({"n": 10}))
  print(g.run({"n": 1}))
  ```

EXPECTED OUTPUT:
  ```
  {'n': 11, 'label': 'big'}
  {'n': 2, 'label': 'small'}
  ```

HINT:
  Three dicts: self.nodes, self.edges, self.conditionals. In run(),
  after executing `current`, check conditionals first, then edges,
  else stop.

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# g = Graph()
# g.add_node("a", lambda s: {**s, "log": ["a"]})
# g.add_node("b", lambda s: {**s, "log": s["log"] + ["b"]})
# g.add_edge("a", "b")
# print(g.run({}))
