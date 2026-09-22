"""Level 10 — Model Deployment — Hard P03 Solution"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def ab_test():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42)
    model_a = LogisticRegression(max_iter=200, random_state=42).fit(X_train, y_train)
    model_b = RandomForestClassifier(random_state=42).fit(X_train, y_train)

    np.random.seed(42)
    test_samples = X_test[np.random.choice(len(X_test), 100, replace=True)]
    results = {'model_a': {'count': 0, 'correct': 0}, 'model_b': {'count': 0, 'correct': 0}}
    for sample in test_samples:
        route = hash(tuple(sample)) % 2
        if route == 0:
            pred = model_a.predict([sample])[0]
            results['model_a']['count'] += 1
        else:
            pred = model_b.predict([sample])[0]
            results['model_b']['count'] += 1
    return results

if __name__ == "__main__":
    print(ab_test())
