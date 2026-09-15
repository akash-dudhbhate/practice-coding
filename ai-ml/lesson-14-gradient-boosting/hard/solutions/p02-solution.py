"""
Gradient Boosting from Scratch
===============================
Implement gradient boosting for regression from scratch:
  - Sequential tree training on residuals
  - Prediction = sum of trees * learning_rate
  - Use sklearn DecisionTreeRegressor as the weak learner
  - Plot the loss curve over iterations
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)


class GradientBoostingScratch:
    """Gradient boosting for regression, built from scratch."""

    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []
        self.initial_pred = None
        self.train_losses = []

    def fit(self, X, y):
        # Initialize with the mean (minimizes squared error)
        self.initial_pred = np.mean(y)
        current_pred = np.full(len(y), self.initial_pred)

        for _ in range(self.n_estimators):
            # Compute residuals (negative gradient of MSE)
            residuals = y - current_pred

            # Fit a weak learner (shallow tree) to the residuals
            tree = DecisionTreeRegressor(max_depth=self.max_depth, random_state=42)
            tree.fit(X, residuals)
            self.trees.append(tree)

            # Update predictions
            current_pred += self.learning_rate * tree.predict(X)

            # Track training loss
            loss = mean_squared_error(y, current_pred)
            self.train_losses.append(loss)

    def predict(self, X):
        pred = np.full(X.shape[0], self.initial_pred)
        for tree in self.trees:
            pred += self.learning_rate * tree.predict(X)
        return pred


if __name__ == "__main__":
    X, y = make_regression(n_samples=500, n_features=10, n_informative=5, noise=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train from-scratch model
    gb = GradientBoostingScratch(n_estimators=100, learning_rate=0.1, max_depth=3)
    gb.fit(X_train, y_train)

    train_mse = mean_squared_error(y_train, gb.predict(X_train))
    test_mse = mean_squared_error(y_test, gb.predict(X_test))

    print("=== Gradient Boosting from Scratch ===")
    print(f"Train MSE: {train_mse:.4f}")
    print(f"Test MSE:  {test_mse:.4f}")
    print(f"Number of trees: {len(gb.trees)}")
    print(f"Initial prediction (mean): {gb.initial_pred:.4f}")

    # Compare with sklearn
    from sklearn.ensemble import GradientBoostingRegressor
    sk_gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    sk_gb.fit(X_train, y_train)
    sk_test_mse = mean_squared_error(y_test, sk_gb.predict(X_test))

    print(f"\nsklearn GradientBoosting test MSE: {sk_test_mse:.4f}")
    print(f"From-scratch test MSE:            {test_mse:.4f}")

    # Plot loss curve
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(gb.train_losses) + 1), gb.train_losses, "b-", label="Training MSE")
    plt.xlabel("Iteration (number of trees)")
    plt.ylabel("Training MSE")
    plt.title("Gradient Boosting — Training Loss Curve")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("gb_loss_curve.png", dpi=150)
    print("\nLoss curve saved to gb_loss_curve.png")
    print()
    print("Key takeaway: Each tree corrects the residual errors of the")
    print("ensemble so far. The loss decreases steadily as more trees are added.")
