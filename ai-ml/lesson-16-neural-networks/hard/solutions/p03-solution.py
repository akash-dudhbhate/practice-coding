"""
NN hyperparameter study
=======================
Vary (a) learning rate [0.001, 0.01, 0.1], (b) batch size [16, 32, 64],
(c) architecture [(32,), (64,32), (128,64,32)].
Record loss and accuracy. Display results in a table.
"""

import numpy as np
import time
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def evaluate(X_train, y_train, X_test, y_test, lr, batch_size, architecture):
    """Train MLP with given hyperparameters, return accuracy and training time."""
    mlp = MLPClassifier(
        hidden_layer_sizes=architecture,
        learning_rate_init=lr,
        batch_size=batch_size,
        max_iter=300,
        random_state=42,
    )
    start = time.time()
    mlp.fit(X_train, y_train)
    train_time = time.time() - start

    train_acc = accuracy_score(y_train, mlp.predict(X_train))
    test_acc = accuracy_score(y_test, mlp.predict(X_test))
    final_loss = mlp.loss_
    return train_acc, test_acc, final_loss, train_time


if __name__ == "__main__":
    # Synthetic classification dataset
    X, y = make_classification(
        n_samples=1000, n_features=20, n_informative=10,
        n_classes=2, random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    learning_rates = [0.001, 0.01, 0.1]
    batch_sizes = [16, 32, 64]
    architectures = [(32,), (64, 32), (128, 64, 32)]

    # --- (a) Learning rate study ---
    print("=" * 70)
    print("(a) Learning Rate Study (batch_size=32, arch=(64,32))")
    print("=" * 70)
    print(f"{'LR':<10} {'Train Acc':<12} {'Test Acc':<12} {'Loss':<12} {'Time(s)':<10}")
    print("-" * 56)
    for lr in learning_rates:
        ta, te, loss, t = evaluate(X_train_s, y_train, X_test_s, y_test,
                                   lr, 32, (64, 32))
        print(f"{lr:<10} {ta:<12.4f} {te:<12.4f} {loss:<12.4f} {t:<10.4f}")

    # --- (b) Batch size study ---
    print(f"\n{'=' * 70}")
    print("(b) Batch Size Study (lr=0.01, arch=(64,32))")
    print("=" * 70)
    print(f"{'Batch':<10} {'Train Acc':<12} {'Test Acc':<12} {'Loss':<12} {'Time(s)':<10}")
    print("-" * 56)
    for bs in batch_sizes:
        ta, te, loss, t = evaluate(X_train_s, y_train, X_test_s, y_test,
                                   0.01, bs, (64, 32))
        print(f"{bs:<10} {ta:<12.4f} {te:<12.4f} {loss:<12.4f} {t:<10.4f}")

    # --- (c) Architecture study ---
    print(f"\n{'=' * 70}")
    print("(c) Architecture Study (lr=0.01, batch_size=32)")
    print("=" * 70)
    print(f"{'Arch':<20} {'Train Acc':<12} {'Test Acc':<12} {'Loss':<12} {'Time(s)':<10}")
    print("-" * 66)
    for arch in architectures:
        ta, te, loss, t = evaluate(X_train_s, y_train, X_test_s, y_test,
                                   0.01, 32, arch)
        print(f"{str(arch):<20} {ta:<12.4f} {te:<12.4f} {loss:<12.4f} {t:<10.4f}")

    print("\n--- Key Takeaways ---")
    print("- Too high LR (0.1) may fail to converge or oscillate.")
    print("- Smaller batches = more updates per epoch but noisier gradients.")
    print("- Deeper networks have more capacity but risk overfitting and slower training.")
