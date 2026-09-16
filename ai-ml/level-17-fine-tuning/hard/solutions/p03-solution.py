"""Level 17 — Fine-Tuning / LoRA — Hard P03 Solution"""

import copy

import torch
import torch.nn as nn


class LoRALinear(nn.Module):
    """Frozen base Linear + trainable low-rank adapter B@A."""

    def __init__(self, linear, rank):
        super().__init__()
        self.base = linear
        for p in self.base.parameters():
            p.requires_grad_(False)
        self.A = nn.Parameter(torch.randn(rank, linear.in_features) * 0.01)
        self.B = nn.Parameter(torch.zeros(linear.out_features, rank))

    def forward(self, x):
        return self.base(x) + (x @ self.A.T) @ self.B.T


def _train(model, X, y, epochs, lr=0.01):
    params = [p for p in model.parameters() if p.requires_grad]
    opt = torch.optim.Adam(params, lr=lr)
    loss_fn = nn.CrossEntropyLoss()
    model.train()
    for _ in range(epochs):
        opt.zero_grad()
        loss = loss_fn(model(X), y)
        loss.backward()
        opt.step()


def _acc(model, X, y):
    model.eval()
    with torch.no_grad():
        return (model(X).argmax(dim=1) == y).float().mean().item()


def catastrophic_forgetting(orig_data, new_data):
    """Full FT forgets the original task; LoRA's base weights survive."""
    X, y = orig_data
    X2, y2 = new_data
    X_tr, y_tr, X_te, y_te = X[:150], y[:150], X[150:], y[150:]

    # 1. Pretrain on the original task
    torch.manual_seed(42)
    base = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))
    _train(base, X_tr, y_tr, epochs=100)
    orig_before = _acc(base, X_te, y_te)

    # 2. Full fine-tune on the new task — all weights overwritten
    m_full = copy.deepcopy(base)
    _train(m_full, X2, y2, epochs=100)
    after_full = _acc(m_full, X_te, y_te)

    # 3. LoRA fine-tune — only A/B adapters train, base stays frozen
    m_lora = copy.deepcopy(base)
    m_lora[0] = LoRALinear(m_lora[0], 4)
    m_lora[2] = LoRALinear(m_lora[2], 4)
    for p in m_lora.parameters():
        p.requires_grad_(False)
    for layer in (m_lora[0], m_lora[2]):
        layer.A.requires_grad_(True)
        layer.B.requires_grad_(True)
    _train(m_lora, X2, y2, epochs=50)
    after_lora = _acc(m_lora, X_te, y_te)

    # 4. Strip the adapters — base weights were never touched
    recovered = nn.Sequential(m_lora[0].base, nn.ReLU(), m_lora[2].base)
    lora_recovered = _acc(recovered, X_te, y_te)

    return {
        'orig_before': orig_before,
        'after_full': after_full,
        'after_lora': after_lora,
        'lora_recovered': lora_recovered,
    }


if __name__ == "__main__":
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                               n_informative=6, n_clusters_per_class=1,
                               class_sep=1.5, random_state=42)
    X2, y2 = make_classification(n_samples=150, n_features=8, n_classes=3,
                                 n_informative=6, n_clusters_per_class=1,
                                 class_sep=1.5, random_state=7)
    orig = (torch.tensor(X, dtype=torch.float32),
            torch.tensor(y, dtype=torch.long))
    new = (torch.tensor(X2, dtype=torch.float32),
           torch.tensor(y2, dtype=torch.long))
    print(catastrophic_forgetting(orig, new))
