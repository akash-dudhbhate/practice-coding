# Lesson 18 — Refactoring Challenges

## Refactor 01 (Easy): Manual Conv2D
### Before
```python
# implement convolution with nested loops
for i in range(h):
    for j in range(w):
        out[i, j] = sum(kernel * image[i:i+k, j:j+k])
```
### After
```python
conv = nn.Conv2d(3, 16, kernel_size=3)
out = conv(image)
```

## Refactor 02 (Medium): No Augmentation
### Before
```python
model.fit(X_train, y_train)  # raw images, may overfit
```
### After
```python
from torchvision import transforms
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
])
```

## Refactor 03 (Hard): Training from Scratch
### Before
```python
model = MyCNN()  # train from scratch, needs lots of data
model.fit(X, y, epochs=100)
```
### After
```python
import torchvision.models as models
model = models.resnet18(pretrained=True)
model.fc = nn.Linear(512, num_classes)  # transfer learning
```
