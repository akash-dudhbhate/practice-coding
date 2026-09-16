"""Solution — easy/p03-temperature.py"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from llm import chat


def creative_vs_precise(prompt):
    precise = chat(prompt, temperature=0.0)
    creative = chat(prompt, temperature=0.9)
    return precise, creative
