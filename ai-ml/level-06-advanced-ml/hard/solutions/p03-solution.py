"""Level 06 — Advanced ML — Hard P03 Solution"""

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, f1_score

def compare_balanced():
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=5,
                               weights=[0.95, 0.05], flip_y=0.0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    default = LogisticRegression(random_state=42, max_iter=1000).fit(X_train, y_train)
    balanced = LogisticRegression(random_state=42, max_iter=1000,
                                  class_weight='balanced').fit(X_train, y_train)

    r_default = recall_score(y_test, default.predict(X_test))
    r_balanced = recall_score(y_test, balanced.predict(X_test))
    f1_default = f1_score(y_test, default.predict(X_test))
    f1_balanced = f1_score(y_test, balanced.predict(X_test))
    return r_default, r_balanced, f1_default, f1_balanced

if __name__ == "__main__":
    rd, rb, fd, fb = compare_balanced()
    print(f"Default  — recall: {rd:.4f}, F1: {fd:.4f}")
    print(f"Balanced — recall: {rb:.4f}, F1: {fb:.4f}")
