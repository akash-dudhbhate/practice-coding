"""Level 05 — Model Evaluation — Medium P02 Solution"""

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

def grid_search():
    X, y = make_classification(n_samples=200, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 10],
        'min_samples_split': [2, 5]
    }
    grid = GridSearchCV(RandomForestClassifier(random_state=42),
                        param_grid, cv=3, scoring='accuracy')
    grid.fit(X_train, y_train)
    return grid.best_params_, grid.best_score_, grid.score(X_test, y_test)

if __name__ == "__main__":
    params, score, test = grid_search()
    print(f"Best params: {params}")
    print(f"CV score: {score:.4f}")
    print(f"Test score: {test:.4f}")
