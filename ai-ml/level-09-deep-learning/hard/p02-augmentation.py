"""
LEVEL 09 — Deep Learning
HARD P02 — Data Augmentation Pipeline
========================================

CONCEPT:
  Augmentation = create new training images from existing ones:
    flips, rotations, crops, color jitter.
  More variety → model can't memorize → better generalization.

  transforms.Compose([...]) chains them. Applied per-sample in
  the DataLoader — every epoch sees slightly different images.

PROBLEM:
  Write `augment_pipeline()` that:
    1. Builds a transforms.Compose with:
       RandomHorizontalFlip, RandomRotation(15),
       RandomCrop(32, padding=4), ColorJitter(0.2),
       ToTensor, Normalize
    2. Applies it to a PIL image of size 32×32
    3. Returns the transform pipeline

TRY THIS INPUT:
  ```python
  t = augment_pipeline()
  print(t)          # shows the Compose
  from PIL import Image
  import numpy as np
  img = Image.fromarray(np.random.randint(0,255,(32,32,3),dtype=np.uint8))
  out = t(img)
  print(out.shape)  # torch.Size([3, 32, 32])
  ```

EXPECTED OUTPUT:
  ```
  torch.Size([3, 32, 32])
  ```

HINT:
  from torchvision import transforms
  transforms.Compose([transforms.RandomHorizontalFlip(), ...])

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# t = augment_pipeline()
# from PIL import Image; import numpy as np
# img = Image.fromarray(np.random.randint(0,255,(32,32,3),dtype=np.uint8))
# print(t(img).shape)
