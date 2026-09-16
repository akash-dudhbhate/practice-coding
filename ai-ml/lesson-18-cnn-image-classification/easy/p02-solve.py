"""
LESSON — Cnn Image Classification
EASY P02 — Create a single `Conv2d` layer (1→16 channels, 3x3 kernel). Pass a 28x28 MNIST image through it. Print input and output shapes. Visualize a few output feature maps.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Create a single `Conv2d` layer (1→16 channels, 3x3 kernel). Pass a 28x28 MNIST image through it. Print input and output shapes. Visualize a few output feature maps


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  transform = transforms.Compose([transforms.ToTensor()])
  trainset = torchvision.datasets.MNIST(
  root="./data", train=True, download=True, transform=transform
  image, label = trainset[0]

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
