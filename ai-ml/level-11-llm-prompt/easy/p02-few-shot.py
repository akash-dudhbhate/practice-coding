"""
LEVEL 11 — LLM & Prompt Engineering
EASY P02 — Few-Shot Classification Prompt
========================================

CONCEPT:
  Few-shot prompting = show examples in the prompt so the model
  learns the pattern:

    "Classify sentiment:
     'I love it' → Positive
     'Terrible' → Negative
     'Meh' → Neutral
     'This is amazing!' → ?"

  The model continues the pattern — no training needed.

PROBLEM:
  Write `few_shot_prompt(examples, query)` that builds a prompt:
    - examples: list of (text, label) tuples
    - query: the text to classify
    Returns the full prompt string.

TRY THIS INPUT:
  ```python
  examples = [("I love it", "Positive"), ("Terrible", "Negative"),
              ("Meh", "Neutral")]
  p = few_shot_prompt(examples, "This is amazing!")
  print(p)
  ```

EXPECTED OUTPUT:
  ```
  Classify the sentiment:

  Text: "I love it" → Positive
  Text: "Terrible" → Negative
  Text: "Meh" → Neutral
  Text: "This is amazing!" →
  ```

HINT:
  Build a string with the examples formatted as 'Text: "..." → Label'

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# ex = [("I love it","Positive"),("Terrible","Negative")]
# print(few_shot_prompt(ex, "Great!"))
