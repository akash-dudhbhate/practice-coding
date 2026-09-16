# Level 09 — Deep Learning

## What You'll Learn
- Convolution — sliding filters over images
- CNN architecture — conv → pool → classify
- Max pooling — downsampling with strongest signal
- CIFAR-10 training, batch norm, dropout
- Transfer learning — ResNet18 pretrained
- Data augmentation — flips, crops, jitter
- Custom nn.Module — real model architecture

## Prerequisites
- Level 08 (PyTorch basics)

## Problems

### Easy
1. `easy/p01-convolution.py` — `convolve(img, kernel)` → 2D conv by hand
2. `easy/p02-cnn-architecture.py` — `build_cnn()` → nn.Sequential CNN
3. `easy/p03-pooling.py` — `max_pool(img)` → 2×2 pooling by hand

### Medium
4. `medium/p01-cnn-training.py` — `train_cnn()` → CIFAR-10 CNN
5. `medium/p02-batchnorm.py` — `compare_bn()` → with/without BatchNorm
6. `medium/p03-dropout.py` — `compare_dropout()` → dropout effect

### Hard
7. `hard/p01-transfer-learning.py` — `transfer_learn()` → ResNet on CIFAR-10
8. `hard/p02-augmentation.py` — `augment_pipeline()` → transform.Compose
9. `hard/p03-custom-module.py` — `CustomCNN` + `count_params()` → real model class

### Project
`project/` — Full CIFAR-10 classifier with augmentation.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
