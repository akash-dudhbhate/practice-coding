"""
LESSON 01 — What is ML?
HARD P01 — Full ML Pipeline Design
===================================

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

PROBLEM:
  Design a complete ML pipeline for predicting diabetes risk.
  Write a function `design_pipeline()` that returns a dictionary with all 8 steps.

EXAMPLE OUTPUT:
  {
    "problem": "classification (diabetic / not-diabetic)",
    "data": "patient records: age, BMI, blood pressure, glucose, family history",
    "preprocessing": "handle missing values, normalize numeric features, encode categories",
    "split": "80/20",
    "model": "logistic regression or decision tree (simple, interpretable)",
    "training": "model.fit(X_train, y_train) on the training set",
    "evaluation": "accuracy, precision, recall, F1 — recall matters most",
    "deployment": "API endpoint that takes patient data and returns risk prediction"
  }
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
