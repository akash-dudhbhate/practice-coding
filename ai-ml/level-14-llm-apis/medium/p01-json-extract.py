"""
LEVEL 14 — MEDIUM P01 — JSON Extraction
======================================

LLMs output text. But your code needs STRUCTURED data.
The fix: prompt for JSON, parse it, handle failure.

TASK:
  Implement `extract(text)`:
    - prompt: "Extract name, age, city from: {text}.
               Return ONLY valid JSON."
    - call chat()
    - json.loads the reply
    - return the dict

INPUT:  extract("My name is Alice, I'm 30, from Paris")
OUTPUT: {"name": "Alice", "age": 30, "city": "Paris"}
        (in simulated mode: returns canned dict with these keys)

WHY: every real LLM app needs structured output — this is how
  you feed LLM answers into databases, APIs, other code.

Run:  python3 medium/p01-json-extract.py
CHECK: python3 check.py medium/p01
"""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from llm import chat


def extract(text):
    """Prompt for JSON, parse, return dict."""
    # TODO
    pass


if __name__ == "__main__":
    d = extract("My name is Alice, I'm 30, from Paris")
    print(d)
