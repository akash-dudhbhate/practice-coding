# Lesson 17 — Refactoring Challenges

## Refactor 01 (Easy): Numpy for Tensors
### Before
```python
import numpy as np
x = np.array([1, 2, 3])
# no GPU support
```
### After
```python
import torch
x = torch.tensor([1, 2, 3]).to("cuda")
```

## Refactor 02 (Medium): Manual Gradient
### Before
```python
# Manual backprop math
grad = 2 * (pred - y) / len(y)
```
### After
```python
loss = nn.MSELoss()(pred, y)
loss.backward()  # autograd
```

## Refactor 03 (Hard): No DataLoader
### Before
```python
for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    # manual batching, no shuffling
```
### After
```python
from torch.utils.data import DataLoader
loader = DataLoader(dataset, batch_size=32, shuffle=True)
for batch in loader: ...
```
