"""
LEVEL 14 — HARD P03 — Cost Tracker
====================================

LLM calls cost money — billed per TOKEN (~4 chars ≈ 1 token).
Build a wrapper that tracks usage so you never get surprised.

TASK:
  Implement class `TrackedLLM`:
    - .call(prompt) → calls chat(), tracks stats, returns reply
    - .stats() → {"calls": n, "est_tokens": t, "est_cost_usd": c}
      where est_tokens = total chars sent / 4
      and est_cost_usd = est_tokens * $0.00015/1K (gpt-4o-mini rate)
    - .history → list of {"prompt":..., "reply":..., "tokens":...}

INPUT:
    llm = TrackedLLM()
    llm.call("hello")
    llm.call("what is AI?")
    llm.stats()

OUTPUT: {"calls": 2, "est_tokens": 5, "est_cost_usd": 0.0000x}

WHY: production LLM apps MUST track usage — a runaway loop or
  a chatty user can burn real money. This is rate-limiting's
  foundation.

Run:  python3 hard/p03-cost-tracker.py
CHECK: python3 check.py hard/p03
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from llm import chat

COST_PER_1K_TOKENS = 0.00015   # gpt-4o-mini input rate


class TrackedLLM:
    def __init__(self):
        # TODO: init counters
        pass

    def call(self, prompt):
        # TODO: chat() + track
        pass

    def stats(self):
        # TODO: return dict
        pass


if __name__ == "__main__":
    llm = TrackedLLM()
    llm.call("hello")
    llm.call("what is AI?")
    print(llm.stats())
    print(f"History entries: {len(llm.history)}")
