"""Level 02 — Python for ML — Easy P02 Solution"""

import pandas as pd

def load_data():
    return pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'age': [25, 30, 35, 28],
        'city': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai']
    })

if __name__ == "__main__":
    df = load_data()
    print(df.head())
    print(df.shape)
    print(df.dtypes)
