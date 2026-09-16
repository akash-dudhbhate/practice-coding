# Level 08 — Concepts Reference

## Easy

### Perceptron
- `output = step(x·w + b)` — the simplest neuron
- Learns by nudging weights toward the right answer

### Activation Functions
- sigmoid → (0,1), ReLU → kills negatives, tanh → (-1,1)
- Without these, a network = one big linear regression

### PyTorch Tensors
- `torch.tensor(...)` — like NumPy arrays + GPU + autograd
- `.requires_grad_(True)` + `.backward()` = auto gradients

## Medium

### XOR Problem
- XOR isn't linearly separable — a single perceptron CAN'T solve it
- Hidden layer (2→2→1) makes it possible — the birth of deep learning

### PyTorch Training Pattern
- `model(X) → loss → optimizer.zero_grad() → loss.backward() → optimizer.step()`
- `nn.Linear(in, out)`, `nn.ReLU()`, `nn.CrossEntropyLoss()`

### MLP
- `nn.Sequential(Linear, ReLU, Linear)` — stack layers
- CrossEntropyLoss for classification (combines softmax + NLL)

## Hard

### Manual Backprop
- Chain rule backwards: `dL/dW = error · sigmoid' · input`
- This is what `.backward()` does for you — now you've seen the math

### Full Training Loop
- DataLoader (batches) → train loop → eval loop → track metrics
- `model.train()` / `model.eval()` / `torch.no_grad()`

### MNIST
- `torchvision.datasets.MNIST` — 70K handwritten digits
- Flatten 28×28 → Linear(784,128) → ReLU → Linear(128,10) → ~97% accuracy
