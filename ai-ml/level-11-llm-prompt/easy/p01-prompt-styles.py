"""
LEVEL 11 — LLM & Prompt Engineering
EASY P01 — Three Prompt Styles
========================================

CONCEPT:
  Same task, different prompts → different quality:

  Vague:     "Summarize this."
  Detailed:  "Summarize this in 3 bullet points."
  Structured: "Summarize as JSON with keys: main_point, key_details."

  More specific = more predictable output.

PROBLEM:
  Write `make_prompts(text)` that returns a dict:
    {"simple": ..., "detailed": ..., "structured": ...}
  Each builds a prompt string for summarizing `text`.

TRY THIS INPUT:
  ```python
  p = make_prompts("ML models learn from data")
  print(p["simple"])
  print(p["detailed"])
  print(p["structured"])
  ```

EXPECTED OUTPUT:
  ```
  Summarize this text.
  Summarize this text in 3 bullet points.
  Summarize this text as JSON with keys: main_point, key_details.
  ```

HINT:
  f-strings: f"Summarize this text." — the text is appended after.

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# p = make_prompts("test")
# print(p)
