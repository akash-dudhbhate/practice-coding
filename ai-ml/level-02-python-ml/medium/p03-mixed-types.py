"""
LEVEL 02 — Python for ML
MEDIUM P03 — Handle Mixed Data Types
========================================

CONCEPT:
  Real data mixes types:
    - datetime strings → pd.to_datetime()
    - categories (text) → LabelEncoder or get_dummies()
    - numbers → StandardScaler

  Models need numbers. Every column must become numeric.

PROBLEM:
  Write `process()` that creates this DataFrame and returns it processed:

      age  city       signup_date
      25   Mumbai     2024-01-15
      30   Delhi      2024-02-20
      35   Bangalore  2024-03-10
      28   Chennai    2024-01-25

  Steps:
    1. Convert signup_date → datetime (pd.to_datetime)
    2. Encode city → numbers (LabelEncoder)
    3. Scale age → standard units (StandardScaler)
  Return the processed DataFrame.

TRY THIS INPUT:
  ```python
  df = process()
  print(df)
  ```

EXPECTED OUTPUT:
  ```
     age       city signup_date  city_encoded  age_scaled
  0   25     Mumbai  2024-01-15             3   -1.236245
  1   30      Delhi  2024-02-20             2    0.137361
  2   35  Bangalore  2024-03-10             0    1.510966
  3   28    Chennai  2024-01-25             1   -0.412082
  ```

HINT:
  from sklearn.preprocessing import LabelEncoder, StandardScaler

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# df = process()
# print(df)
