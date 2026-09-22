"""
LEVEL 13 PROJECT — Personal Task Agent
========================================

Build a complete mini-agent that combines everything from this
level: tools + planner + memory + ReAct loop.

BUILD class `TaskAgent`:
  - __init__(): sets up tools registry and empty memory
  - add_tool(name, fn): register a tool
  - remember(fact): store a fact
  - run(task): full loop —
      1. THINK: decide which tool fits the task (keyword match)
      2. ACT: call it with parsed args
      3. OBSERVE: store result in memory
      4. Return (tool_used, result)

DEFAULT TOOLS to register in __init__:
  - "calc": eval-safe math  (a, b, op) → number
  - "search": fake search   (query) → f"Results for: {query}"
  - "summarize": (text) → first 50 chars + "..."
  - "weather": (city) → f"Weather in {city}: sunny"

TEST RUN:
  ```python
  agent = TaskAgent()
  print(agent.run("calc 6 * 7"))
  print(agent.run("search agentic ai"))
  print(agent.run("weather Mumbai"))
  print(agent.memory)   # should contain 3 observations
  ```

EXPECTED:
  ```
  ('calc', 42)
  ('search', 'Results for: agentic ai')
  ('weather', 'Weather in Mumbai: sunny')
  ['calc → 42', 'search → Results...', 'weather → ...']
  ```

STRETCH: add a 2-step task — "search X then summarize" — where
  run() chains two tools automatically.
"""

# === WRITE YOUR CODE BELOW ===

class TaskAgent:
    def __init__(self):
        # TODO: register default tools, init memory list
        pass

    def add_tool(self, name, fn):
        pass

    def remember(self, fact):
        pass

    def run(self, task):
        # TODO: think → act → observe → return
        pass


if __name__ == "__main__":
    agent = TaskAgent()
    print(agent.run("calc 6 * 7"))
    print(agent.run("search agentic ai"))
    print(agent.run("weather Mumbai"))
    print("Memory:", agent.memory)
