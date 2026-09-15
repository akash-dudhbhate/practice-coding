# Lesson 18 — Common Mistakes

## Mistake 01: Wrong input shape
```python
# WRONG — flattened
x.shape  # (32, 784)
# CORRECT — 4D
x = x.view(-1, 1, 28, 28)  # (32, 1, 28, 28)
```

## Mistake 02: No normalization
```python
# WRONG
transforms.ToTensor()
# CORRECT
transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])
```

## Mistake 03: No augmentation for small data
```python
# Add augmentation for training
transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
])
```

## Mistake 04: Not using transfer learning
```python
# WRONG — train from scratch (slow, needs lots of data)
# CORRECT — use pretrained
models.resnet18(pretrained=True)
```

## Mistake 05: Not freezing pretrained layers
```python
# Freeze early layers
for param in model.parameters():
    param.requires_grad = False
# Only train final layer
model.fc.requires_grad = True
```
