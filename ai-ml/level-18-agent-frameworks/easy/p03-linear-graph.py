"""
LEVEL 18 — Agent Frameworks
EASY P03 — Linear Graph (the simplest graph)
========================================

CONCEPT:
  The simplest possible graph is a chain: run node1, feed its output
  to node2, feed that to node3... No branches, no loops.

      state ──► node1 ──► node2 ──► node3 ──► final_state

  Key insight: `linear_graph(nodes)` RETURNS A FUNCTION. A graph made
  of nodes is itself just a `state → state` function — which means a
  whole graph can be a node inside a bigger graph. That's how real
  frameworks compose sub-agents.

PROBLEM:
  Write `linear_graph(nodes)` that:
    - takes a list of callables (each: dict → dict)
    - returns a function `pipeline(state)` that runs them in order,
      feeding each node's output into the next
    - returns the final state dict

TRY THIS INPUT:
  ```python
  add_one  = lambda s: {**s, "x": s["x"] + 1}
  times_3  = lambda s: {**s, "x": s["x"] * 3}
  minus_2  = lambda s: {**s, "x": s["x"] - 2}

  pipe = linear_graph([add_one, times_3, minus_2])
  print(pipe({"x": 1}))     # ((1+1)*3)-2 = 4
  ```

EXPECTED OUTPUT:
  ```
  {'x': 4}
  ```

HINT:
  Define `pipeline(state)` inside `linear_graph`, loop over `nodes`
  reassigning `state = node(state)`, then `return pipeline`.

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# pipe = linear_graph([lambda s: {"x": 5}, lambda s: {"x": s["x"] * 2}])
# print(pipe({}))
