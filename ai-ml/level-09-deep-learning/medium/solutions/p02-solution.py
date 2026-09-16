"""Level 09 Deep Learning — Medium P02 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim

def solve():
    torch.manual_seed(42)
    X = torch.randn(100, 10)
    y = torch.randint(0, 2, (100,))
    # Without batch norm
    model_no_bn = nn.Sequential(
        nn.Linear(10, 32), nn.ReLU(),
        nn.Linear(32, 16), nn.ReLU(),
        nn.Linear(16, 2)
    )
    # With batch norm
    model_bn = nn.Sequential(
        nn.Linear(10, 32), nn.BatchNorm1d(32), nn.ReLU(),
        nn.Linear(32, 16), nn.BatchNorm1d(16), nn.ReLU(),
        nn.Linear(16, 2)
    )
    criterion = nn.CrossEntropyLoss()
    for name, model in [("No BN", model_no_bn), ("With BN", model_bn)]:
        optimizer = optim.Adam(model.parameters(), lr=0.001)
        for epoch in range(20):
            optimizer.zero_grad()
            outputs = model(X)
            loss = criterion(outputs, y)
            loss.backward()
            optimizer.step()
        print(f"{name}: final loss={loss.item():.4f}")
    return model_bn

if __name__ == "__main__":
    solve()