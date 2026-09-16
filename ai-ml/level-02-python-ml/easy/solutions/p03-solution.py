"""Level 02 — Python for ML — Easy P03 Solution"""

import pandas as pd
import numpy as np

def fill_missing():
    df = pd.DataFrame({
        'age': [25, np.nan, 30, np.nan, 35],
        'city': ['Mumbai', 'Delhi', np.nan, 'Chennai', np.nan],
        'score': [85, 90, np.nan, 78, 92]
    })
    df['age'] = df['age'].fillna(df['age'].median())
    df['score'] = df['score'].fillna(df['score'].median())
    df['city'] = df['city'].fillna(df['city'].mode()[0])
    return df

if __name__ == "__main__":
    print(fill_missing())
