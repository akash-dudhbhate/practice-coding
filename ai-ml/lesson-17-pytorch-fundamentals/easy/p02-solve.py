"""
LESSON — Pytorch Fundamentals
EASY P02 — Use autograd: create a tensor with `requires_grad=True`, compute y = x³ + 2x² + 1, call `backward()`, print the gradient (dy/dx = 3x² + 4x). Verify manually.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Use autograd: create a tensor with `requires_grad=True`, compute y = x³ + 2x² + 1, call `backward()`, print the gradient (dy/dx = 3x² + 4x). Verify manually


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  x = torch.tensor([2.0], requires_grad=True)

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 easy/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
