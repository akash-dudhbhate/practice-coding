"""
LEVEL 13 — Agentic AI
HARD P01 — Multi-Agent System
========================================

CONCEPT:
  Multiple specialized agents work together:
    Researcher → gathers info
    Writer → creates content
    Reviewer → checks quality

  Each has a role; they pass work between them.

PROBLEM:
  Write `multi_agent(task)` that:
    1. Creates 3 agents: researcher, writer, reviewer
    2. Each takes the task, returns their contribution
    3. Returns dict: {"researcher": ..., "writer": ..., "reviewer": ...}

TRY THIS INPUT:
  ```python
  r = multi_agent("Write a blog post")
  for role, output in r.items():
      print(f"{role}: {output}")
  ```

EXPECTED OUTPUT:
  ```
  researcher: Working on Write a blog post
  writer: Working on Write a blog post
  reviewer: Working on Write a blog post
  ```

HINT:
  Each agent is a function that wraps the task string.

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# r = multi_agent("Write a blog post")
# print(r)
