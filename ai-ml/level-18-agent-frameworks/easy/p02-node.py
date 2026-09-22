"""
LEVEL 18 — Agent Frameworks
EASY P02 — Node (a named action)
========================================

CONCEPT:
  A node is the unit of work in a graph agent. It's just a function
  that takes the current state dict and returns a new state dict:

      state_in  ──►  ┌ NODE ┐  ──►  state_out

  Why wrap it in a class? The NAME. When the graph runs, it can
  record "plan ran, then execute ran" — observability for free.
  In LangGraph every node has a name; same idea here.

PROBLEM:
  Write a `Node` class with:
    - `Node(name, fn)` — store the name and the function
    - `.run(state)` — call fn(state), return the result
    - calling `node(state)` directly must also work (make instances callable)

  Node functions receive a dict and return a dict:
      def shout(state):           # state in
          return {**state, "text": state["text"].upper()}   # state out

TRY THIS INPUT:
  ```python
  n = Node("shout", lambda s: {**s, "text": s["text"].upper()})
  print(n.name)
  print(n.run({"text": "hi"}))
  print(n({"text": "go"}))        # callable, same as .run()
  ```

EXPECTED OUTPUT:
  ```
  shout
  {'text': 'HI'}
  {'text': 'GO'}
  ```

HINT:
  `__call__(self, state)` makes an instance callable like a function.

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# n = Node("inc", lambda s: {**s, "x": s["x"] + 1})
# print(n({"x": 1}))
