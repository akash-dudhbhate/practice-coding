"""
LESSON — Feature Engineering
MEDIUM P01 — Create a date column and engineer features: year, month, day of week, is_weekend, quarter. Use pandas datetime methods. Print the engineered DataFrame.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Create a date column and engineer features: year, month, day of week, is_weekend, quarter. Use pandas datetime methods. Print the engineered DataFrame


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  dates = pd.date_range(start="2024-01-01", periods=15, freq="3D")
  df = pd.DataFrame({"date": dates, "sales": np.random.randint(100, 500, size=15)})

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 medium/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
