"""Level 08 Neural Networks — Hard P02 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim

def solve():
    # Custom loss: weighted MSE
    class WeightedMSELoss(nn.Module):
        def __init__(self, weights):
            super().__init__()
            self.weights = weights
        def forward(self, pred, target):
            return torch.mean(self.weights * (pred - target) ** 2)
    torch.manual_seed(42)
    model = nn.Linear(2, 1)
    weights = torch.tensor([1.0, 2.0])
    criterion = WeightedMSELoss(weights)
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    X = torch.randn(50, 2)
    y = torch.randn(50, 1)
    for epoch in range(100):
        optimizer.zero_grad()
        output = model(X)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
    print(f"Final loss: {loss.item():.4f}")
    return model

if __name__ == "__main__":
    solve()