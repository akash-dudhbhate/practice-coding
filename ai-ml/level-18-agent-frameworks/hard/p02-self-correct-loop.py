"""
LEVEL 18 — Agent Frameworks
HARD P02 — Self-Correct Loop (retry until good)
========================================

CONCEPT:
  Agents produce garbage sometimes. The fix pattern:

      produce ──► verify ──┬─ ok? ──► done
                     ▲     └─ bad ──┘ (loop back and fix)

  In a graph you'd wire verify's conditional edge BACK to the fixer —
  a cycle. Here we build the same thing as a single reusable node:
  keep calling fix_fn until check_fn(state) passes or we hit max_iters.

  ALWAYS bound the loop — an agent with no iteration cap is a
  infinite API bill waiting to happen.

PROBLEM:
  Write `self_correct_loop(check_fn, fix_fn, max_iters)` that returns
  a node function `node(state)` which:
    - while check_fn(state) is falsy AND iters < max_iters:
        state = fix_fn(state); iters += 1
    - returns state with two keys added:
        state["iterations"] = number of fix calls made
        state["ok"]         = final check_fn(state) result (bool)

TRY THIS INPUT:
  ```python
  needs_3   = lambda s: s.get("x", 0) >= 3
  bump      = lambda s: {**s, "x": s.get("x", 0) + 1}

  ok_node   = self_correct_loop(needs_3, bump, 10)
  print(ok_node({"x": 0}))          # reaches 3

  weak_node = self_correct_loop(needs_3, bump, 2)
  print(weak_node({"x": 0}))        # gives up at 2
  ```

EXPECTED OUTPUT:
  ```
  {'x': 3, 'iterations': 3, 'ok': True}
  {'x': 2, 'iterations': 2, 'ok': False}
  ```

HINT:
  `while not check_fn(state) and iters < max_iters:` — then record
  `iterations` and `bool(check_fn(state))` before returning.

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# n = self_correct_loop(lambda s: s.get("x", 0) >= 5,
#                       lambda s: {**s, "x": s.get("x", 0) + 1}, 10)
# print(n({}))
