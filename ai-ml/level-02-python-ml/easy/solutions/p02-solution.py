"""Level 02 — Python for ML — Easy P02 Solution"""

import pandas as pd

def solve():
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'age': [25, 30, 35, 28],
        'city': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai']
    })
    print(df.head())
    print(f"Shape: {df.shape}")
    print(f"Dtypes:\n{df.dtypes}")
    return df

if __name__ == "__main__":
    solve()