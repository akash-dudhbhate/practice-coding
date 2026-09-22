"""
LEVEL 01 — ML Foundations
MEDIUM P02 — Train vs Test Split
=====================================

CONCEPT:
  You split data into:
    - Training set (~80%): model learns from this
    - Test set (~20%): used ONLY to evaluate — model never sees it

  Why? To know if the model GENERALIZES (works on new data),
  not just memorizes. Testing on training data is like grading
  a student on the exact questions they studied — meaningless.

PROBLEM:
  Write a function `explain()` that returns a dictionary answering:

  Questions:
    1. why_split: Why do we split data into train and test?
    2. typical_ratio: What ratio is typical? (e.g., "80/20")
    3. overfitting: What is overfitting in one sentence?
    4. interpret: If train=99% and test=60%, what does this mean?

TRY THIS INPUT:
  ```python
  result = explain()
  print(result["why_split"])      # "To evaluate on unseen data"
  print(result["typical_ratio"])  # "80/20"
  ```

EXPECTED OUTPUT:
  ```
  {
    "why_split": "To evaluate if the model generalizes to unseen data",
    "typical_ratio": "80/20",
    "overfitting": "Model memorizes training data including noise, fails on new data",
    "interpret": "Classic overfitting — the model memorized, didn't learn"
  }
  ```

Write your function below.
CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Uncomment to test your solution:
# result = explain()
# for key, value in result.items():
#     print(f"{key}: {value}")
