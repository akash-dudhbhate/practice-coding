# Level 08 Neural Networks — Neural Networks & PyTorch

## What You'll Learn
- Perceptron and activation functions
- Forward and backward propagation
- Loss functions and optimizers
- PyTorch tensors and autograd
- Building nn.Module
- Training loops

## Prerequisites
- Previous levels completed
- Python basics

## How This Level Works

Each problem has:
1. **CONCEPT** — the idea you need to understand
2. **PROBLEM** — what to build
3. **TRY THIS INPUT** — test code to verify your solution
4. **EXPECTED OUTPUT** — what it should print
5. **AUTO-CHECK** — run `check.py` to verify automatically

Start with `easy/` problems, then `medium/`, then `hard/`, then the project.

---

## Problems

### Easy
1. `easy/p01-perceptron.py` — Implement a single perceptron from scratch. Train on OR gate...
2. `easy/p02-activation-functions.py` — Implement sigmoid, ReLU, and tanh from scratch. Plot them....
3. `easy/p03-pytorch-tensor.py` — Create PyTorch tensors, do basic operations, compute gradien...

### Medium
4. `medium/p01-mlp-scratch.py` — Build a 2-layer neural network from scratch. Train on XOR....
5. `medium/p02-pytorch-nn.py` — Build a neural network with nn.Module. Train on synthetic da...
6. `medium/p03-training-loop.py` — Write a complete PyTorch training loop with loss tracking....

### Hard
7. `hard/p01-backprop-scratch.py` — Implement backpropagation from scratch for a 2-layer network...
8. `hard/p02-custom-loss.py` — Implement a custom loss function in PyTorch....
9. `hard/p03-transfer-learning.py` — Use a pretrained model (ResNet) for a new classification tas...

### Project
`project/` — Build a MNIST digit recognizer with PyTorch from scratch.

---

## Verify Your Work

```bash
# Run a problem
python3 easy/p01-perceptron.py

# Check your answer
python3 check.py easy/p01
```

When `check.py` says "PASS", add `# DONE` to the first line and move on.
