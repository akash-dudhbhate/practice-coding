"""
LESSON — Cnn Image Classification
MEDIUM P03 — Build a CNN for CIFAR-10 (3 color channels, 32x32 images, 10 classes). Train for 5 epochs. Print test accuracy. Handle the 3-channel input correctly.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a CNN for CIFAR-10 (3 color channels, 32x32 images, 10 classes). Train for 5 epochs. Print test accuracy. Handle the 3-channel input correctly


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
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
    python3 medium/solutions/p03-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
