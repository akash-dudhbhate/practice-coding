"""
LEVEL 06 — Advanced ML
EASY P02 — One-Hot Encode Categories
========================================

CONCEPT:
  Models only understand numbers. 'red', 'blue', 'green' must
  become columns: is_red, is_blue, is_green — each 0 or 1.

  pd.get_dummies(df, columns=[...]) — one-hot encoding.
  (LabelEncoder gives 0/1/2 which falsely implies order —
   only use it for truly ordinal categories.)

PROBLEM:
  Write `encode()` that:
    1. Creates DataFrame: color [red,blue,green,red,green],
       size [S,M,L,S,M]
    2. One-hot encodes BOTH columns
    3. Returns the encoded DataFrame

TRY THIS INPUT:
  ```python
  df = encode()
  print(df.shape)
  print(list(df.columns))
  ```

EXPECTED OUTPUT:
  ```
  (5, 6)
  ['color_blue', 'color_green', 'color_red', 'size_L', 'size_M', 'size_S']
  ```

HINT:
  pd.get_dummies(df) — no need to pass columns, it auto-detects objects.

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# df = encode()
# print(df.shape, list(df.columns))
