"""
LEVEL 14 — EASY P01 — First Real LLM Call
==========================================

The simplest possible LLM interaction. One function, one call.

PROBLEM:
  Implement `ask_llm(question)`:
    - import `chat` from llm.py  (sys.path insert is done below)
    - call it with the question
    - return the reply string

TRY THIS INPUT:   ask_llm("What is 2+2?")
EXPECTED OUTPUT:  a non-empty string — in simulated mode it echoes the prompt;
        with Ollama/OpenAI it's a real model reply.

RUN: python3 easy/p01-first-call.py
CHECK: python3 check.py easy/p01
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from llm import chat


def ask_llm(question):
    """Call chat() and return the reply."""
    # TODO
    pass


if __name__ == "__main__":
    r = ask_llm("What is 2+2?")
    print(f"Reply: {r}")
