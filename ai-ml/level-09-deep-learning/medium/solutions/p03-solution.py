"""Level 09 Deep Learning — Medium P03 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim

def solve():
    torch.manual_seed(42)
    X = torch.randn(200, 10)
    y = torch.randint(0, 2, (200,))
    X_train, X_test = X[:160], X[160:]
    y_train, y_test = y[:160], y[160:]
    # Without dropout
    model_no_drop = nn.Sequential(
        nn.Linear(10, 64), nn.ReLU(),
        nn.Linear(64, 32), nn.ReLU(),
        nn.Linear(32, 2)
    )
    # With dropout
    model_drop = nn.Sequential(
        nn.Linear(10, 64), nn.ReLU(), nn.Dropout(0.3),
        nn.Linear(64, 32), nn.ReLU(), nn.Dropout(0.3),
        nn.Linear(32, 2)
    )
    criterion = nn.CrossEntropyLoss()
    for name, model in [("No Dropout", model_no_drop), ("With Dropout", model_drop)]:
        optimizer = optim.Adam(model.parameters(), lr=0.001)
        for epoch in range(50):
            optimizer.zero_grad()
            outputs = model(X_train)
            loss = criterion(outputs, y_train)
            loss.backward()
            optimizer.step()
        model.eval()
        with torch.no_grad():
            test_acc = (model(X_test).argmax(1) == y_test).float().mean()
        print(f"{name}: test acc={test_acc:.4f}")
    return model_drop

if __name__ == "__main__":
    solve()