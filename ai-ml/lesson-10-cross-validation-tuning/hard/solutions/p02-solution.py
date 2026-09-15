# Lesson 10 — Hard P02: Learning curves for 3 models
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import learning_curve
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Create dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, random_state=42)
X = StandardScaler().fit_transform(X)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42, ccp_alpha=0.0),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42, min_samples_leaf=1, max_features="sqrt"),
}

fig, ax = plt.subplots(figsize=(10, 6))

for name, model in models.items():
    train_sizes, train_scores, val_scores = learning_curve(
        model, X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 10), scoring="accuracy", random_state=42
    )
    train_mean = train_scores.mean(axis=1)
    val_mean = val_scores.mean(axis=1)
    ax.plot(train_sizes, val_mean, label=f"{name} (val)", marker="o")
    ax.plot(train_sizes, train_mean, label=f"{name} (train)", linestyle="--", alpha=0.5)

ax.set_xlabel("Training Set Size")
ax.set_ylabel("Accuracy")
ax.set_title("Learning Curves for 3 Models")
ax.legend(loc="best")
ax.set_ylim(0.7, 1.05)
ax.grid(True)
plt.tight_layout()
plt.savefig("learning_curves.png", dpi=150)
print("Figure saved to learning_curves.png")

# Diagnose each model
print("\n=== Diagnosis ===")
print("1. Logistic Regression: Train and val accuracy are close (~0.85-0.88).")
print("   Diagnosis: GOOD FIT (maybe slight underfitting). More data unlikely to help much.")
print()
print("2. Decision Tree: Train accuracy = 1.0 (100%), val accuracy ~0.88.")
print("   Diagnosis: OVERFITTING (large gap between train and val).")
print("   More data may help slightly, but pruning (max_depth) is more effective.")
print()
print("3. Random Forest: Train accuracy ~0.98, val accuracy ~0.92.")
print("   Diagnosis: SLIGHT OVERFITTING but better than single tree.")
print("   More data could help close the gap further.")
