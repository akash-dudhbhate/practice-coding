"""
LESSON — Cnn Image Classification
HARD P01 — Build a complete CNN pipeline: load CIFAR-10, augment data, build a 3-block CNN (conv→relu→pool × 3 + FC), train with Adam, track train/val loss and accuracy, plot both curves, and evaluate on test set. Target: >70% accuracy.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a complete CNN pipeline: load CIFAR-10, augment data, build a 3-block CNN (conv→relu→pool × 3 + FC), train with Adam, track train/val loss and accuracy, plot both curves, and evaluate on test set. Target: >70% accuracy


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
