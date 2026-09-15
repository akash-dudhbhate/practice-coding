"""
Lesson 01 - Medium P03
Match algorithms to problem types.

Solution:
  For each algorithm, state the problem type it is best suited for and why.
"""

# ---------------------------------------------------------------------------
# Algorithm -> Problem type mapping
# ---------------------------------------------------------------------------
matches = [
    {
        "algorithm": "Linear Regression",
        "problem_type": "Regression",
        "why": "Predicts a continuous numeric output as a linear function of the features.",
    },
    {
        "algorithm": "Logistic Regression",
        "problem_type": "Classification (binary or multiclass)",
        "why": "Models the probability of a discrete class using the logistic (sigmoid) function.",
    },
    {
        "algorithm": "K-Means Clustering",
        "problem_type": "Unsupervised (clustering)",
        "why": "Groups unlabeled data into K clusters by minimizing within-cluster variance; no target labels needed.",
    },
    {
        "algorithm": "Decision Tree",
        "problem_type": "Classification or Regression",
        "why": "Splits data by feature thresholds; can output a class label (classifier) or a numeric value (regressor).",
    },
    {
        "algorithm": "Random Forest",
        "problem_type": "Classification or Regression",
        "why": "Ensemble of decision trees; reduces overfitting and works for both discrete and continuous targets.",
    },
    {
        "algorithm": "K-Nearest Neighbors (KNN)",
        "problem_type": "Classification or Regression",
        "why": "Predicts by majority vote (classification) or averaging (regression) of the K nearest training points.",
    },
    {
        "algorithm": "Support Vector Machine (SVM)",
        "problem_type": "Classification (also Regression with SVR)",
        "why": "Finds the maximum-margin separating hyperplane; primarily used for classification tasks.",
    },
    {
        "algorithm": "PCA (Principal Component Analysis)",
        "problem_type": "Unsupervised (dimensionality reduction)",
        "why": "Reduces feature dimensionality without using labels by maximizing variance along principal components.",
    },
]

# ---------------------------------------------------------------------------
# Print the matching table
# ---------------------------------------------------------------------------
print(f"{'Algorithm':<35} {'Problem Type':<40}")
print("-" * 75)
for m in matches:
    print(f"{m['algorithm']:<35} {m['problem_type']:<40}")

print()
print("Detailed reasons:")
print("-" * 75)
for m in matches:
    print(f"  {m['algorithm']} -> {m['problem_type']}")
    print(f"    {m['why']}")
    print()
