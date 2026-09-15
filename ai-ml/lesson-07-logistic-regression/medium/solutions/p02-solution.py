"""
Plot Decision Boundary with Meshgrid and Contourf
=================================================
Train logistic regression on 2D synthetic data and visualize
the decision boundary using a meshgrid and contourf.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification


if __name__ == "__main__":
    # Generate 2D synthetic data for visualization
    X, y = make_classification(
        n_samples=300, n_features=2, n_informative=2, n_redundant=0,
        n_clusters_per_class=1, random_state=42
    )

    # Train logistic regression
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X, y)

    # Create meshgrid
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    # Predict on meshgrid points
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.RdYlBu)
    plt.contour(xx, yy, Z, colors="black", linewidths=0.5, alpha=0.5)

    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu,
                          edgecolors="black", s=40)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Logistic Regression Decision Boundary")
    plt.colorbar(scatter, label="Class")
    plt.tight_layout()
    plt.savefig("decision_boundary.png", dpi=150)
    plt.show()
    print("Decision boundary plot saved to decision_boundary.png")
