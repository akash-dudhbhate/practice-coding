"""
LEVEL 14 — MEDIUM P02 — Retry on Parse Failure
==============================================

Real LLMs sometimes return malformed JSON — "Here's the JSON: {...}"
or trailing commas. Production code RETRIES instead of crashing.

TASK:
  Implement `parse_or_retry(text)`:
    - first attempt: prompt + json.loads (like p01)
    - if json.loads raises → retry ONCE with a stronger prompt:
      "Your previous reply was not valid JSON. Return ONLY the
       raw JSON object, no markdown, no preamble."
    - if second attempt also fails → return {"error": "unparseable"}
    - return the dict on success

INPUT:  parse_or_retry("Alice is 30, lives in Paris")
OUTPUT: {"name": ..., "age": ..., "city": ...} or {"error": ...}

WHY: LLM output is unreliable — never assume parseable.
  One retry fixes ~90% of malformed responses.

Run:  python3 medium/p02-retry-parse.py
CHECK: python3 check.py medium/p02
"""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from llm import chat


def parse_or_retry(text):
    """Try to parse JSON; retry once on failure; else error dict."""
    # TODO
    pass


if __name__ == "__main__":
    d = parse_or_retry("Alice is 30, lives in Paris")
    print(d)
