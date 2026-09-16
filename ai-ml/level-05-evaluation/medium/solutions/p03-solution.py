"""Level 05 — Model Evaluation — Medium P03 Solution"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve

def plot_learning_curve():
    X, y = make_classification(n_samples=500, n_features=10, random_state=42)
    train_sizes, train_scores, val_scores = learning_curve(
        LogisticRegression(random_state=42, max_iter=1000), X, y, cv=5,
        train_sizes=np.linspace(0.1, 1.0, 10))
    train_mean = np.mean(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_mean, 'o-', label='Training score')
    plt.plot(train_sizes, val_mean, 'o-', label='Validation score')
    plt.xlabel('Training Size')
    plt.ylabel('Score')
    plt.title('Learning Curve')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('learning_curve.png', dpi=150, bbox_inches='tight')
    plt.close()
    return train_sizes, train_mean, val_mean

if __name__ == "__main__":
    ts, tr, va = plot_learning_curve()
    print(f"Sizes: {ts[:3]}...")
    print(f"Final train: {tr[-1]:.4f}, val: {va[-1]:.4f}")
