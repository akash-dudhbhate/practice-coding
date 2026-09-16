"""Level 08 Neural Networks — Medium P02 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

def solve():
    np.random.seed(42)
    torch.manual_seed(42)
    X = torch.randn(100, 2)
    y = (X[:, 0] + X[:, 1] > 0).float()
    model = nn.Sequential(
        nn.Linear(2, 8),
        nn.ReLU(),
        nn.Linear(8, 1),
        nn.Sigmoid()
    )
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    for epoch in range(100):
        optimizer.zero_grad()
        outputs = model(X).squeeze()
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        preds = (model(X).squeeze() > 0.5).float()
        accuracy = (preds == y).float().mean()
    print(f"Accuracy: {accuracy:.4f}")
    return model

if __name__ == "__main__":
    solve()