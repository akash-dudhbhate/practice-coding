"""Level 05 — Model Evaluation — Easy P03 Solution"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

def cross_validate():
    iris = load_iris()
    scores = cross_val_score(RandomForestClassifier(random_state=42),
                             iris.data, iris.target, cv=5)
    return scores.mean(), scores.std()

if __name__ == "__main__":
    m, s = cross_validate()
    print(f"{m:.4f} ± {s:.4f}")
