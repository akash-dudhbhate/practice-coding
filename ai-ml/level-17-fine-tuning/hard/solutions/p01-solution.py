"""Level 17 — Fine-Tuning / LoRA — Hard P01 Solution"""

import torch
import torch.nn as nn


class LoRALinear(nn.Module):
    """Wrap an existing Linear with a frozen base + trainable A/B adapter."""

    def __init__(self, linear, rank):
        super().__init__()
        self.base = linear
        for p in self.base.parameters():
            p.requires_grad_(False)
        self.A = nn.Parameter(torch.randn(rank, linear.in_features) * 0.01)
        self.B = nn.Parameter(torch.zeros(linear.out_features, rank))

    def forward(self, x):
        return self.base(x) + (x @ self.A.T) @ self.B.T


def lora_finetune(X_tr, y_tr, X_te, y_te, rank=4):
    """LoRA on the hidden layer + trainable head; return test accuracy."""
    torch.manual_seed(42)
    model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))

    # Wrap the hidden (feature) layer — keeps its pretrained weights
    model[0] = LoRALinear(model[0], rank)

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
        return (model(X_te).argmax(dim=1) == y_te).float().mean().item()


if __name__ == "__main__":
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                               n_informative=6, n_clusters_per_class=1,
                               class_sep=1.5, random_state=42)
    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.long)
    acc = lora_finetune(X[:150], y[:150], X[150:], y[150:], rank=4)
    print(f"LoRA fine-tune test acc: {acc:.3f}")
