"""
LEVEL 02 — Python for ML
EASY P03 — Fill Missing Values
========================================

CONCEPT:
  Real data has missing values (NaN = "Not a Number").
  Models can't handle NaN — you must fill them ("imputation").

  Strategy:
    - Numeric column  → fill with MEDIAN (robust to outliers)
    - Category column → fill with MODE (most frequent value)

  Methods:
    - df['col'].median()
    - df['col'].mode()[0]
    - df['col'].fillna(value)

PROBLEM:
  Write `fill_missing()` that creates this DataFrame and fills NaN:

      age   city      score
      25    Mumbai    85
      NaN   Delhi     90
      30    NaN       NaN
      NaN   Chennai   78
      35    NaN       92

  Fill: age→median, score→median, city→mode.
  Return the cleaned DataFrame.

TRY THIS INPUT:
  ```python
  df = fill_missing()
  print(df)
  ```

EXPECTED OUTPUT:
  ```
      age     city  score
  0  25.0   Mumbai   85.0
  1  30.0    Delhi   90.0
  2  30.0  Chennai   87.5
  3  30.0  Chennai   78.0
  4  35.0  Chennai   92.0
  ```

HINT:
  Median of [25, 30, 35] = 30.  Mode of cities = 'Chennai' (appears 2x).
  Median of [85, 90, 78, 92] = 87.5.

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# df = fill_missing()
# print(df)
