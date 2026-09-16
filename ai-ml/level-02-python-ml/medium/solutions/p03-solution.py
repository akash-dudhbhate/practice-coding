"""Level 02 — Python for ML — Medium P03 Solution"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def process():
    df = pd.DataFrame({
        'age': [25, 30, 35, 28],
        'city': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai'],
        'signup_date': ['2024-01-15', '2024-02-20', '2024-03-10', '2024-01-25']
    })
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['city_encoded'] = LabelEncoder().fit_transform(df['city'])
    df['age_scaled'] = StandardScaler().fit_transform(df[['age']])
    return df

if __name__ == "__main__":
    print(process())
