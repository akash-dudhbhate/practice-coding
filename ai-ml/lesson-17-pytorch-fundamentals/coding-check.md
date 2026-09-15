# Lesson 17 — Coding Check

## Easy

### p01-solve.py — Tensors
- [ ] 1D, 2D, 3D tensors created
- [ ] Shapes, dtypes, devices printed
- [ ] Addition performed
- [ ] Multiplication performed
- [ ] Matrix multiplication performed
- [ ] PyTorch ↔ NumPy conversion works

### p02-solve.py — Autograd
- [ ] Tensor created with `requires_grad=True`
- [ ] y = x³ + 2x² + 1 computed
- [ ] `backward()` called
- [ ] Gradient printed
- [ ] Gradient matches manual: 3x² + 4x
- [ ] No sklearn used

### p03-solve.py — Single-layer model
- [ ] `nn.Module` subclass created
- [ ] `nn.Linear(5, 1)` used
- [ ] `forward()` method defined
- [ ] Random input created
- [ ] Output printed
- [ ] `super().__init__()` called

## Medium

### p01-solve.py — 2-layer network
- [ ] Network: 10 → 64 → 2
- [ ] ReLU activation between layers
- [ ] Synthetic dataset created
- [ ] SGD optimizer used
- [ ] Trained for 100 epochs
- [ ] Loss printed every 10 epochs
- [ ] Loss decreases over epochs

### p02-solve.py — Iris with DataLoader
- [ ] Custom Dataset class created
- [ ] `__len__` and `__getitem__` implemented
- [ ] DataLoader with batch_size=16, shuffle=True
- [ ] Network trained
- [ ] Test accuracy printed
- [ ] Accuracy > 80%

### p03-solve.py — Optimizer comparison
- [ ] SGD trained (loss tracked)
- [ ] SGD+momentum trained (loss tracked)
- [ ] Adam trained (loss tracked)
- [ ] Loss curves plotted on same graph
- [ ] Fastest converging optimizer identified
- [ ] Adam typically converges fastest

## Hard

### p01-solve.py — Complete training pipeline
- [ ] Custom dataset created
- [ ] DataLoader used
- [ ] 3-layer network built
- [ ] Train/val split used
- [ ] Training loop with loss tracking
- [ ] Early stopping implemented
- [ ] Final test evaluation
- [ ] Train/val/test accuracy printed
- [ ] Reproducible (random seed set)

### p02-solve.py — NN from scratch with autograd
- [ ] Weights as tensors with requires_grad=True
- [ ] Forward pass implemented manually
- [ ] ReLU activation implemented
- [ ] Backward pass uses autograd
- [ ] Trained on make_moons
- [ ] Loss decreases
- [ ] Decision boundary plotted
- [ ] No nn.Module used

### p03-solve.py — Regression pipeline
- [ ] Non-linear regression dataset created
- [ ] PyTorch MLP built
- [ ] MSE loss used
- [ ] Adam optimizer used
- [ ] Predictions vs actual plotted
- [ ] Train/val loss tracked
- [ ] Dropout added
- [ ] Dropout shown to reduce overfitting (val loss improves)
