"""
LEVEL 04 — Supervised Learning
MEDIUM P03 — SVM vs KNN Comparison
========================================

CONCEPT:
  SVM = finds the boundary that maximizes the margin between classes.
  KNN = classifies by the K nearest neighbors' majority vote.

  Different algorithms → different decision boundaries → different
  accuracy on the same data. Always compare!

PROBLEM:
  Write `compare_models()` that:
    1. make_classification(200, 5 features, seed=42)
    2. Split 80/20 (seed=42)
    3. SVC(seed=42) and KNeighborsClassifier(n_neighbors=5)
    4. Returns (svm_accuracy, knn_accuracy)

TRY THIS INPUT:
  ```python
  s, k = compare_models()
  print(f"SVM: {s:.4f}  KNN: {k:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  SVM: 0.8500  KNN: 0.8000
  ```

HINT:
  from sklearn.svm import SVC
  from sklearn.neighbors import KNeighborsClassifier

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# s, k = compare_models()
# print(s, k)
