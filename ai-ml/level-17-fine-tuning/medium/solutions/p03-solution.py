"""Level 17 — Fine-Tuning / LoRA — Medium P03 Solution"""

import torch
import torch.nn as nn


def _build():
    torch.manual_seed(42)
    return nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))


def _train(model, X_tr, y_tr, epochs=100):
    trainable = [p for p in model.parameters() if p.requires_grad]
    opt = torch.optim.Adam(trainable, lr=0.01)
    loss_fn = nn.CrossEntropyLoss()
    model.train()
    for _ in range(epochs):
        opt.zero_grad()
        loss = loss_fn(model(X_tr), y_tr)
        loss.backward()
        opt.step()


def _acc(model, X, y):
    model.eval()
    with torch.no_grad():
        return (model(X).argmax(dim=1) == y).float().mean().item()


def full_vs_head(X_tr, y_tr, X_te, y_te):
    """Return (full_finetune_acc, head_only_acc)."""
    # Full fine-tune — all 387 params train
    m_full = _build()
    _train(m_full, X_tr, y_tr)
    full_acc = _acc(m_full, X_te, y_te)

    # Head-only — backbone frozen, only 99 head params train
    m_head = _build()
    for p in m_head[0].parameters():
        p.requires_grad_(False)
    _train(m_head, X_tr, y_tr)
    head_acc = _acc(m_head, X_te, y_te)

    return full_acc, head_acc


if __name__ == "__main__":
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                               n_informative=6, n_clusters_per_class=1,
                               class_sep=1.5, random_state=42)
    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.long)
    fa, ha = full_vs_head(X[:150], y[:150], X[150:], y[150:])
    print(f"full={fa:.3f} head={ha:.3f}")
