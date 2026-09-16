"""
LEVEL 11 — LLM & Prompt Engineering
MEDIUM P02 — Persona + Format + Context Prompt
========================================

CONCEPT:
  A powerful prompt has THREE parts:
    1. PERSONA: "You are a data scientist."
    2. FORMAT:  "Format your response as: 3 bullet points"
    3. CONTEXT: "Context: machine learning basics"

  This structure gives consistent, well-formatted, role-appropriate
  responses every time.

PROBLEM:
  Write `structured_prompt(persona, context, format, question)`
  that builds a prompt string with all three parts plus the question.

TRY THIS INPUT:
  ```python
  p = structured_prompt("data scientist", "machine learning basics",
                         "3 bullet points", "What is overfitting?")
  print(p)
  ```

EXPECTED OUTPUT:
  ```
  You are a data scientist. Your task is to explain a concept.

  Context: machine learning basics

  Format your response as:
  3 bullet points

  Input: What is overfitting?
  ```

HINT:
  f-string with \n\n between sections.

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(structured_prompt("data scientist", "ML basics", "3 bullets", "What is overfitting?"))
