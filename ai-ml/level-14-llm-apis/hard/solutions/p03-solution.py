"""Solution — hard/p03-cost-tracker.py"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from llm import chat

COST_PER_1K_TOKENS = 0.00015


class TrackedLLM:
    def __init__(self):
        self.calls = 0
        self.total_tokens = 0
        self.history = []

    def call(self, prompt):
        reply = chat(prompt)
        tokens = len(prompt) // 4 + len(reply) // 4
        self.calls += 1
        self.total_tokens += tokens
        self.history.append({"prompt": prompt, "reply": reply,
                             "tokens": tokens})
        return reply

    def stats(self):
        return {
            "calls": self.calls,
            "est_tokens": self.total_tokens,
            "est_cost_usd": round(self.total_tokens * COST_PER_1K_TOKENS / 1000, 6),
        }
