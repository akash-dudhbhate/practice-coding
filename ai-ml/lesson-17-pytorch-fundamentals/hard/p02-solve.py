"""
LESSON — Pytorch Fundamentals
HARD P02 — Implement a neural network from scratch using only tensors and autograd (no nn.Module). Define weights as tensors with requires_grad=True. Implement forward and backward manually. Train on make_moons. Plot the decision boundary.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Implement a neural network from scratch using only tensors and autograd (no nn.Module). Define weights as tensors with requires_grad=True. Implement forward and backward manually. Train on make_moons. Plot the decision boundary


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_moons(n_samples=500, noise=0.2, random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42
  scaler = StandardScaler()

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
