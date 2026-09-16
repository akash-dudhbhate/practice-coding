"""
LEVEL 00A — What is AI?
HARD P02 — What is an Agent?
==============================

CONCEPT:
  An agent = a program that DECIDES which action to take based on
  the situation, instead of following a fixed script.

  The loop is: observe → think → act → observe again.
  Below you build the "think" part — choosing the right tool.

PROBLEM:
  Write `choose_action(query)` that returns a tool name string:
    - If query contains "weather" or "temperature" → "get_weather"
    - If query contains "search" or "find" or "look up" → "web_search"
    - If query contains "email" or "send" or "mail" → "send_email"
    - If query contains "calculate" or "math" or "+" or "-" → "calculator"
    - Otherwise → "chat"

  (Check lowercase so "Send Email" works too.)

TRY THIS INPUT:
  ```python
  print(choose_action("what's the weather in Tokyo?"))
  print(choose_action("search for pizza recipes"))
  print(choose_action("send email to john@example.com"))
  print(choose_action("calculate 5 + 3"))
  print(choose_action("tell me a joke"))
  ```

EXPECTED OUTPUT:
  ```
  get_weather
  web_search
  send_email
  calculator
  chat
  ```

WHY THIS MATTERS:
  This IS the "brain" of an agent — a router that picks the tool.
  Level-13/18 build full agents with real LLM-powered routing.

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement choose_action(query)


def choose_action(query):
    """Pick which tool to use based on the user's query."""
    pass


# === TEST ===
# print(choose_action("what's the weather in Tokyo?"))
# print(choose_action("search for pizza recipes"))
# print(choose_action("send email to john@example.com"))
# print(choose_action("calculate 5 + 3"))
# print(choose_action("tell me a joke"))
