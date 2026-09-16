"""Level 06 — Advanced ML — Easy P03 Solution"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

def scale_features():
    df = pd.DataFrame({
        'age': [25, 30, 35, 40, 45],
        'income': [30000, 50000, 70000, 90000, 110000]
    })
    scaled = StandardScaler().fit_transform(df)
    return pd.DataFrame(scaled, columns=df.columns)

if __name__ == "__main__":
    df = scale_features()
    print(df)
    print(f"age mean: {df['age'].mean():.6f}")
    print(f"income mean: {df['income'].mean():.6f}")
