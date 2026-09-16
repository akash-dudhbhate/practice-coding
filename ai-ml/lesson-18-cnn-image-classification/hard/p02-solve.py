"""
LESSON — Cnn Image Classification
HARD P02 — Use transfer learning: load pre-trained ResNet18, adapt it for CIFAR-10 (10 classes, 32x32 images), fine-tune for 5 epochs. Compare accuracy and training time with the from-scratch CNN.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Use transfer learning: load pre-trained ResNet18, adapt it for CIFAR-10 (10 classes, 32x32 images), fine-tune for 5 epochs. Compare accuracy and training time with the from-scratch CNN


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  train_loader, test_loader = get_dataloaders(batch_size=32)

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
