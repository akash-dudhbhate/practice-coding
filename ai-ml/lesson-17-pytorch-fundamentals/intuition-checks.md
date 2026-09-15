# Lesson 17 — Intuition Checks

## Check 01: Tensor
```python
x = torch.tensor([1, 2, 3])
x.dtype  # torch.int64
x = torch.tensor([1.0, 2.0])
x.dtype  # torch.float32
```
<details><summary>Answer</summary>
Tensors are like numpy arrays but: support GPU, track gradients, work with autograd. Default float type is float32.
</details>

## Check 02: Autograd
```python
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
y.backward()
print(x.grad)  # 4.0
```
<details><summary>Answer</summary>
Autograd tracks operations. `backward()` computes gradients. dy/dx = 2x = 4.0 at x=2. Essential for training neural networks.
</details>

## Check 03: Training loop
```python
for epoch in range(epochs):
    for x, y in dataloader:
        optimizer.zero_grad()
        output = model(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
```
<details><summary>Answer</summary>
Standard PyTorch training loop: zero gradients, forward pass, compute loss, backward pass (gradients), update weights. Repeat for each batch and epoch.
</details>

## Check 04: GPU
```python
model = model.to("cuda")
x = x.to("cuda")
```
<details><summary>Answer</summary>
Move model and data to GPU for faster computation. Both must be on same device. `torch.cuda.is_available()` checks if GPU is available.
</details>

## Check 05: DataLoader
```python
DataLoader(dataset, batch_size=32, shuffle=True)
```
<details><summary>Answer</summary>
Handles batching, shuffling, parallel loading. `shuffle=True` for training (randomize), `shuffle=False` for testing (reproducible).
</details>
