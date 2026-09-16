"""
LESSON 01 — What is ML?
HARD P02 — Confusion Matrix Intuition
=======================================

CONCEPT:
  When a model makes predictions, there are 4 outcomes:

                Predicted YES    Predicted NO
    Actual YES   TP (correct)     FN (missed)
    Actual NO    FP (false alarm)  TN (correct)

  TP and TN = correct. FP and FN = errors.
  Accuracy = (TP + TN) / total — but accuracy alone is misleading.

PROBLEM:
  A medical test was run on 1000 patients:
    - 80 patients have the disease, 70 were correctly detected (TP)
    - 10 patients with disease were missed (FN)
    - 920 patients don't have the disease
    - 890 were correctly cleared (TN), 30 got false alarms (FP)

  Write a function `analyze()` that returns a dictionary with:
    TP, FP, TN, FN, accuracy, and worse_error

EXAMPLE OUTPUT:
  {
    "TP": 70,
    "FP": 30,
    "TN": 890,
    "FN": 10,
    "accuracy": 0.96,
    "worse_error": "false-negative"  # missing a disease is worse than a false alarm
  }
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
