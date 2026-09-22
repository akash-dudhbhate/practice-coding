"""
LEVEL 13 — Agentic AI
MEDIUM P03 — Memory (Context Window)
========================================

CONCEPT:
  Agents need memory — what has the user told us before?
  Store facts and include them in every response.

    memory = ["User likes Python", "User is learning ML"]
    response = f"Based on [{memory}], here's my answer to: {question}"

PROBLEM:
  Write `AgentMemory` class with:
    - `add(fact)` — store a fact
    - `get_all()` — return all facts
    - `respond(question)` — return f"Based on [fact1 | fact2 | ...], here's my response to: {question}"

TRY THIS INPUT:
  ```python
  m = AgentMemory()
  m.add("User likes Python")
  m.add("User is learning ML")
  print(m.respond("What should I learn next?"))
  ```

EXPECTED OUTPUT:
  ```
  Based on [User likes Python | User is learning ML], here's my response to: What should I learn next?
  ```

HINT:
  Store facts in a list; join with " | ".

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# m = AgentMemory()
# m.add("User likes Python")
# print(m.respond("What next?"))
