"""
LEVEL 13 — Agentic AI
MEDIUM P01 — Tool-Calling Agent
========================================

CONCEPT:
  A real agent receives a task, picks a tool, executes it,
  and returns the result. This connects decide + tools.

PROBLEM:
  Write `run_agent(task)` that:
    1. Decides which tool to use (add, multiply, weather)
    2. Calls it with parsed arguments
    3. Returns (tool_name, result)

  Task formats:
    "add 2 and 3" → ("add", 5)
    "multiply 4 and 7" → ("multiply", 28)
    "weather Mumbai" → ("weather", "Weather in Mumbai: sunny")

TRY THIS INPUT:
  ```python
  print(run_agent("add 2 and 3"))
  print(run_agent("multiply 4 and 7"))
  print(run_agent("weather Mumbai"))
  ```

EXPECTED OUTPUT:
  ```
  ('add', 5)
  ('multiply', 28)
  ('weather', 'Weather in Mumbai: sunny')
  ```

HINT:
  Parse the task with .split() — extract numbers and tool name.

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(run_agent("add 2 and 3"))
