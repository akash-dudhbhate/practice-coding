"""
LEVEL 13 — Agentic AI
MEDIUM P02 — Multi-Step Planner
========================================

CONCEPT:
  Complex goals need multiple steps. A planner breaks a goal
  into a sequence of actions:

    "Research a topic and write a summary"
    → ["Search for information",
       "Read and summarize",
       "Write report"]

  The planner outputs an ordered list of steps.

PROBLEM:
  Write `plan(goal)` that returns a list of step strings
  for common goals:

    "research X" → ["Search for information", "Read and summarize", "Write report"]
    "solve X" → ["Break down the problem", "Solve each part", "Combine answers"]

TRY THIS INPUT:
  ```python
  steps = plan("research AI trends")
  for s in steps:
      print(s)
  ```

EXPECTED OUTPUT:
  ```
  Search for information
  Read and summarize
  Write report
  ```

HINT:
  Check which keywords are in the goal, return the matching plan.

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# for s in plan("research AI"):
#     print(s)
