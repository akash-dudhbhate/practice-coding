"""
LESSON — Cnn Image Classification
MEDIUM P02 — Add data augmentation (RandomRotation, RandomAffine) to the MNIST training data. Train the same CNN. Compare test accuracy with and without augmentation.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Add data augmentation (RandomRotation, RandomAffine) to the MNIST training data. Train the same CNN. Compare test accuracy with and without augmentation


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  basic_transform = transforms.Compose([transforms.ToTensor()])

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
