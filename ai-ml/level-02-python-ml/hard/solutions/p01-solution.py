"""Level 02 — Python for ML — Hard P01 Solution"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

def solve():
    df = pd.DataFrame({
        'age': [25, np.nan, 30, 35, np.nan, 28],
        'income': [50000, 60000, np.nan, 70000, 55000, 62000],
        'city': ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai'],
        'target': [0, 1, 0, 1, 0, 1]
    })
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    numeric_features = ['age', 'income']
    categorical_features = ['city']
    preprocessor = ColumnTransformer([
        ('num', Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), numeric_features),
        ('cat', Pipeline([('imputer', SimpleImputer(strategy='most_frequent')), ('onehot', OneHotEncoder())]), categorical_features)
    ])
    model = Pipeline([('preprocessor', preprocessor), ('classifier', RandomForestClassifier(random_state=42))])
    model.fit(X_train, y_train)
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    print(f"Train accuracy: {train_acc:.4f}")
    print(f"Test accuracy: {test_acc:.4f}")
    return train_acc, test_acc

if __name__ == "__main__":
    solve()