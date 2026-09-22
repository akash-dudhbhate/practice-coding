"""
LEVEL 04 — Supervised Learning
EASY P03 — Decision Tree on Iris
========================================

CONCEPT:
  DecisionTreeClassifier splits data by asking yes/no questions
  about features. max_depth limits how deep it grows
  (deeper = more overfitting risk).

  Iris dataset: 150 flowers, 4 measurements, 3 species.

PROBLEM:
  Write `train_tree()` that:
    1. Loads iris (load_iris)
    2. Splits 80/20 (random_state=42)
    3. Trains DecisionTreeClassifier(max_depth=3, random_state=42)
    4. Plots with plot_tree → 'decision_tree.png'
    5. Returns (test_accuracy, tree)

TRY THIS INPUT:
  ```python
  acc, tree = train_tree()
  print(f"{acc:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  1.0000
  ```
  (plus decision_tree.png saved)

HINT:
  from sklearn.tree import DecisionTreeClassifier, plot_tree
  Use matplotlib Agg backend or save without showing.

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# acc, t = train_tree()
# print(acc)
