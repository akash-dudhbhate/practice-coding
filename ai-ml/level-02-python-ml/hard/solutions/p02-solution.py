"""Level 02 — Python for ML — Hard P02 Solution"""

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

def build():
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, random_state=42)
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(5)])
    np.random.seed(42)
    df['category'] = np.random.choice(['A', 'B', 'C'], 200)
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)

    preprocessor = ColumnTransformer([
        ('num', Pipeline([
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ]), [f'feature_{i}' for i in range(5)]),
        ('cat', Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder())
        ]), ['category'])
    ])

    model = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)

if __name__ == "__main__":
    print(f"Accuracy: {build():.4f}")
