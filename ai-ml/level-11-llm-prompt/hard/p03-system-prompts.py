"""
LEVEL 11 — LLM & Prompt Engineering
HARD P03 — System Prompt Personas
========================================

CONCEPT:
  System prompts set the model's personality and constraints:
    "You are a helpful assistant." → generic
    "You are an expert data scientist." → technical, detailed
    "You are a critical reviewer." → finds flaws

  Different personas → same question, different answer style.

PROBLEM:
  Write `get_personas()` that returns a dict of 4 personas:
    {"helpful": ..., "expert": ..., "creative": ..., "critical": ...}
  Each is a system prompt string.

TRY THIS INPUT:
  ```python
  p = get_personas()
  print(p["expert"])
  ```

EXPECTED OUTPUT:
  ```
  You are an expert data scientist. Provide detailed technical explanations.
  ```

HINT:
  Four different system prompt strings, each setting a different role.

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# p = get_personas()
# for k, v in p.items():
#     print(f"{k}: {v}")
