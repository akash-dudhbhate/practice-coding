"""
LEVEL 14 — HARD P01 — Streaming Tokens
=======================================

Real APIs stream tokens one at a time — the user sees text appear
as it's generated. Your job: implement a `stream()` generator
that yields chunks.

PROBLEM:
  Implement `stream(prompt)` — a GENERATOR (use `yield`):
    - get the full reply from chat()
    - split into word-chunks
    - yield each chunk with a trailing space
    (in real APIs, you'd iterate the response stream — here we
     simulate it so the CODE SHAPE is identical)

TRY THIS INPUT:   list(stream("Tell me a joke"))
EXPECTED OUTPUT:  ["Why", "did", "the", "chicken", ...] — word chunks

WHY: streaming = perceived speed. ChatGPT types character by
  character for this exact reason. Your code must handle
  a generator, not a string.

RUN: python3 hard/p01-stream-tokens.py
CHECK: python3 check.py hard/p01
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from llm import chat


def stream(prompt):
    """Yield reply chunks word-by-word (simulated streaming)."""
    # TODO — use yield
    pass


if __name__ == "__main__":
    chunks = list(stream("Tell me a joke"))
    print("".join(chunks))
