"""
LEVEL 11 — LLM & Prompt Engineering
MEDIUM P01 — Chain-of-Thought Prompting
========================================

CONCEPT:
  Chain-of-thought (CoT) = tell the model to "think step by step."
  This dramatically improves math/logic reasoning:

    "Solve this step by step:
     Problem: 3 apples for $2, how much for 12?
     Step 1: Find cost per apple.
     Step 2: Multiply."

  The model generates the reasoning, then the answer follows.

PROBLEM:
  Write `chain_of_thought(problem)` that builds a CoT prompt:
    - Takes a math/logic problem string
    - Returns a prompt asking for step-by-step solution

TRY THIS INPUT:
  ```python
  p = chain_of_thought("If 3 apples cost $2, how much do 12 cost?")
  print(p)
  ```

EXPECTED OUTPUT:
  ```
  Solve this step by step:

  Problem: If 3 apples cost $2, how much do 12 cost?

  Step 1: Find the cost per apple.
  $2 / 3 = $0.67 per apple

  Step 2: Multiply by the number of apples.
  $0.67 × 12 = $8.00
  ```

HINT:
  The prompt should guide the model through the reasoning steps.

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(chain_of_thought("If 3 apples cost $2, how much do 12 cost?"))
