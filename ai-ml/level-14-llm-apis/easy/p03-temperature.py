"""
LEVEL 14 — EASY P03 — Temperature: Creative vs Precise
======================================================

Same prompt, two temperatures. temp=0.0 → deterministic/extraction.
temp=0.9 → creative/varied. You'll SEE the difference.

PROBLEM:
  Implement `creative_vs_precise(prompt)`:
    - call chat(prompt, temperature=0.0) → precise reply
    - call chat(prompt, temperature=0.9) → creative reply
    - return (precise, creative) tuple

TRY THIS INPUT:   creative_vs_precise("Write a tagline for a coffee shop")
EXPECTED OUTPUT:  (precise_string, creative_string)

WHY: extraction/classification want temp=0 (repeatable).
  Brainstorming/writing want temp~0.8 (varied). Know which to use.

RUN: python3 easy/p03-temperature.py
CHECK: python3 check.py easy/p03
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from llm import chat


def creative_vs_precise(prompt):
    """Return (precise_reply, creative_reply)."""
    # TODO
    pass


if __name__ == "__main__":
    p, c = creative_vs_precise("Write a tagline for a coffee shop")
    print(f"Precise (t=0):  {p}")
    print(f"Creative (t=0.9): {c}")
