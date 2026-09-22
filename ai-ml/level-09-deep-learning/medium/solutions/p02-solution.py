"""Level 09 — Deep Learning — Medium P02 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification

def compare_bn():
    torch.manual_seed(42)
    X, y = make_classification(n_samples=500, n_features=10, random_state=42)
    X_t = torch.tensor(X, dtype=torch.float32)
    y_t = torch.tensor(y, dtype=torch.long)

    def _train(model, epochs=100):
        criterion = nn.CrossEntropyLoss()
        opt = optim.Adam(model.parameters(), lr=0.01)
        for _ in range(epochs):
            opt.zero_grad()
            loss = criterion(model(X_t), y_t)
            loss.backward()
            opt.step()
        return loss.item()

    no_bn = nn.Sequential(nn.Linear(10, 64), nn.ReLU(), nn.Linear(64, 2))
    with_bn = nn.Sequential(nn.Linear(10, 64), nn.BatchNorm1d(64), nn.ReLU(), nn.Linear(64, 2))
    return _train(no_bn), _train(with_bn)

if __name__ == "__main__":
    a, b = compare_bn()
    print(f"No BN: {a:.4f}  With BN: {b:.4f}")
