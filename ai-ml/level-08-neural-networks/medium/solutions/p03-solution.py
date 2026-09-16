"""Level 08 Neural Networks — Medium P03 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

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
    losses = []
    for epoch in range(100):
        optimizer.zero_grad()
        outputs = model(X).squeeze()
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
        if epoch % 20 == 0:
            print(f"Epoch {epoch}: loss={loss.item():.4f}")
    plt.plot(losses)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss')
    plt.savefig('training_loss.png', dpi=150, bbox_inches='tight')
    plt.show()
    return losses

if __name__ == "__main__":
    solve()