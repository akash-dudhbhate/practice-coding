# Lesson 17 — PyTorch Fundamentals

## What you'll learn
- What PyTorch is (NumPy + GPU + autograd)
- Tensors (creation, operations, properties)
- Autograd (automatic differentiation)
- Building neural networks (nn.Module)
- The training loop (forward, backward, step)
- Datasets and DataLoaders (batching, shuffling)
- Loss functions and optimizers
- Evaluation and inference (eval mode, no_grad)

## Lesson

### Model
```python
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 2)
    def forward(self, x):
        return self.fc(x)
```

### Training loop
```python
for epoch in range(10):
    for X, y in dataloader:
        optimizer.zero_grad()
        loss = criterion(model(X), y)
        loss.backward()
        optimizer.step()
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Create tensors: 1D, 2D, and 3D. Print their shapes, dtypes, and devices. Perform addition, multiplication, and matrix multiplication. Convert between PyTorch and NumPy.
2. `easy/p02-solve.py` — Use autograd: create a tensor with `requires_grad=True`, compute y = x³ + 2x² + 1, call `backward()`, print the gradient (dy/dx = 3x² + 4x). Verify manually.
3. `easy/p03-solve.py` — Build a single-layer `nn.Module` (Linear with 5 inputs, 1 output). Create random input, pass it through the model, print the output. No training yet.

### Medium
4. `medium/p01-solve.py` — Build a 2-layer neural network with `nn.Module` (10 → 64 → 2). Use ReLU activation. Create a synthetic dataset, train for 100 epochs with SGD, print the loss every 10 epochs.
5. `medium/p02-solve.py` — Create a custom Dataset for the Iris dataset. Use a DataLoader with batch_size=16 and shuffle=True. Train a simple network. Print accuracy on the test set.
6. `medium/p03-solve.py` — Compare optimizers: train the same network with SGD, SGD+momentum, and Adam. Plot the loss curves for all three on the same graph. Identify the fastest converging optimizer.

### Hard
7. `hard/p01-solve.py` — Build a complete PyTorch training pipeline: custom dataset, DataLoader, 3-layer network, training loop with train/val split, loss tracking, early stopping, and final test evaluation. Print train/val/test accuracy.
8. `hard/p02-solve.py` — Implement a neural network from scratch using only tensors and autograd (no nn.Module). Define weights as tensors with requires_grad=True. Implement forward and backward manually. Train on make_moons. Plot the decision boundary.
9. `hard/p03-solve.py` — Build a regression pipeline: create a non-linear regression dataset, build a PyTorch MLP, train with MSE loss and Adam optimizer, plot predictions vs actual, and track train/val loss. Add dropout and show it reduces overfitting.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
