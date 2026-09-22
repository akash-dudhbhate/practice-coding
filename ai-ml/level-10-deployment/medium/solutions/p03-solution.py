"""Level 10 — Model Deployment — Medium P03 Solution"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split

def build_registry():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42)
    models = [
        ('v1', 'logistic_regression', LogisticRegression(max_iter=200, random_state=42)),
        ('v2', 'random_forest', RandomForestClassifier(random_state=42)),
        ('v3', 'gradient_boosting', GradientBoostingClassifier(random_state=42)),
    ]
    registry = {}
    for ver, name, model in models:
        model.fit(X_train, y_train)
        registry[ver] = {'model': name, 'accuracy': round(model.score(X_test, y_test), 2)}
    return registry

if __name__ == "__main__":
    print(build_registry())
