"""Solution — hard/p01-stream-tokens.py"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from llm import chat


def stream(prompt):
    reply = chat(prompt)
    for word in reply.split():
        yield word + " "
