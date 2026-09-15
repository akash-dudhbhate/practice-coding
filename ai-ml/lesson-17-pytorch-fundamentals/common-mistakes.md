# Lesson 17 — Common Mistakes

## Mistake 01: Forgetting zero_grad
```python
# WRONG — gradients accumulate
loss.backward()
optimizer.step()
# CORRECT
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

## Mistake 02: No train/eval mode
```python
# WRONG — dropout/batchnorm wrong during eval
model(x)
# CORRECT
model.eval()
with torch.no_grad():
    model(x)
model.train()  # switch back
```

## Mistake 03: No torch.no_grad for inference
```python
# WRONG — wastes memory
output = model(x)
# CORRECT
with torch.no_grad():
    output = model(x)
```

## Mistake 04: Device mismatch
```python
# WRONG — model on GPU, data on CPU
model.to("cuda")
model(x)  # x is on CPU
# CORRECT
x = x.to("cuda")
model(x)
```

## Mistake 05: Not saving model
```python
# Save after training
torch.save(model.state_dict(), "model.pth")
# Load
model.load_state_dict(torch.load("model.pth"))
```
