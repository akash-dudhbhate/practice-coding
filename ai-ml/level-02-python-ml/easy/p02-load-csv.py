"""
LEVEL 02 — Python for ML
EASY P02 — Load Data into a DataFrame
========================================

CONCEPT:
  pandas DataFrame = a table of data (rows × columns).
  In ML, your dataset is almost always a DataFrame first.

  Key operations:
    - pd.DataFrame({...}) — create from dict of lists
    - df.head() — first 5 rows
    - df.shape — (rows, cols)
    - df.dtypes — type of each column

PROBLEM:
  Write `load_data()` that creates and returns this DataFrame:

      name      age  city
      Alice     25   Mumbai
      Bob       30   Delhi
      Charlie   35   Bangalore
      Diana     28   Chennai

TRY THIS INPUT:
  ```python
  df = load_data()
  print(df.head())
  print(df.shape)
  print(df.dtypes)
  ```

EXPECTED OUTPUT:
  ```
       name  age       city
  0   Alice   25     Mumbai
  1     Bob   30      Delhi
  2 Charlie   35  Bangalore
  3   Diana   28    Chennai
  (4, 3)
  name    object
  age      int64
  city    object
  dtype: object
  ```

HINT:
  pd.DataFrame({'name': [...], 'age': [...], 'city': [...]})

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# df = load_data()
# print(df.head())
