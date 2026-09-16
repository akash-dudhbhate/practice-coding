"""
LESSON — Cnn Image Classification
EASY P03 — Create a `MaxPool2d` layer (2x2). Pass a 28x28 tensor through it. Print input and output shapes. Verify the spatial dimension is halved.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Create a `MaxPool2d` layer (2x2). Pass a 28x28 tensor through it. Print input and output shapes. Verify the spatial dimension is halved


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  x = torch.randn(1, 1, 28, 28)

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 easy/solutions/p03-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
