# Level 08 — Neural Networks

## What You'll Learn
- Perceptron — the simplest neuron
- Activation functions (sigmoid, ReLU, tanh)
- Why hidden layers are needed (XOR problem)
- Backpropagation from scratch
- PyTorch: tensors, nn.Linear, training loops, MLPs
- MNIST digit recognition

## Prerequisites
- Level 00 (dot product, weighted sum)
- Level 04 (gradient descent intuition)
- `pip install torch torchvision` (CPU version is fine)

## Problems

### Easy
1. `easy/p01-perceptron.py` — `train_perceptron()` → solve OR gate
2. `easy/p02-activation-functions.py` — `sigmoid/relu/tanh(z)` → implement all three
3. `easy/p03-pytorch-tensors.py` — `tensor_basics()` → torch operations

### Medium
4. `medium/p01-xor-hidden-layer.py` — `solve_xor()` → 2-2-1 network
5. `medium/p02-pytorch-linear.py` — `train_linear()` → nn.Linear training loop
6. `medium/p03-pytorch-mlp.py` — `train_mlp()` → Linear→ReLU→Linear

### Hard
7. `hard/p01-manual-backprop.py` — `train_manual()` → numpy backprop on XOR
8. `hard/p02-pytorch-full-training.py` — `train()` → DataLoader + val loop
9. `hard/p03-mnist-nn.py` — `train_mnist()` → real handwritten digits

### Project
`project/` — MNIST digit recognizer with visualization.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
