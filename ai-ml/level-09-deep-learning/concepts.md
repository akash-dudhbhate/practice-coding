# Level 09 — Concepts Reference

## Easy

### Convolution
- Slide a kernel over the image, dot product at each position
- [1,0,-1] detects vertical edges — that's how CNNs "see"

### CNN Architecture
- `Conv2d(in_ch, out_ch, kernel, padding)` → ReLU → MaxPool → repeat
- `Flatten → Linear` at the end for classification

### Max Pooling
- Take max of each 2×2 block — halves size, keeps strongest signal
- Gives translation invariance (feature present? not where exactly)

## Medium

### CIFAR-10
- 60K color images (32×32), 10 classes
- `datasets.CIFAR10` downloads automatically via torchvision

### BatchNorm
- `nn.BatchNorm1d(n)` between Linear and ReLU
- Stabilizes training — each layer sees mean-0, std-1 inputs

### Dropout
- `nn.Dropout(0.5)` — kills 50% of neurons randomly during training
- Forces redundant features; only active in .train() mode

## Hard

### Transfer Learning
- `models.resnet18()` → replace `.fc` with your output layer
- Pretrained layers know edges/shapes — you teach the classes
- Freeze backbone for speed, or fine-tune for accuracy

### Data Augmentation
- `transforms.Compose([flip, rotate, crop, jitter, ToTensor, Normalize])`
- New variations each epoch → model generalizes better

### Custom nn.Module
- Subclass nn.Module, define layers in `__init__`, logic in `forward()`
- For complex architectures (skip connections, multiple heads)
