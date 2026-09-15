# Lesson 18 — CNN & Image Classification

## What you'll learn
- What CNNs are (convolutional neural networks for images)
- Convolutional layers (filters, kernels, padding)
- Pooling layers (max pooling, reducing dimensions)
- Building a CNN in PyTorch
- Image data loading (torchvision, transforms)
- Data augmentation (flips, rotations, shifts)
- Transfer learning (pre-trained models)
- Training and evaluating a CNN

## Lesson

### CNN architecture
```python
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc = nn.Linear(32*14*14, 10)
    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(x.size(0), -1)
        return self.fc(x)
```

### Data loading
```python
from torchvision import datasets, transforms
transform = transforms.Compose([transforms.ToTensor()])
train = datasets.MNIST('./data', train=True, download=True, transform=transform)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Load MNIST using torchvision. Visualize 5 sample images with their labels using matplotlib. Print the shape of a single image tensor.
2. `easy/p02-solve.py` — Create a single `Conv2d` layer (1→16 channels, 3x3 kernel). Pass a 28x28 MNIST image through it. Print input and output shapes. Visualize a few output feature maps.
3. `easy/p03-solve.py` — Create a `MaxPool2d` layer (2x2). Pass a 28x28 tensor through it. Print input and output shapes. Verify the spatial dimension is halved.

### Medium
4. `medium/p01-solve.py` — Build a simple CNN (2 conv layers + 1 FC layer) for MNIST. Train for 3 epochs. Print training loss and test accuracy. Target: >95% accuracy.
5. `medium/p02-solve.py` — Add data augmentation (RandomRotation, RandomAffine) to the MNIST training data. Train the same CNN. Compare test accuracy with and without augmentation.
6. `medium/p03-solve.py` — Build a CNN for CIFAR-10 (3 color channels, 32x32 images, 10 classes). Train for 5 epochs. Print test accuracy. Handle the 3-channel input correctly.

### Hard
7. `hard/p01-solve.py` — Build a complete CNN pipeline: load CIFAR-10, augment data, build a 3-block CNN (conv→relu→pool × 3 + FC), train with Adam, track train/val loss and accuracy, plot both curves, and evaluate on test set. Target: >70% accuracy.
8. `hard/p02-solve.py` — Use transfer learning: load pre-trained ResNet18, adapt it for CIFAR-10 (10 classes, 32x32 images), fine-tune for 5 epochs. Compare accuracy and training time with the from-scratch CNN.
9. `hard/p03-solve.py` — Build a CNN experiment: compare 3 architectures (shallow: 1 conv layer, medium: 2 conv layers, deep: 4 conv layers) on MNIST. For each: train, print accuracy, parameter count, and training time. Create a comparison table. Identify the best trade-off.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
