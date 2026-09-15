# Lesson 18 — Approach Comparison

## Problem: Image Classification

### Approach 1: Train from scratch
```python
model = SimpleCNN()
```
**Cons:** Needs lots of data, slow training.

### Approach 2: Transfer learning
```python
model = models.resnet18(pretrained=True)
model.fc = nn.Linear(512, num_classes)
```

**Winner:** Approach 2 — faster, better results, less data needed.

---

## Problem: Prevent Overfitting

### Approach 1: Data augmentation
```python
transforms.RandomFlip(), transforms.RandomRotation(10)
```

### Approach 2: Dropout
```python
nn.Dropout(0.5)
```

**Winner:** Use both. Augmentation is more effective for images.
