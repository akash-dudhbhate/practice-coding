"""
LESSON — Linear Regression
MEDIUM P03 — Compare simple vs multiple regression: same dataset, first use one feature, then three. Compare R² and MSE. Document which is better and why.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Compare simple vs multiple regression: same dataset, first use one feature, then three. Compare R² and MSE. Document which is better and why


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = generate_data()
  X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42

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
