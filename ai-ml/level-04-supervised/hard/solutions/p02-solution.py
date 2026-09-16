"""Level 04 — Supervised Learning — Hard P02 Solution"""

from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split

def compare_ensembles():
    X, y = make_classification(n_samples=500, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    models = {
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        results[name] = (model.score(X_train, y_train), model.score(X_test, y_test))
    return results

if __name__ == "__main__":
    results = compare_ensembles()
    print(f"{'Model':<20} {'Train':<8} {'Test':<8}")
    for name, (tr, te) in results.items():
        print(f"{name:<20} {tr:<8.4f} {te:<8.4f}")
