# Lesson 18 — Coding Check

## Easy

### p01-solve.py — Load and visualize MNIST
- [ ] MNIST loaded with torchvision
- [ ] 5 sample images visualized with matplotlib
- [ ] Labels displayed with images
- [ ] Image tensor shape printed: (1, 28, 28)
- [ ] Pixel values in [0, 1] (ToTensor applied)

### p02-solve.py — Conv2d layer
- [ ] `Conv2d(1, 16, 3, padding=1)` created
- [ ] 28x28 image passed through
- [ ] Input shape printed: (1, 1, 28, 28)
- [ ] Output shape printed: (1, 16, 28, 28)
- [ ] Feature maps visualized

### p03-solve.py — MaxPool2d
- [ ] `MaxPool2d(2, 2)` created
- [ ] 28x28 tensor passed through
- [ ] Input shape printed: (28, 28)
- [ ] Output shape printed: (14, 14)
- [ ] Spatial dimension halved

## Medium

### p01-solve.py — Simple CNN for MNIST
- [ ] CNN with 2 conv layers + 1 FC built
- [ ] Trained for 3 epochs
- [ ] Training loss printed per epoch
- [ ] Test accuracy printed
- [ ] Accuracy > 95%
- [ ] Uses CrossEntropyLoss and Adam

### p02-solve.py — Data augmentation
- [ ] RandomRotation added to training transforms
- [ ] RandomAffine added
- [ ] CNN trained with augmentation
- [ ] CNN trained without augmentation
- [ ] Test accuracy compared
- [ ] Augmentation improves accuracy (or reduces overfitting)

### p03-solve.py — CNN for CIFAR-10
- [ ] CIFAR-10 loaded (3 channels, 32x32)
- [ ] CNN handles 3-channel input (in_channels=3)
- [ ] Trained for 5 epochs
- [ ] Test accuracy printed
- [ ] Accuracy > 50% (CIFAR is harder than MNIST)

## Hard

### p01-solve.py — Complete CNN pipeline
- [ ] CIFAR-10 loaded
- [ ] Data augmentation applied
- [ ] 3-block CNN built (conv→relu→pool × 3)
- [ ] FC layers for classification
- [ ] Adam optimizer used
- [ ] Train/val loss tracked
- [ ] Train/val accuracy tracked
- [ ] Both curves plotted
- [ ] Test accuracy > 70%
- [ ] Model.eval() and torch.no_grad() used for evaluation

### p02-solve.py — Transfer learning
- [ ] ResNet18 loaded with pretrained=True
- [ ] Final layer replaced for 10 classes
- [ ] Input adapted for 32x32 (resize or adaptive pooling)
- [ ] Fine-tuned for 5 epochs
- [ ] Test accuracy printed
- [ ] Training time measured
- [ ] Compared with from-scratch CNN
- [ ] Transfer learning is faster and/or more accurate

### p03-solve.py — Architecture comparison
- [ ] Shallow CNN (1 conv layer) built and trained
- [ ] Medium CNN (2 conv layers) built and trained
- [ ] Deep CNN (4 conv layers) built and trained
- [ ] Accuracy printed for each
- [ ] Parameter count printed for each
- [ ] Training time measured for each
- [ ] Comparison table created
- [ ] Best trade-off identified (accuracy vs speed)
