"""Level 02 — Python for ML — Medium P01 Solution"""

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

def build_pipeline():
    X, y = make_classification(n_samples=200, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler()),
        ('model', LogisticRegression())
    ])
    pipeline.fit(X_train, y_train)
    return pipeline.score(X_test, y_test)

if __name__ == "__main__":
    print(f"Accuracy: {build_pipeline():.4f}")
