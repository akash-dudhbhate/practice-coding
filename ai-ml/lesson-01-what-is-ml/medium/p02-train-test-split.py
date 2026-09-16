"""
LESSON 01 — What is ML?
MEDIUM P02 — Train vs Test Split
=================================

CONCEPT:
  Train set = model learns from this (~80%).
  Test set  = used ONLY to evaluate (~20%). Model never sees it during training.
  Why? To know if the model generalizes, not just memorizes.

PROBLEM:
  Write a function `explain()` that returns a dictionary answering:

  Questions:
    1. why_split: Why do we split data into train and test?
    2. typical_ratio: What ratio is typical? (e.g., "80/20")
    3. overfitting: What is overfitting in one sentence?
    4. interpret: If train=99% and test=60%, what does this mean?

EXAMPLE OUTPUT:
  {
    "why_split": "To evaluate if the model generalizes to unseen data",
    "typical_ratio": "80/20",
    "overfitting": "Model memorizes training data including noise, fails on new data",
    "interpret": "Classic overfitting — the model memorized, didn't learn"
  }
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
