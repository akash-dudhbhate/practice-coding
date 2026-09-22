"""Level 02 — Python for ML — Hard P01 Solution"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

def train_clean():
    np.random.seed(42)
    n = 200
    df = pd.DataFrame({
        'age': np.random.randint(18, 70, n).astype(float),
        'income': np.random.randint(20000, 120000, n).astype(float),
        'city': np.random.choice(['Mumbai', 'Delhi', 'Chennai'], n),
    })
    df['target'] = (df['age'] > 40).astype(int)
    df.loc[np.random.choice(n, 20, replace=False), 'age'] = np.nan
    df.loc[np.random.choice(n, 15, replace=False), 'city'] = np.nan

    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    preprocessor = ColumnTransformer([
        ('num', Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), ['age', 'income']),
        ('cat', Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ]), ['city'])
    ])

    model = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=50, random_state=42))
    ])
    model.fit(X_train, y_train)
    return model.score(X_train, y_train), model.score(X_test, y_test)

if __name__ == "__main__":
    tr, te = train_clean()
    print(f"Train: {tr:.4f}  Test: {te:.4f}")
