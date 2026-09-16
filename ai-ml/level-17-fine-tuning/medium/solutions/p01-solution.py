"""Level 17 — Fine-Tuning / LoRA — Medium P01 Solution"""

import torch
import torch.nn as nn


def feature_extract_finetune(X_tr, y_tr, X_te, y_te):
    """Freeze the backbone, train only the head, return test accuracy."""
    torch.manual_seed(42)
    model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))

    # Freeze backbone — model[0] becomes a fixed feature extractor
    for p in model[0].parameters():
        p.requires_grad_(False)

    trainable = [p for p in model.parameters() if p.requires_grad]
    opt = torch.optim.Adam(trainable, lr=0.01)
    loss_fn = nn.CrossEntropyLoss()

    model.train()
    for _ in range(100):
        opt.zero_grad()
        loss = loss_fn(model(X_tr), y_tr)
        loss.backward()
        opt.step()

    model.eval()
    with torch.no_grad():
        preds = model(X_te).argmax(dim=1)
        return (preds == y_te).float().mean().item()


if __name__ == "__main__":
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                               n_informative=6, n_clusters_per_class=1,
                               class_sep=1.5, random_state=42)
    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.long)
    acc = feature_extract_finetune(X[:150], y[:150], X[150:], y[150:])
    print(f"Feature-extraction test acc: {acc:.3f}")
