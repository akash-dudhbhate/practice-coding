"""
LEVEL 13 — Agentic AI
EASY P02 — Tool Registry
========================================

CONCEPT:
  Agents have tools — a registry of functions they can call.
  A dict mapping tool name → function:

    tools = {"add": add, "multiply": multiply, "weather": get_weather}
    tools["add"](2, 3) → 5

  The agent picks a tool by name, then calls it.

PROBLEM:
  Write `build_tools()` that returns a dict:
    {"add": fn(a,b), "multiply": fn(a,b), "weather": fn(city)}
  where weather returns f"Weather in {city}: sunny"

TRY THIS INPUT:
  ```python
  tools = build_tools()
  print(tools["add"](3, 5))        # 8
  print(tools["multiply"](4, 7))   # 28
  print(tools["weather"]("Mumbai"))  # Weather in Mumbai: sunny
  ```

EXPECTED OUTPUT:
  ```
  8
  28
  Weather in Mumbai: sunny
  ```

HINT:
  Use lambdas or def functions, store in a dict.

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# t = build_tools()
# print(t["add"](3,5))
