"""
LEVEL 13 — Agentic AI
EASY P01 — Simple Agent Function
========================================

CONCEPT:
  An agent = a function that takes a goal and returns an action.
  Simplest form: a Python function that decides what to do
  based on the input.

  Think of it as: "Given this goal, what tool should I call?"

PROBLEM:
  Write `agent_decide(goal)` that:
    - "calculate" in goal → returns "use calculator"
    - "search" in goal → returns "use search"
    - "write" in goal → returns "use writer"
    - anything else → returns "unknown goal"

TRY THIS INPUT:
  ```python
  print(agent_decide("calculate 6 * 7"))
  print(agent_decide("search for AI news"))
  print(agent_decide("write a report"))
  print(agent_decide("cook dinner"))
  ```

EXPECTED OUTPUT:
  ```
  use calculator
  use search
  use writer
  unknown goal
  ```

HINT:
  Simple if/elif on goal.lower()

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(agent_decide("calculate 6*7"))
