"""Solution — medium/p01-json-extract.py"""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from llm import chat


def extract(text):
    prompt = f"Extract name, age, city from: {text}. Return ONLY valid JSON."
    reply = chat(prompt, temperature=0.0)
    return json.loads(reply)
