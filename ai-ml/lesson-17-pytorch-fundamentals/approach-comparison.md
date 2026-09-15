# Lesson 17 — Approach Comparison

## Problem: Build Model

### Approach 1: nn.Sequential
```python
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

### Approach 2: Custom class
```python
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)
```

**Winner:** Approach 1 for simple models. Approach 2 for complex architectures.

---

## Problem: Training

### Approach 1: Manual loop
```python
for epoch in range(10):
    for x, y in loader:
        optimizer.zero_grad()
        loss = criterion(model(x), y)
        loss.backward()
        optimizer.step()
```

### Approach 2: PyTorch Lightning
```python
class Model(LightningModule):
    def training_step(self, batch, idx):
        x, y = batch
        return F.cross_entropy(self(x), y)
```

**Winner:** Approach 2 for production (less boilerplate). Approach 1 for learning.
