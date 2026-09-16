"""
LEVEL 01 — ML Foundations
MEDIUM P03 — Match Algorithm to Problem
==========================================

CONCEPT:
  Different algorithms solve different types of problems:

  Linear Regression   → predicts a NUMBER (price, temperature)
  Logistic Regression → predicts a CATEGORY (spam/ham, yes/no)
  K-Means Clustering  → finds GROUPS in unlabeled data
  Decision Tree       → both, good for interpretability
  Neural Network      → complex patterns (images, text, audio)

PROBLEM:
  Match each scenario to the best algorithm. Write a function
  `match(scenario)` that returns one of:
    "linear-regression", "logistic-regression", "kmeans-clustering",
    "decision-tree", "neural-network"

  Scenarios:
    A) Predicting tomorrow's temperature (a number)
    B) Grouping customers into 5 segments (no labels)
    C) Classifying emails as spam or not spam (binary, labeled)
    D) Predicting house prices from 50 features (continuous, labeled)
    E) Recognizing objects in photos (complex patterns, labeled images)

TRY THIS INPUT:
  ```python
  print(match("A"))  # "linear-regression"
  print(match("B"))  # "kmeans-clustering"
  print(match("C"))  # "logistic-regression"
  ```

EXPECTED OUTPUT:
  ```
  linear-regression
  kmeans-clustering
  logistic-regression
  linear-regression
  neural-network
  ```

Write your function below.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Uncomment to test your solution:
# for s in ["A", "B", "C", "D", "E"]:
#     print(f"{s}: {match(s)}")
