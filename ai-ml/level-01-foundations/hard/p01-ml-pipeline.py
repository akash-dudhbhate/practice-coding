"""
LEVEL 01 — ML Foundations
HARD P01 — Full ML Pipeline Design
====================================

CONCEPT:
  Every ML project follows the same pipeline:
    1. Define the problem    → what are we predicting?
    2. Collect data          → where does it come from?
    3. Preprocess data       → clean, normalize, handle missing values
    4. Split data            → train/test split
    5. Choose a model        → which algorithm?
    6. Train the model       → model.fit(X_train, y_train)
    7. Evaluate              → how good is it on test data?
    8. Deploy                → put it in production

  Skipping any step = project failure.

PROBLEM:
  Design a complete ML pipeline for predicting diabetes risk.
  Write a function `design_pipeline()` that returns a dictionary
  with all 8 steps filled in.

  Steps:
    1. problem: classification or regression?
    2. data: what data do you need?
    3. preprocessing: what cleaning is needed?
    4. split: what train/test ratio?
    5. model: which algorithm to start with?
    6. training: what does training look like?
    7. evaluation: which metric matters most?
    8. deployment: how would this be used in production?

TRY THIS INPUT:
  ```python
  result = design_pipeline()
  print(result["problem"])      # "classification"
  print(result["model"])        # "logistic regression" or "decision tree"
  print(result["evaluation"])   # "recall" — missing a disease is worse
  ```

EXPECTED OUTPUT:
  ```
  {
    "problem": "classification (diabetic / not-diabetic)",
    "data": "patient records: age, BMI, blood pressure, glucose, family history",
    "preprocessing": "handle missing values, normalize numeric features, encode categories",
    "split": "80/20",
    "model": "logistic regression or decision tree",
    "training": "model.fit(X_train, y_train)",
    "evaluation": "recall — missing a disease is worse than a false alarm",
    "deployment": "API endpoint that takes patient data and returns risk score"
  }
  ```

Write your function below.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Uncomment to test your solution:
# result = design_pipeline()
# for key, value in result.items():
#     print(f"{key}: {value}")
