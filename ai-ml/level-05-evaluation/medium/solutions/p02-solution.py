"""Level 05 Evaluation — Medium P02 Solution"""

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

def solve():
    X, y = make_classification(n_samples=200, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 10],
        'min_samples_split': [2, 5]
    }
    rf = RandomForestClassifier(random_state=42)
    grid = GridSearchCV(rf, param_grid, cv=3, scoring='accuracy')
    grid.fit(X_train, y_train)
    print(f"Best params: {grid.best_params_}")
    print(f"Best score: {grid.best_score_:.4f}")
    print(f"Test score: {grid.score(X_test, y_test):.4f}")
    return grid.best_params_, grid.best_score_

if __name__ == "__main__":
    solve()