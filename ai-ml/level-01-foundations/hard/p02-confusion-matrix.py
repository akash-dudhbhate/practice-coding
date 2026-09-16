"""
LEVEL 01 — ML Foundations
HARD P02 — Confusion Matrix Intuition
========================================

CONCEPT:
  When a model makes predictions, there are 4 outcomes:

                Predicted YES    Predicted NO
    Actual YES   TP (correct)     FN (missed)
    Actual NO    FP (false alarm)  TN (correct)

  TP and TN = correct. FP and FN = errors.
  Accuracy = (TP + TN) / total — but misleading for imbalanced data.

  Example: if 99% of emails are not spam, a model that always says
  "not spam" is 99% accurate but completely useless.

PROBLEM:
  A medical test was run on 1000 patients:
    - 80 patients have the disease, 70 were correctly detected (TP)
    - 10 patients with disease were missed (FN)
    - 920 patients don't have the disease
    - 890 were correctly cleared (TN), 30 got false alarms (FP)

  Write a function `analyze()` that returns a dictionary with:
    TP, FP, TN, FN, accuracy, and worse_error

  worse_error should be "false-positive" or "false-negative" —
  which is worse for a medical test?

TRY THIS INPUT:
  ```python
  result = analyze()
  print(result["TP"])          # 70
  print(result["FN"])          # 10
  print(result["accuracy"])    # 0.96
  print(result["worse_error"]) # "false-negative"
  ```

EXPECTED OUTPUT:
  ```
  {
    "TP": 70,
    "FP": 30,
    "TN": 890,
    "FN": 10,
    "accuracy": 0.96,
    "worse_error": "false-negative"
  }
  ```

Write your function below.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Uncomment to test your solution:
# result = analyze()
# for key, value in result.items():
#     print(f"{key}: {value}")
