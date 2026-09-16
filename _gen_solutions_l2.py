"""
Generate real working solutions for all AI/ML levels.
Each solution is a complete, runnable implementation.
"""

import os
import glob
import textwrap

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

# Level 02: Python for ML
LEVEL_02_SOLUTIONS = {
    "easy": [
        """import numpy as np

def solve():
    np.random.seed(42)
    arr = np.random.randint(0, 100, (4, 5))
    print(f"Shape: {arr.shape}")
    print(f"Dtype: {arr.dtype}")
    print(f"Ndim: {arr.ndim}")
    print(f"Size: {arr.size}")
    print(f"Column means: {arr.mean(axis=0)}")
    return arr

if __name__ == "__main__":
    solve()""",
        """import pandas as pd

def solve():
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'age': [25, 30, 35, 28],
        'city': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai']
    })
    print(df.head())
    print(f"Shape: {df.shape}")
    print(f"Dtypes:\\n{df.dtypes}")
    return df

if __name__ == "__main__":
    solve()""",
        """import pandas as pd
import numpy as np

def solve():
    df = pd.DataFrame({
        'age': [25, np.nan, 30, np.nan, 35],
        'city': ['Mumbai', 'Delhi', np.nan, 'Chennai', np.nan],
        'score': [85, 90, np.nan, 78, 92]
    })
    df['age'] = df['age'].fillna(df['age'].median())
    df['score'] = df['score'].fillna(df['score'].median())
    df['city'] = df['city'].fillna(df['city'].mode()[0])
    print(df)
    return df

if __name__ == "__main__":
    solve()""",
    ],
    "medium": [
        """import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

def solve():
    X, y = make_classification(n_samples=200, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler()),
        ('model', LogisticRegression())
    ])
    pipeline.fit(X_train, y_train)
    accuracy = pipeline.score(X_test, y_test)
    print(f"Accuracy: {accuracy:.4f}")
    return accuracy

if __name__ == "__main__":
    solve()""",
        """import numpy as np

def solve():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = data[(data < lower) | (data > upper)]
    cleaned = np.clip(data, lower, upper)
    print(f"Outliers: {outliers}")
    print(f"Cleaned: {cleaned}")
    return cleaned, len(outliers)

if __name__ == "__main__":
    solve()""",
        """import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

def solve():
    df = pd.DataFrame({
        'age': [25, 30, 35, 28],
        'city': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai'],
        'signup_date': ['2024-01-15', '2024-02-20', '2024-03-10', '2024-01-25']
    })
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    le = LabelEncoder()
    df['city_encoded'] = le.fit_transform(df['city'])
    scaler = StandardScaler()
    df['age_scaled'] = scaler.fit_transform(df[['age']])
    print(df)
    return df

if __name__ == "__main__":
    solve()""",
    ],
    "hard": [
        """import pandas as pd
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
    solve()""",
        """import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

def solve():
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, random_state=42)
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(5)])
    df['category'] = np.random.choice(['A', 'B', 'C'], 200)
    X = df
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    numeric_features = [f'feature_{i}' for i in range(5)]
    categorical_features = ['category']
    preprocessor = ColumnTransformer([
        ('num', Pipeline([('imputer', SimpleImputer(strategy='mean')), ('scaler', StandardScaler())]), numeric_features),
        ('cat', Pipeline([('imputer', SimpleImputer(strategy='most_frequent')), ('onehot', OneHotEncoder())]), categorical_features)
    ])
    model = Pipeline([('preprocessor', preprocessor), ('classifier', RandomForestClassifier(random_state=42))])
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy:.4f}")
    return accuracy

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def solve():
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=5,
                               weights=[0.95, 0.05], flip_y=0.0, random_state=42)
    # Without stratify
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Without stratify:")
    print(f"  Train: {np.bincount(y_train)}")
    print(f"  Test:  {np.bincount(y_test)}")
    # With stratify
    X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    print("With stratify:")
    print(f"  Train: {np.bincount(y_train_s)}")
    print(f"  Test:  {np.bincount(y_test_s)}")
    # Train and compare
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    model_s = RandomForestClassifier(random_state=42)
    model_s.fit(X_train_s, y_train_s)
    print(f"Without stratify test accuracy: {model.score(X_test, y_test):.4f}")
    print(f"With stratify test accuracy: {model_s.score(X_test_s, y_test_s):.4f}")
    return model.score(X_test, y_test), model_s.score(X_test_s, y_test_s)

if __name__ == "__main__":
    solve()""",
    ],
}

# Write solutions for level-02
level_path = os.path.join(AIML_DIR, "level-02-python-ml")
for difficulty, solutions in LEVEL_02_SOLUTIONS.items():
    for i, solution_code in enumerate(solutions, 1):
        filepath = os.path.join(level_path, difficulty, "solutions", f"p{i:02d}-solution.py")
        with open(filepath, "w") as f:
            f.write(f'"""Level 02 — Python for ML — {difficulty.capitalize()} P{i:02d} Solution"""\n\n')
            f.write(solution_code)
        print(f"Wrote {filepath}")
