# Lesson 18 — Intuition Checks

## Check 01: How CNNs work
<details><summary>Answer</summary>
Convolution layers slide filters over image to detect patterns (edges, textures). Pooling reduces dimensions. Deeper layers detect complex patterns (faces, objects). Fully connected layers at end for classification.
</details>

## Check 02: Conv2d parameters
```python
nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)
```
<details><summary>Answer</summary>
in_channels — input depth (3 for RGB). out_channels — number of filters. kernel_size — filter size (3x3). padding — add zeros to keep dimensions.
</details>

## Check 03: Pooling
```python
nn.MaxPool2d(2)  # reduces dimensions by half
```
<details><summary>Answer</summary>
Max pooling takes maximum value in each 2x2 window. Reduces spatial dimensions, provides translation invariance, reduces computation.
</details>

## Check 04: Transfer learning
```python
model = models.resnet18(pretrained=True)
model.fc = nn.Linear(512, num_classes)
```
<details><summary>Answer</summary>
Use pretrained model (trained on ImageNet). Replace final layer for your classes. Freeze early layers (general features), train final layer (specific features). Much faster than training from scratch.
</details>

## Check 05: Data augmentation
```python
transforms.RandomHorizontalFlip()
transforms.RandomRotation(10)
transforms.ColorJitter(brightness=0.2)
```
<details><summary>Answer</summary>
Creates variations of training images. Model sees more diverse data, generalizes better. Only for training, not validation/test.
</details>
