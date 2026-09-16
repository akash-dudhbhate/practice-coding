"""
LEVEL 01 — ML Foundations
EASY P02 — Identify Features and Labels
========================================

CONCEPT:
  Features (X) = the INPUTS — clues the model uses to predict.
  Label (y)   = the OUTPUT — what you're trying to predict.

  Example: predicting house price
    Features: size (sq ft), bedrooms, location, age
    Label:    price

PROBLEM:
  For each scenario, identify the features (X) and label (y).
  Write a function `identify(scenario)` that returns a dict with:
    {"features": [list of features], "label": "the label"}

  Scenarios:
    A) Predicting whether a student will pass an exam
    B) Predicting the total sales of a store next month

TRY THIS INPUT:
  ```python
  result = identify("A")
  print(result["features"])  # ["study_hours", "attendance", "past_scores"]
  print(result["label"])     # "pass_fail"
  ```

EXPECTED OUTPUT:
  ```
  {"features": ["study_hours", "attendance", "past_scores"], "label": "pass_fail"}
  {"features": ["month", "last_month_sales", "season"], "label": "total_sales"}
  ```

Write your function below.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Uncomment to test your solution:
# print(identify("A"))
# print(identify("B"))
