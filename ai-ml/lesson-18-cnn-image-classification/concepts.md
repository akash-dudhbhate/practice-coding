# Lesson 18 — Concepts Explained (CNN & Image Classification)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is a CNN?

**What:** Convolutional Neural Networks are designed for image data. They use convolutional layers to detect patterns like edges, textures, and shapes.

```python
# A CNN typically has:
# 1. Convolutional layers: detect spatial patterns
# 2. Pooling layers: reduce spatial dimensions
# 3. Fully connected layers: final classification

# Image: 28x28 pixels → CNN detects edges → textures → shapes → objects
```

**Why it exists:** Regular neural networks (MLP) flatten images → lose spatial structure. CNNs preserve spatial relationships → detect patterns anywhere in the image → much better for images.

**Where it's used:** Image classification, object detection, facial recognition, medical imaging, self-driving cars.

**What goes wrong without it:**
- Using MLP on images → too many parameters (28x28 = 784 inputs → huge first layer) → overfits, slow.
- Not normalizing images → pixel values 0-255 → large gradients → unstable training. Normalize to 0-1.
- Wrong input shape → PyTorch expects (batch, channels, height, width). MNIST: (B, 1, 28, 28).

---

## Convolutional Layers

**What:** Conv layers slide a filter (kernel) over the image to detect patterns.

```python
import torch.nn as nn

# Conv2d: 1 input channel (grayscale), 32 output channels (filters), 3x3 kernel
conv = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1)

# Input: (batch, 1, 28, 28) → Output: (batch, 32, 28, 28)
# padding=1 → keeps the same spatial size
# Each of the 32 filters detects a different pattern (edges, corners, etc.)
```

**Why it exists:** Convolution preserves spatial structure and is translation-invariant (detects a cat anywhere in the image, not just one corner). Much fewer parameters than fully connected → efficient.

**Where it's used:** Every CNN — the core building block.

**What goes wrong without it:**
- `kernel_size=3` → common. Larger (5, 7) → more context but more parameters. Smaller (1) → no spatial info.
- `padding=0` → output is smaller than input (border pixels are lost). Use `padding=1` for same-size output with 3x3.
- `stride=2` → output is half the size (downsampling). Use for reducing dimensions instead of pooling.

---

## Pooling Layers

**What:** Pooling reduces spatial dimensions → fewer parameters, less computation.

```python
# Max pooling: take the maximum value in each window
pool = nn.MaxPool2d(kernel_size=2, stride=2)
# Input: (batch, 32, 28, 28) → Output: (batch, 32, 14, 14)
# Reduces spatial size by half

# Average pooling: take the average
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2)

# Adaptive pooling: output a fixed size regardless of input
adaptive = nn.AdaptiveAvgPool2d((1, 1))  # → (batch, 32, 1, 1)
```

**Why it exists:** Without pooling, the network has too many parameters → overfits, slow. Pooling reduces dimensions while keeping important information → efficient, robust to small translations.

**Where it's used:** Between conv layers in CNNs.

**What goes wrong without it:**
- Max pooling loses exact position → keeps the strongest feature. Good for classification, bad for localization.
- Pooling too aggressively (large kernel) → loses too much information → poor performance.
- Global average pooling (adaptive) → replaces fully connected layers → fewer parameters, less overfitting.

---

## Building a CNN in PyTorch

**What:** A complete CNN architecture for image classification.

```python
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        # Conv blocks
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)   # 1→32 channels
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)   # 32→64 channels
        self.pool = nn.MaxPool2d(2, 2)
        self.relu = nn.ReLU()

        # Fully connected layers
        self.fc1 = nn.Linear(64 * 7 * 7, 128)  # after 2 pools: 28→14→7
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        # Block 1: conv → relu → pool
        x = self.pool(self.relu(self.conv1(x)))  # (B, 32, 14, 14)
        # Block 2: conv → relu → pool
        x = self.pool(self.relu(self.conv2(x)))  # (B, 64, 7, 7)
        # Flatten
        x = x.view(x.size(0), -1)                # (B, 64*7*7)
        # Classify
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x
```

**Why it exists:** This is the standard CNN pattern: conv blocks (detect features) → flatten → fully connected (classify). Understanding this pattern → you can build any CNN.

**Where it's used:** Every image classification task.

**What goes wrong without it:**
- `x.view(x.size(0), -1)` → flatten keeping batch dimension. Using `x.view(-1)` → merges batch into features → wrong.
- FC input size must match: after 2 pools on 28x28 → 7x7, with 64 channels → 64*7*7 = 3136. Mismatch → error.
- Not using ReLU between conv layers → just linear operations → no non-linearity → poor model.

---

## Image Data Loading

**What:** Loading and preprocessing image data.

```python
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Transforms: preprocessing pipeline
transform = transforms.Compose([
    transforms.ToTensor(),              # PIL → tensor, scale to 0-1
    transforms.Normalize((0.5,), (0.5,))  # normalize to -1 to 1
])

# Load MNIST
train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST('./data', train=False, transform=transform)

# DataLoaders
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)
```

**Why it exists:** Without torchvision, you'd manually load images, convert to tensors, normalize → tedious. torchvision handles it → plus built-in datasets (MNIST, CIFAR, ImageNet).

**Where it's used:** Every image classification project.

**What goes wrong without it:**
- Forgetting `transforms.ToTensor()` → images are PIL objects, not tensors → model can't process.
- `Normalize((0.5,), (0.5,))` → for grayscale (1 channel). For RGB: `Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))`.
- `download=True` → downloads the dataset. For large datasets (ImageNet), download manually.

---

## Data Augmentation

**What:** Artificially expand the training data with transformations.

```python
transform_train = transforms.Compose([
    transforms.RandomHorizontalFlip(),    # 50% chance to flip
    transforms.RandomRotation(10),        # rotate ±10 degrees
    transforms.RandomAffine(0, translate=(0.1, 0.1)),  # shift
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])
```

**Why it exists:** Without augmentation, the model sees the same images every epoch → memorizes → overfits. Augmentation creates "new" images → model learns robust features → better generalization.

**Where it's used:** Every image classification with limited data.

**What goes wrong without it:**
- Too aggressive augmentation (90-degree rotation for digits) → creates unrealistic images → confuses model.
- Augmenting test data → test should be clean → only normalize, don't augment.
- Forgetting to augment → model overfits → poor test accuracy. Augmentation is one of the most effective regularization techniques for images.

---

## Transfer Learning

**What:** Use a pre-trained model (trained on ImageNet) and fine-tune it for your task.

```python
import torchvision.models as models

# Load pre-trained ResNet
model = models.resnet18(pretrained=True)

# Replace the final layer for your number of classes
model.fc = nn.Linear(model.fc.in_features, num_classes)

# Freeze feature layers (optional)
for param in model.parameters():
    param.requires_grad = False
model.fc.requires_grad = True  # only train the final layer
```

**Why it exists:** Training a CNN from scratch needs millions of images and days of GPU time. Transfer learning uses a pre-trained model → already knows edges, textures, shapes → fine-tune on your small dataset → great results with little data.

**Where it's used:** Every practical image classification task — almost no one trains from scratch.

**What goes wrong without it:**
- Not replacing the final layer → model outputs 1000 ImageNet classes instead of your classes → wrong.
- Freezing all layers → only the final layer trains → might underfit. Unfreeze later layers for better performance.
- Different input size → ResNet expects 224x224. Resize your images or adapt the model.

---

## Training a CNN

**What:** The training loop for a CNN.

```python
model = SimpleCNN(num_classes=10)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(5):
    model.train()
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    # Evaluate
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f"Epoch {epoch}: {100*correct/total:.2f}% accuracy")
```

**Why it exists:** The CNN training loop is the same as any PyTorch training loop — but with images as input. Understanding it lets you train any CNN.

**Where it's used:** Every CNN training.

**What goes wrong without it:**
- Not switching between `model.train()` and `model.eval()` → dropout/batch norm behave wrong → inconsistent results.
- GPU: move model and data to GPU → 10-100x faster. `model = model.cuda()`, `images = images.cuda()`.
- Too many epochs without early stopping → overfits. Monitor validation accuracy.
