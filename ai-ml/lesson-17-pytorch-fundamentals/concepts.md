# Lesson 17 — Concepts Explained (PyTorch Fundamentals)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is PyTorch?

**What:** PyTorch is a deep learning framework — like NumPy but with GPU support and automatic differentiation.

```python
import torch

# Tensors (like NumPy arrays but can run on GPU)
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

# Operations
z = x + y  # tensor([5, 7, 9])

# GPU
if torch.cuda.is_available():
    x = x.cuda()  # move to GPU
    y = y.cuda()
    z = x + y     # computed on GPU
```

**Why it exists:** NumPy can't use GPUs or compute gradients automatically. PyTorch adds both → train neural networks on GPUs → 100x faster than CPU.

**Where it's used:** Deep learning research, production AI, computer vision, NLP, any neural network task.

**What goes wrong without it:**
- Not installing: `pip install torch`.
- CPU vs GPU tensors → can't mix: `cpu_tensor + gpu_tensor` → error. Move both to the same device.
- Not setting random seed → non-reproducible results. Use `torch.manual_seed(42)`.

---

## Tensors

**What:** Tensors are multi-dimensional arrays — the core data structure in PyTorch.

```python
# Create tensors
x = torch.tensor([1, 2, 3])                    # 1D
x = torch.zeros(3, 4)                           # 2D: 3x4 zeros
x = torch.ones(2, 3, 4)                         # 3D: 2x3x4 ones
x = torch.randn(100, 10)                        # 2D: random normal
x = torch.arange(0, 10, 2)                      # [0, 2, 4, 6, 8]

# Properties
x.shape      # torch.Size([3, 4])
x.dtype      # torch.float32
x.device     # device(type='cpu')

# Operations
x = torch.tensor([[1, 2], [3, 4]])
x.sum()      # tensor(10)
x.mean()     # tensor(2.5)
x.T          # transpose
x @ x        # matrix multiplication
```

**Why it exists:** Tensors are the data format for neural networks. Understanding them is essential — every input, weight, and output is a tensor.

**Where it's used:** Every PyTorch operation.

**What goes wrong without it:**
- `torch.tensor([1, 2])` → dtype is int64. Neural networks need float32. Use `torch.tensor([1.0, 2.0])` or `torch.FloatTensor([1, 2])`.
- Shape mismatches → `torch.matmul(a, b)` → a is (3, 4), b is (3, 4) → error. b must be (4, something).
- Reshaping: `x.view(3, 4)` → fails if total size doesn't match. Use `x.reshape(3, 4)` (more flexible).

---

## Autograd (Automatic Differentiation)

**What:** PyTorch automatically computes gradients for backpropagation.

```python
# Gradients are computed automatically
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2 + 3 * x + 1  # y = x² + 3x + 1
y.backward()             # compute gradients
print(x.grad)            # dy/dx = 2x + 3 = 7.0

# In training:
# 1. Forward pass: compute loss
# 2. loss.backward(): compute all gradients
# 3. optimizer.step(): update weights using gradients
```

**Why it exists:** Without autograd, you'd manually compute derivatives for every operation → impossible for complex networks. Autograd handles it → you just write the forward pass.

**Where it's used:** Every neural network training in PyTorch.

**What goes wrong without it:**
- Forgetting `requires_grad=True` → no gradient computed → weights don't update.
- Not calling `optimizer.zero_grad()` before `backward()` → gradients accumulate → wrong updates.
- Calling `backward()` twice without `retain_graph=True` → error (graph is freed after first backward).

---

## Building a Neural Network (nn.Module)

**What:** PyTorch's `nn.Module` is the base class for all neural networks.

```python
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 64)   # input=10, output=64
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 2)    # output=2 (binary classification)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)                # no activation (raw logits)
        return x

model = SimpleNet()
```

**Why it exists:** `nn.Module` handles the boilerplate — parameter tracking, GPU movement, saving/loading. You just define the layers and the forward pass → clean and reusable.

**Where it's used:** Every PyTorch model.

**What goes wrong without it:**
- Forgetting `super().__init__()` → parameters aren't registered → model doesn't work.
- Not defining `forward()` → calling `model(x)` → error.
- Applying activation after the last layer → for classification with CrossEntropyLoss, don't apply softmax (the loss applies it internally).

---

## Training Loop

**What:** The standard PyTorch training loop.

```python
import torch.optim as optim

model = SimpleNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10):
    for batch_X, batch_y in dataloader:
        # 1. Forward pass
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)

        # 2. Backward pass
        optimizer.zero_grad()    # clear old gradients
        loss.backward()          # compute new gradients

        # 3. Update weights
        optimizer.step()

    print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
```

**Why it exists:** This is the core of PyTorch training. Understanding each step → you can debug any training issue.

**Where it's used:** Every PyTorch training script.

**What goes wrong without it:**
- Forgetting `optimizer.zero_grad()` → gradients accumulate → weights update too much → divergence.
- `loss.item()` → extracts the scalar. `print(loss)` → prints the tensor with grad info → messy.
- Not moving data to GPU → model on GPU, data on CPU → error. Use `batch_X.to(device)`.

---

## Datasets and DataLoaders

**What:** PyTorch provides `Dataset` and `DataLoader` for efficient data loading.

```python
from torch.utils.data import Dataset, DataLoader

# Custom dataset
class MyDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.FloatTensor(X)
        self.y = torch.LongTensor(y)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# DataLoader: batching, shuffling, parallel loading
dataset = MyDataset(X_train, y_train)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

for batch_X, batch_y in dataloader:
    # batch_X: (32, n_features)
    # batch_y: (32,)
    outputs = model(batch_X)
```

**Why it exists:** Without DataLoaders, you'd manually batch and shuffle → error-prone. DataLoaders handle it → plus parallel loading → fast training.

**Where it's used:** Every PyTorch training with more than a few samples.

**What goes wrong without it:**
- `__getitem__` returning wrong type → model expects float, gets int → error. Use `torch.FloatTensor`.
- `batch_size` too large → out of memory (GPU). Reduce batch size.
- Not shuffling → model sees data in the same order every epoch → biased training. Use `shuffle=True`.

---

## Loss Functions and Optimizers

**What:** Loss functions measure error; optimizers update weights.

```python
import torch.nn as nn
import torch.optim as optim

# Loss functions
criterion_cls = nn.CrossEntropyLoss()    # multiclass classification
criterion_binary = nn.BCEWithLogitsLoss()  # binary classification
criterion_reg = nn.MSELoss()             # regression

# Optimizers
optimizer_sgd = optim.SGD(model.parameters(), lr=0.01)
optimizer_adam = optim.Adam(model.parameters(), lr=0.001)
optimizer_adamw = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)
```

**Why it exists:** Different tasks need different loss functions. Different optimizers have different convergence behaviors. Choosing the right ones is crucial.

**Where it's used:** Every PyTorch training.

**What goes wrong without it:**
- `CrossEntropyLoss` expects class indices (0, 1, 2), NOT one-hot. `BCEWithLogitsLoss` expects floats (0.0, 1.0).
- SGD without momentum → slow convergence. Use `SGD(momentum=0.9)` or Adam.
- Learning rate too high → loss diverges (NaN). Too low → barely learns. Start with 0.001 for Adam.

---

## Evaluation and Inference

**What:** How to evaluate a trained model.

```python
# Evaluation mode: turns off dropout, batch norm uses running stats
model.eval()

# No gradient computation (faster, less memory)
with torch.no_grad():
    outputs = model(X_test)
    _, predicted = torch.max(outputs, 1)
    accuracy = (predicted == y_test).float().mean()

print(f"Accuracy: {accuracy.item():.4f}")

# Don't forget to switch back to training mode
model.train()
```

**Why it exists:** During evaluation, you don't need gradients (no training) → `torch.no_grad()` saves memory and time. `model.eval()` turns off dropout and batch norm → correct inference behavior.

**Where it's used:** Every model evaluation and inference.

**What goes wrong without it:**
- Forgetting `model.eval()` → dropout still active → inconsistent predictions.
- Forgetting `torch.no_grad()` → gradients computed → wastes memory → might OOM on large data.
- Forgetting `model.train()` after evaluation → subsequent training has dropout off → wrong training.
