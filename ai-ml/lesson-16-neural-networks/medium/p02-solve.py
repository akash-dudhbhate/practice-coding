"""
LESSON — Neural Networks
MEDIUM P02 — Train MLPClassifier with different architectures: (8,), (16, 8), (32, 16, 8). Compare accuracy and training time. Identify the best architecture for the dataset.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Train MLPClassifier with different architectures: (8,), (16, 8), (32, 16, 8). Compare accuracy and training time. Identify the best architecture for the dataset


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  iris = load_iris()
  X, y = iris.data, iris.target
  X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42, stratify=y
  scaler = StandardScaler()

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 medium/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
