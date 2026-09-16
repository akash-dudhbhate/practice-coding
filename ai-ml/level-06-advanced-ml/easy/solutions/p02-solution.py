"""Level 06 — Advanced ML — Easy P02 Solution"""

import pandas as pd

def encode():
    df = pd.DataFrame({
        'color': ['red', 'blue', 'green', 'red', 'green'],
        'size': ['S', 'M', 'L', 'S', 'M']
    })
    return pd.get_dummies(df)

if __name__ == "__main__":
    df = encode()
    print(df.shape)
    print(list(df.columns))
    print(df)
