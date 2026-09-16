"""
LESSON — Imbalanced Data
HARD P02 — Build a fraud detection simulation: create synthetic transaction data (amount, merchant, time, is_fraud). Handle imbalance with SMOTE. Train a model. Plot the precision-recall curve. Find the threshold that gives 80% recall. Report the precision at that threshold.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a fraud detection simulation: create synthetic transaction data (amount, merchant, time, is_fraud). Handle imbalance with SMOTE. Train a model. Plot the precision-recall curve. Find the threshold that gives 80% recall. Report the precision at that threshold


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  n = 5000
  amount = np.random.exponential(scale=50, size=n)
  merchant = np.random.choice(["Amazon", "Walmart", "Target", "BestBuy", "Other"], n)
  hour = np.random.randint(0, 24, n)
  distance = np.random.exponential(scale=100, size=n)

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
