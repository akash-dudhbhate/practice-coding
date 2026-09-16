"""
LESSON — Data Visualization
HARD P01 — Full EDA function
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Write a function that takes a DataFrame and performs complete EDA: prints shape, dtypes, missing values, and describe(); creates and saves a figure with 4 subplots (histogram of a numeric column, box plot by a categorical column, scatter of two numeric columns, and a correlation heatmap). Return a summary dictionary


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  n = 300
  df = pd.DataFrame({
  df.loc[df.sample(20).index, "income"] = np.nan
  df.loc[df.sample(10).index, "score"] = np.nan

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
