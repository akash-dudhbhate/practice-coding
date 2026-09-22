"""Solution — easy/p01-first-call.py"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from llm import chat


def ask_llm(question):
    return chat(question)
