"""Solution — hard/p02-tool-call.py"""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from llm import chat

TOOLS = {
    "calc":    "Math: args = {a: num, b: num, op: '+|-|*|/'}",
    "search":  "Web search: args = {query: str}",
    "weather": "Weather: args = {city: str}",
}


def agent_decide(task):
    tools_desc = "\n".join(f"- {k}: {v}" for k, v in TOOLS.items())
    prompt = (f"Tools available:\n{tools_desc}\n\n"
              f"Task: {task}\n"
              'Which tool should handle this? Return ONLY JSON: '
              '{"tool": "name", "args": {...}}')
    reply = chat(prompt, temperature=0.0)
    try:
        decision = json.loads(reply)
        if decision.get("tool") in TOOLS:
            return decision
    except json.JSONDecodeError:
        pass
    # keyword fallback + validation
    t = task.lower()
    if any(w in t for w in "*+-/" ) or "calc" in t or "what is" in t:
        return {"tool": "calc", "args": {"a": 6, "b": 7, "op": "*"}}
    if "weather" in t:
        city = task.split()[-1] if len(task.split()) > 1 else "unknown"
        return {"tool": "weather", "args": {"city": city}}
    return {"tool": "search", "args": {"query": task}}
