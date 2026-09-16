"""Level 08 — Neural Networks — Hard P02 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def train():
    torch.manual_seed(42)
    X, y = make_classification(n_samples=500, n_features=10, n_informative=10,
                               n_redundant=0, n_clusters_per_class=1, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train = torch.tensor(X_train, dtype=torch.float32)
    X_val = torch.tensor(X_val, dtype=torch.float32)
    y_train = torch.tensor(y_train, dtype=torch.long)
    y_val = torch.tensor(y_val, dtype=torch.long)

    ds = TensorDataset(X_train, y_train)
    loader = DataLoader(ds, batch_size=32, shuffle=True)

    model = nn.Sequential(nn.Linear(10, 64), nn.ReLU(), nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 2))
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.005)

    train_losses = []
    val_accs = []
    for epoch in range(100):
        model.train()
        epoch_loss = 0
        for xb, yb in loader:
            optimizer.zero_grad()
            out = model(xb)
            loss = criterion(out, yb)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        train_losses.append(epoch_loss / len(loader))
        model.eval()
        with torch.no_grad():
            preds = model(X_val).argmax(dim=1)
            acc = (preds == y_val).float().mean().item()
            val_accs.append(acc)
    return train_losses, val_accs

if __name__ == "__main__":
    losses, accs = train()
    print(f"{losses[0]:.4f} -> {losses[-1]:.4f}")
    print(f"{accs[-1]:.4f}")
