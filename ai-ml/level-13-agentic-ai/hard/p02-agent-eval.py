"""
LEVEL 13 — Agentic AI
HARD P02 — Agent Evaluation
========================================

CONCEPT:
  Evaluate agents on three dimensions:
    correctness — did it get the right answer?
    efficiency — did it use the minimum steps?
    completeness — did it address all parts of the goal?

  Score each on 0-1.

PROBLEM:
  Write `evaluate_agent(agent_output, expected, steps_used, min_steps, covered_parts, total_parts)`:
    - correctness = 1.0 if agent_output == expected else 0.5
    - efficiency = min_steps / steps_used (cap at 1.0)
    - completeness = covered_parts / total_parts
    - Returns dict of all three scores

TRY THIS INPUT:
  ```python
  r = evaluate_agent("42", "42", 3, 3, 2, 3)
  print(r)
  ```

EXPECTED OUTPUT:
  ```
  {'correctness': 1.0, 'efficiency': 1.0, 'completeness': 0.67}
  ```

HINT:
  Each metric is a simple ratio, capped at 1.0.

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# r = evaluate_agent("42", "42", 3, 3, 2, 3)
# print(r)
