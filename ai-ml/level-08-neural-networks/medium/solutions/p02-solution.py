"""Level 08 — Neural Networks — Medium P02 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim

def train_linear():
    torch.manual_seed(42)
    X = torch.randn(100, 1)
    y = 3 * X + 2 + torch.randn(100, 1) * 0.1
    model = nn.Linear(1, 1)
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    criterion = nn.MSELoss()
    for epoch in range(100):
        pred = model(X)
        loss = criterion(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    return loss.item(), model.weight.item(), model.bias.item()

if __name__ == "__main__":
    loss, w, b = train_linear()
    print(f"{loss:.4f} {w:.4f} {b:.4f}")
