"""
LESSON — Feature Engineering
MEDIUM P02 — Create a house dataset (sqft, bedrooms, price). Engineer: price_per_sqft, total_rooms, bedrooms_per_sqft. Train a model with and without engineered features. Compare R².
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Create a house dataset (sqft, bedrooms, price). Engineer: price_per_sqft, total_rooms, bedrooms_per_sqft. Train a model with and without engineered features. Compare R²


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  n = 200
  sqft = np.random.randint(800, 4000, n)
  bedrooms = np.random.randint(1, 6, n)
  bathrooms = np.random.randint(1, 4, n)
  price = sqft * 150 + bedrooms * 10000 + bathrooms * 5000 + np.random.normal(0, 20000, n)

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
