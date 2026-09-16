"""
LEVEL 11 — LLM & Prompt Engineering
HARD P01 — Prompt Iteration & Scoring
========================================

CONCEPT:
  Prompt engineering = iterating. Write v1, test it, improve:
    v1: "Summarize this." → vague, mediocre
    v2: "Summarize in 3 bullet points." → better
    v3: "Summarize in 3 bullet points with key metrics." → best

  Score prompts by completeness, specificity, and clarity.

PROBLEM:
  Write `iterate_prompts(task)` that:
    1. Takes a task description string
    2. Returns a list of (prompt, score) tuples for v1→v3
    3. Score = how specific/complete the prompt is (0-1)

TRY THIS INPUT:
  ```python
  prompts = iterate_prompts("summarize a sales report")
  for p, s in prompts:
      print(f"{s:.2f}: {p}")
  ```

EXPECTED OUTPUT:
  ```
  0.60: Summarize this.
  0.75: Summarize in 3 bullet points.
  0.85: Summarize in 3 bullet points with key metrics.
  ```

HINT:
  Score by counting specificity features: mentions format,
  constraints, or output structure.

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# for p, s in iterate_prompts("summarize"):
#     print(s, p)
