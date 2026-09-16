"""
LESSON 01 — What is ML?
MEDIUM P03 — Match Algorithm to Problem
========================================

CONCEPT:
  Linear Regression   → predicts a NUMBER
  Logistic Regression → predicts a CATEGORY
  K-Means Clustering  → finds GROUPS in unlabeled data
  Decision Tree       → both, interpretable
  Neural Network      → complex patterns (images, text, audio)

PROBLEM:
  Match each scenario to the best algorithm. Write a function `match(scenario)`
  that returns one of:
    "linear-regression", "logistic-regression", "kmeans-clustering",
    "decision-tree", "neural-network"

  Scenarios:
    A) Predicting tomorrow's temperature (a number)
    B) Grouping customers into 5 segments (no labels)
    C) Classifying emails as spam or not spam (binary, labeled)
    D) Predicting house prices from 50 features (continuous, labeled)
    E) Recognizing objects in photos (complex patterns, labeled images)

EXAMPLE:
  Input:  match("A")
  Output: "linear-regression"

  Input:  match("B")
  Output: "kmeans-clustering"

EXPECTED OUTPUT:
  A: linear-regression
  B: kmeans-clustering
  C: logistic-regression
  D: linear-regression
  E: neural-network
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
