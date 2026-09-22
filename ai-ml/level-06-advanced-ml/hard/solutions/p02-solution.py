"""Level 06 — Advanced ML — Hard P02 Solution"""

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def engineer_and_train():
    np.random.seed(42)
    n = 200
    df = pd.DataFrame({
        'age': np.random.randint(18, 70, n),
        'income': np.random.randint(20000, 120000, n),
        'day_of_week': np.random.randint(0, 7, n),
    })
    df['target'] = (df['income'] / df['age'] > 1500).astype(int)
    df['income_per_age'] = df['income'] / df['age']
    df['age_sq'] = df['age'] ** 2
    df['income_log'] = np.log1p(df['income'])
    df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)

    feature_cols = ['age', 'income', 'day_of_week', 'income_per_age',
                    'age_sq', 'income_log', 'is_weekend']
    X = df[feature_cols]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(random_state=42, max_iter=1000))
    ])
    pipe.fit(X_train, y_train)
    return pipe.score(X_test, y_test), feature_cols

if __name__ == "__main__":
    acc, feats = engineer_and_train()
    print(f"{acc:.4f}")
    print(feats)
