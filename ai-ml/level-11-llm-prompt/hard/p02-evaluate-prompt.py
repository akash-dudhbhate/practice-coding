"""
LEVEL 11 — LLM & Prompt Engineering
HARD P02 — Prompt Evaluation Framework
========================================

CONCEPT:
  Before shipping a prompt, evaluate it:
    - Does the output meet length requirements?
    - Does it follow the requested format?
    - Is it accurate?

  Build an evaluator: checks a response against criteria.

PROBLEM:
  Write `evaluate_response(response, criteria)` that:
    - criteria = {"max_length": 100, "format": "bullet", "contains": "keyword"}
    - Returns {"length": bool, "format": bool, "accuracy": bool}

TRY THIS INPUT:
  ```python
  r = evaluate_response(
      "- Point one\n- Point two\n- Point three",
      {"max_length": 100, "format": "bullet", "contains": "point"})
  print(r)
  ```

EXPECTED OUTPUT:
  ```
  {'length': True, 'format': True, 'accuracy': True}
  ```

HINT:
  "format": "bullet" → check if lines start with "- " or "•"
  "contains" → check if keyword is in response (case-insensitive)

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# r = evaluate_response("- a\n- b", {"max_length": 50, "format": "bullet", "contains": "a"})
# print(r)
