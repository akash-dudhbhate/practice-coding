"""Solution — medium/p02-retry-parse.py"""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from llm import chat


def parse_or_retry(text):
    prompt = f"Extract name, age, city from: {text}. Return ONLY valid JSON."
    try:
        return json.loads(chat(prompt, temperature=0.0))
    except json.JSONDecodeError:
        retry = ("Your previous reply was not valid JSON. "
                 "Return ONLY the raw JSON object, no markdown, no preamble. "
                 f"Text: {text}")
        try:
            return json.loads(chat(retry, temperature=0.0))
        except json.JSONDecodeError:
            return {"error": "unparseable"}
