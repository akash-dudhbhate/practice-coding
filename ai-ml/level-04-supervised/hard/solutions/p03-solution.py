"""Level 04 Supervised — Hard P03 Solution"""

from sklearn.datasets import make_classification
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def solve():
    X, y = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestClassifier(random_state=42)
    rfe = RFE(estimator=rf, n_features_to_select=5)
    rfe.fit(X_train, y_train)
    selected = rfe.support_
    X_train_selected = X_train[:, selected]
    X_test_selected = X_test[:, selected]
    rf.fit(X_train_selected, y_train)
    accuracy = rf.score(X_test_selected, y_test)
    print(f"Selected features: {list(np.where(selected)[0])}")
    print(f"Accuracy with selected features: {accuracy:.4f}")
    return selected, accuracy

if __name__ == "__main__":
    solve()