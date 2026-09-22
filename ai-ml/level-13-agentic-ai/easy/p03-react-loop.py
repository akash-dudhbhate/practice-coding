"""
LEVEL 13 — Agentic AI
EASY P03 — ReAct Pattern (Think → Act → Observe)
========================================

CONCEPT:
  ReAct = Reasoning + Acting. The agent thinks about what to do,
  takes an action, observes the result, and repeats until done.

    THINK: I need to calculate 6 * 7
    ACT: Use calculator tool
    OBSERVE: Result is 42
    THINK: I have the answer
    ACT: Return 42

  This is the core loop of every agent system (AutoGPT, etc.)

PROBLEM:
  Write `react_loop(goal)` that simulates a ReAct agent:
    1. Parse the goal (e.g., "calculate 6 * 7")
    2. Print the THINK/ACT/OBSERVE steps
    3. Returns the final answer (the computed result)

TRY THIS INPUT:
  ```python
  result = react_loop("calculate 6 * 7")
  print(result)   # 42
  ```

EXPECTED OUTPUT:
  ```
  THINK: I need to calculate 6 * 7
  ACT: Use calculator tool
  OBSERVE: Result is 42
  THINK: I have the answer
  ACT: Return 42
  42
  ```

HINT:
  eval("6 * 7") works, or use a simple parser.
  Print the steps, then return the number.

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(react_loop("calculate 6 * 7"))
