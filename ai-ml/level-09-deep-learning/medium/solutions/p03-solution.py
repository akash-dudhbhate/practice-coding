"""Level 09 — Deep Learning — Medium P03 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def compare_dropout():
    torch.manual_seed(42)
    X, y = make_classification(n_samples=200, n_features=20, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_tr = torch.tensor(X_train, dtype=torch.float32)
    X_te = torch.tensor(X_test, dtype=torch.float32)
    y_tr = torch.tensor(y_train, dtype=torch.long)
    y_te = torch.tensor(y_test, dtype=torch.long)

    def _train(model, epochs=200):
        criterion = nn.CrossEntropyLoss()
        opt = optim.Adam(model.parameters(), lr=0.01)
        for _ in range(epochs):
            model.train()
            opt.zero_grad()
            loss = criterion(model(X_tr), y_tr)
            loss.backward()
            opt.step()
        model.eval()
        with torch.no_grad():
            preds = model(X_te).argmax(dim=1)
            return (preds == y_te).float().mean().item()

    no_drop = nn.Sequential(nn.Linear(20, 64), nn.ReLU(), nn.Linear(64, 2))
    with_drop = nn.Sequential(nn.Linear(20, 64), nn.ReLU(), nn.Dropout(0.5), nn.Linear(64, 2))
    return _train(no_drop), _train(with_drop)

if __name__ == "__main__":
    a, b = compare_dropout()
    print(f"No dropout: {a:.4f}  With dropout: {b:.4f}")
