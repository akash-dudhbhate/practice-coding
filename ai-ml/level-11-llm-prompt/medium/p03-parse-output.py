"""
LEVEL 11 — LLM & Prompt Engineering
MEDIUM P03 — Parse Structured LLM Output
========================================

CONCEPT:
  LLMs output text. For programmatic use, ask for JSON and parse it:
    "Return JSON: {"score": 0.95, "category": "positive"}"

  Then json.loads() to extract the data.

PROBLEM:
  Write `parse_llm_output(text)` that:
    1. Finds JSON inside a text response
    2. Parses and returns it as a Python dict
    3. Returns None if no valid JSON found

TRY THIS INPUT:
  ```python
  text = 'The sentiment is: {"score": 0.95, "category": "positive"}'
  print(parse_llm_output(text))
  ```

EXPECTED OUTPUT:
  ```
  {'score': 0.95, 'category': 'positive'}
  ```

HINT:
  Find the JSON substring between { and }, then json.loads().

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# t = 'Score: {"score": 0.95, "category": "positive"}'
# print(parse_llm_output(t))
