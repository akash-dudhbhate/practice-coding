"""
LEVEL 18 — Agent Frameworks
HARD P01 — Parallel Nodes (fan-out / fan-in)
========================================

CONCEPT:
  One node calls three search APIs at once? That's fan-out:
  several nodes all read the SAME input state, each returns its own
  updates, and their results get merged into one state (fan-in).

      ┌──► node_a ──┐
  in ─┼──► node_b ──┼──► merged_state
      └──► node_c ──┘

  Two rules keep it sane:
    1. Each branch gets a COPY of the input — branch A must not see
       branch B's writes (they run "at the same time", conceptually).
    2. Merge order = dict order — later branches overwrite on conflict.

  LangGraph calls this Send/join; it's how agents run parallel tools.

PROBLEM:
  Write `parallel_nodes(nodes_dict)` where nodes_dict = {name: fn}.
  It returns a node function `parallel(state)` that:
    - runs each fn on a COPY of the incoming state
    - merges every branch's returned dict into one output state
      (input keys survive unless a branch overwrites them)
    - stores each branch's output under out["results"][name]
    - appends "parallel" to out["trace"]

TRY THIS INPUT:
  ```python
  p = parallel_nodes({
      "a": lambda s: {"x": s["n"] + 1},
      "b": lambda s: {"y": s["n"] * 10},
  })
  out = p({"n": 5})
  print(out["x"], out["y"])
  print(out["results"])
  ```

EXPECTED OUTPUT:
  ```
  6 50
  {'a': {'x': 6}, 'b': {'y': 50}}
  ```

HINT:
  `fn(dict(state))` hands each branch a copy. Loop `nodes_dict.items()`,
  `merged.update(branch_out)` for fan-in, and collect per-name results.

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# p = parallel_nodes({"a": lambda s: {"x": 1}, "b": lambda s: {"y": 2}})
# print(p({"z": 0}))
