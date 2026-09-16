"""
LEVEL 14 — HARD P02 — Tool Calling via JSON
============================================

The model can't DO things — it can only DECIDE what to do.
You give it a list of tools; it returns which one + arguments
as JSON. Your code executes it.

TASK:
  Implement `agent_decide(task)`:
    - build a prompt listing the tools: calc, search, weather
    - ask: "Which tool should handle this task? Return ONLY
            JSON: {"tool": "name", "args": {...}}"
    - parse the JSON → return the dict
    - validate: tool must be one of the 3 names; if not,
      return {"tool": "unknown", "args": {}}

INPUT:  agent_decide("what is 6 * 7?")
OUTPUT: {"tool": "calc", "args": {"a": 6, "b": 7, "op": "*"}}
        (simulated mode returns a plausible dict; real API picks
         the right tool from the description)

WHY: this is EXACTLY how OpenAI function-calling and every agent
  framework works internally — LLM decides, code executes.

Run:  python3 hard/p02-tool-call.py
CHECK: python3 check.py hard/p02
"""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from llm import chat

TOOLS = {
    "calc":    "Math: args = {a: num, b: num, op: '+|-|*|/'}",
    "search":  "Web search: args = {query: str}",
    "weather": "Weather: args = {city: str}",
}


def agent_decide(task):
    """LLM picks a tool → return {"tool":..,"args":..} dict."""
    # TODO
    pass


if __name__ == "__main__":
    print(agent_decide("what is 6 * 7?"))
    print(agent_decide("weather in Mumbai"))
    print(agent_decide("find info about transformers"))
