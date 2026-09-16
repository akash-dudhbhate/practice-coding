"""
LEVEL 14 — EASY P02 — System Prompt / Persona
============================================

The `system` parameter shapes the model's behavior before it
sees your question. Same question + different persona = different
answer style.

TASK:
  Implement `ask_with_persona(question, persona)`:
    - call chat(question, system=persona)
    - return the reply

INPUT:  ask_with_persona("Explain recursion", "You are a 5-year-old")
OUTPUT: a non-empty string

WHY: system prompts are the cheapest "fine-tuning" — no training,
  just instructions. This is how every chatbot persona works.

Run:  python3 easy/p02-system-prompt.py
CHECK: python3 check.py easy/p02
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from llm import chat


def ask_with_persona(question, persona):
    """Call chat with a system prompt."""
    # TODO
    pass


if __name__ == "__main__":
    r = ask_with_persona("Explain recursion",
                         "You explain things to a 5-year-old")
    print(f"Reply: {r}")
