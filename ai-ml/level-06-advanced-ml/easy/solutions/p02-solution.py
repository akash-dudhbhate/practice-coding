"""Level 06 Advanced Ml — Easy P02 Solution"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def solve():
    df = pd.DataFrame({
        'color': ['red', 'blue', 'green', 'red', 'blue'],
        'size': ['S', 'M', 'L', 'M', 'S']
    })
    # Label encoding
    le = LabelEncoder()
    df['color_encoded'] = le.fit_transform(df['color'])
    # One-hot encoding
    df_onehot = pd.get_dummies(df, columns=['size'])
    print("Label encoded:")
    print(df[['color', 'color_encoded']])
    print("
One-hot encoded:")
    print(df_onehot)
    return df, df_onehot

if __name__ == "__main__":
    solve()