"""Solution — easy/p02-system-prompt.py"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from llm import chat


def ask_with_persona(question, persona):
    return chat(question, system=persona)
