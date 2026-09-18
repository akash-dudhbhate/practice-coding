# Level 09 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept explains:
What it is · Why it exists · Where it's used · What goes wrong without it ·
worked example · code · expected output.

---

## Easy

### 1. Convolution (The Filter) — `p01`

**What it is:** Slide a small matrix (the "kernel" or "filter")
across an image; at each position, multiply the overlapping patch
element-wise and sum to one number. Kernels act as pattern
detectors — one kernel finds vertical edges, another finds
horizontal edges, another finds corners.

**Why it exists:** Before CNNs, vision systems used hand-designed
feature detectors — an expert had to engineer a new filter set per
domain. Convolution was adopted because the SAME small kernel
scans the whole image (weight sharing), so one detector finds its
pattern anywhere — and crucially, the kernels themselves can be
*learned* by backprop instead of designed by hand.

**Where it's used:** This is THE operation of computer vision —
CNNs, ResNet, YOLO, and also audio spectrograms. Layer 1 learns
edge detectors, deeper layers compose those into textures, then
shapes, then objects.

**What goes wrong without it:** Flatten a 224×224×3 image into a
dense layer and the first layer alone has ~150K inputs — billions
of parameters, it memorizes pixel positions, and a cat shifted 5
pixels looks like a brand-new object. Also practical traps: the
output SHRINKS without padding — a 28×28 image with a 3×3 kernel
gives 26×26, not 28×28 (use `padding=1` in Conv2d). And the kernel
isn't flipped — deep-learning "convolution" is technically
cross-correlation; nobody cares, the learned weights absorb the
difference.

**Worked example:** Vertical-edge kernel on a 4×4 image:
```
image:                kernel (3×3):
[[1,2,3,0],           [[1,0,-1],
 [4,5,6,0],            [1,0,-1],
 [7,8,9,0],            [1,0,-1]]
 [0,0,0,0]]

Position (0,0): patch [[1,2,3],[4,5,6],[7,8,9]] × kernel
  = (1·1 + 2·0 + 3·-1) + (4·1 + 5·0 + 6·-1) + (7·1 + 8·0 + 9·-1)
  = (1-3) + (4-6) + (7-9) = -2-2-2 = -6   ← strong response!

Output shape: (4-3+1, 4-3+1) = (2, 2) — valid convolution.
The -6 says "left bright, right dark" → vertical edge detected.
```

**Code:**
```python
def convolve(image, kernel):
    H, W = image.shape; k = kernel.shape[0]
    out = np.zeros((H-k+1, W-k+1))
    for i in range(H-k+1):
        for j in range(W-k+1):
            out[i,j] = np.sum(image[i:i+k, j:j+k] * kernel)
    return out
```

**Expected output:** On the worked-example image and kernel,
`convolve(image, kernel)` → `[[-6., 15.], [-4., 13.]]` — a 2×2
map where the strong negative (-6, -4) column marks the vertical
edge.

---

### 2. CNN Architecture — `p02`

**What it is:** The standard recipe: `Conv → ReLU → MaxPool`
repeated (extracts features at growing scales), then `Flatten →
Linear` (classify from those features). Each conv layer outputs
"feature maps" — one per learned filter.

**Why it exists:** A single conv layer can only detect simple
patterns — an edge, a corner. Stacking conv+pool lets later layers
compose simple detectors into complex ones (edges → textures →
shapes → objects), while pooling shrinks the spatial size so
deeper layers stay cheap. The "channels grow, space shrinks"
pattern exists to trade *where* for *what*.

**Where it's used:** ResNet, VGG, every vision net — 1→16→32
channels while 28→14→7 is the universal shape. Channels hold "what
was detected"; spatial dims hold "where."

**What goes wrong without it:** The Flatten→Linear size (1568
here) must be computed BY HAND from the shape trace — get it wrong
and you get a `mat1 and mat2 shapes` error at runtime. Skip
pooling and the spatial dims never shrink → the Flatten vector is
enormous and the Linear layer explodes in parameters. Always trace
the tensor through each layer on paper first.

**Worked example:** Tracing shapes through the problem's CNN on a
28×28 grayscale digit:
```
Input:        [1, 1, 28, 28]      (batch, channels, H, W)
Conv2d(1,16,3,padding=1) → [1,16,28,28]   16 filters, size kept
MaxPool2d(2)             → [1,16,14,14]   halved
Conv2d(16,32,3,padding=1)→ [1,32,14,14]   32 filters
MaxPool2d(2)             → [1,32, 7, 7]   halved again
Flatten()                → [1, 1568]      32×7×7 = 1568
Linear(1568,128)→ReLU→Linear(128,10) → [1,10] class logits
```

**Code:**
```python
model = nn.Sequential(
    nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
    nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
    nn.Flatten(), nn.Linear(32*7*7, 128), nn.ReLU(), nn.Linear(128, 10)
)
```

**Expected output:** `model(torch.randn(1, 1, 28, 28)).shape` →
`torch.Size([1, 10])` — one logit per digit class.

---

### 3. Max Pooling — `p03`

**What it is:** Downsample by keeping only the max of each small
window (usually 2×2). 4×4 → 2×2. You lose exact position but keep
the strongest signal — "was this feature detected nearby?" matters
more than "at which exact pixel?"

**Why it exists:** Convolution is position-sensitive — the same
edge at pixel 10 vs. pixel 12 produces a response in a different
cell. Pooling was introduced to keep the strongest response while
discarding exact location (translation invariance) — and to halve
the spatial size so deeper layers cost less.

**Where it's used:** Between conv blocks in every classic CNN.
(Modern nets sometimes use strided convs instead, but pooling is
still everywhere.) A cat is a cat whether its ear is at pixel 10
or pixel 12 — pooling is what teaches the network that.

**What goes wrong without it:** Without downsampling, feature maps
stay full-size → later layers and the final Linear get huge. Worse,
the model overfits exact pixel positions — a 1-pixel shift of a
digit can flip the prediction. Practical notes: max pooling has NO
learnable parameters (it's a fixed operation), and `MaxPool2d(2)`
means a 2×2 window with stride 2 (non-overlapping), not "2 pools."

**Worked example:**
```
image (4×4):            2×2 max pooling:
[[1,  3,  2,  4],       block [1,3; 5,6] → max = 6
 [5,  6,  7,  8],       block [2,4; 7,8] → max = 8
 [9, 10, 11, 12],       block [9,10;13,14] → max = 14
 [13,14, 15, 16]]       block [11,12;15,16] → max = 16

output: [[6, 8],
         [14, 16]]      — 4×4 → 2×2, strongest values survive
```

**Code:**
```python
def max_pool(img):
    H, W = img.shape
    out = np.zeros((H//2, W//2))
    for i in range(0, H, 2):
        for j in range(0, W, 2):
            out[i//2, j//2] = img[i:i+2, j:j+2].max()
    return out
```

**Expected output:** `max_pool(img)` on the worked-example 4×4 →
`[[ 6.,  8.], [14., 16.]]`.

---

## Medium

### 4. Training a CNN on CIFAR-10 — `p01`

**What it is:** CIFAR-10 = 60,000 color images (32×32×3) in 10
classes (plane, car, cat, ...). Train the same CNN pattern on it —
the training loop is IDENTICAL to level-08; only the input is now
3-channel images instead of flat vectors.

**Why it exists:** MNIST is too easy — clean, grayscale, centered
digits. CIFAR-10 exists as the "real images" benchmark: color,
clutter, varied poses. It's where you discover that tricks like
BatchNorm, dropout, and augmentation aren't optional anymore.

**Where it's used:** The standard small-scale benchmark for
natural-image classification. The jump from ~97% on MNIST to ~65%
on CIFAR teaches the key lesson: natural images are much harder.

**What goes wrong without it:** CIFAR images are 3-channel — the
first conv must be `Conv2d(3, ...)`, not `Conv2d(1, ...)`. MNIST=1
channel, CIFAR=3. Getting this wrong is the #1 shape error. Also:
skip `Normalize` and pixel stats drift far from what the model
expects; expect MNIST-level accuracy and ~0.65 will look like
failure — it's actually the CNN learning real features (random
guessing is 0.10).

**Worked example:**
```
Input batch: [64, 3, 32, 32]  (64 color images)
Conv(3→16) → ReLU → Pool:   [64,16,16,16]
Conv(16→32) → ReLU → Pool:  [64,32, 8, 8]
Flatten:                    [64, 2048]    (32×8×8)
Linear → 10 logits → CrossEntropyLoss → backward → step

After 3 epochs: test accuracy ≈ 0.60–0.65
(vs. ~0.10 for random guessing — the CNN learned real features;
 more epochs/augmentation pushes it into the 0.8s)
```

**Code:**
```python
from torchvision import datasets, transforms
tf = transforms.Compose([transforms.ToTensor(),
                         transforms.Normalize((0.5,)*3, (0.5,)*3)])
ds = datasets.CIFAR10('./data', train=True, download=True, transform=tf)
```

**Expected output:** `len(ds)` → 50000; each item is a `[3, 32,
32]` tensor plus a label 0-9. After 3 epochs, test accuracy ≈
0.60–0.65.

---

### 5. Batch Normalization — `p02`

**What it is:** A layer that re-normalizes each activation to
mean≈0, std≈1 using the current mini-batch's statistics, then
applies a learned scale/shift. Insert between Linear and ReLU.

**Why it exists:** As weights update, each layer's output
distribution shifts — the next layer keeps chasing a moving target
("internal covariate shift"). BatchNorm was invented to pin
activations to a stable range so deep nets train faster and
tolerate higher learning rates.

**Where it's used:** Baked into nearly every modern architecture,
sitting between Linear/Conv and the activation. It enabled much
deeper networks to train at all.

**What goes wrong without it:** Deep nets without BN train slowly
or diverge when you raise the learning rate — wild activations
saturate sigmoid/ReLU units. Order matters: it's `Linear →
BatchNorm → ReLU` (norm before the nonlinearity). BatchNorm1d's
argument is the FEATURE count (64), not batch size. And at eval
time it must use stored running stats — that's another reason
`model.eval()` matters; in train mode with batch size 1 the batch
std is ~0 and normalization blows up.

**Worked example:**
```
A hidden layer's outputs across a batch, mid-training:
  activations = [120, -85, 300, -210, 45, ...]   ← wild spread
  (each layer's output distribution shifts as weights change —
   the next layer keeps chasing a moving target)

BatchNorm1d per batch:
  mean ≈ 14, std ≈ 180
  120 → (120-14)/180 ≈ 0.59
  -85 → (-85-14)/180 ≈ -0.55
  → all values land near [-2, +2] — stable, sane inputs for ReLU

Result: models converge faster, higher lr becomes usable.
```

**Code:**
```python
nn.Sequential(
    nn.Linear(10, 64),
    nn.BatchNorm1d(64),     # normalize the 64 activations
    nn.ReLU(),
    nn.Linear(64, 2)
)
```

**Expected output:** Activations like `[120, -85, 300, ...]` come
out as ≈ `[0.59, -0.55, 1.59, ...]` — values clustered around 0
with std ≈ 1 — and training converges in fewer epochs than the
same net without BN.

---

### 6. Dropout — `p03`

**What it is:** During training, randomly zero a fraction of
activations each forward pass (`Dropout(0.5)` = kill half). The
network can't depend on any single neuron, so it learns redundant,
robust features. At eval time, all neurons stay on.

**Why it exists:** Big networks memorize training data instead of
generalizing (overfitting). Dropout was invented (Srivastava et
al., 2014) to break "co-adaptation" — no neuron can rely on any
other specific neuron being present, so the net is forced to learn
features that work in many combinations. It's ensemble learning in
disguise: each batch trains a different random sub-network.

**Where it's used:** Mostly on the big dense layers of MLPs and
CNN classifier heads — anywhere overfitting shows up. The
signature that it's working: train accuracy might dip while TEST
accuracy rises.

**What goes wrong without it:** The model memorizes the training
set → train acc 99%, test acc 65%. But misuse is its own trap:
dropout runs ONLY in train mode — forget `model.eval()` at
inference and activations get randomly zeroed → different
prediction every call on the SAME input. And 0.5 on every layer is
too much for small nets — it's typically on the big dense layers.

**Worked example:**
```
Hidden activations: [0.8, 0.0, 1.2, 0.5, 0.9, 0.3, 1.1, 0.7]

Training forward pass with Dropout(0.5), one random mask:
  mask ~ [1, 0, 1, 0, 0, 1, 1, 0]
  out  = [0.8·2, 0, 1.2·2, 0, 0, 0.3·2, 1.1·2, 0]
       = [1.6, 0, 2.4, 0, 0, 0.6, 2.2, 0]
  (survivors scaled ×2 so expected sum stays constant)

Next pass gets a DIFFERENT random mask → different sub-network.
Model.eval(): dropout OFF → all 8 activations used, no scaling.
```

**Code:**
```python
nn.Sequential(nn.Linear(20,64), nn.ReLU(),
              nn.Dropout(0.5),        # active only in .train() mode
              nn.Linear(64,2))
model.train()   # dropout on     model.eval()   # dropout off
```

**Expected output:** With `Dropout(0.5)` in train mode, a forward
pass on `[0.8, 0.0, 1.2, 0.5, 0.9, 0.3, 1.1, 0.7]` returns roughly
half the entries zeroed and survivors ×2 — e.g.
`[1.6, 0, 2.4, 0, 0, 0.6, 2.2, 0]` (mask is random each call).
In eval mode the same input returns unchanged.

---

## Hard

### 7. Transfer Learning — `p01`

**What it is:** Don't train a vision model from scratch — start
from one already trained on millions of images (ImageNet). Its
early layers already detect edges/textures/shapes; you only
replace the final classifier layer with one for YOUR classes and
(optionally) freeze everything else.

**Why it exists:** Training a competitive vision model from
scratch needs millions of labeled images and days of GPU time —
almost nobody has that. Transfer learning exists because features
learned on ImageNet (edges, textures, shapes) generalize: you get
~90% of the performance with ~1% of the data.

**Where it's used:** Almost all applied vision work — fine-tune a
pretrained backbone rather than training your own. The same idea
powers NLP: fine-tune a pretrained LLM instead of training from
scratch.

**What goes wrong without it:** Train ResNet18 from random init on
5K images → massive overfit and ~40-50% accuracy where transfer
gets 80%+. Practical traps: `model.fc.in_features` reads the OLD
layer's input size (512 for ResNet18) — use it instead of
hardcoding; freezing uses `requires_grad = False` on PARAMETERS,
not on layers — and if you freeze the new head too, nothing
trains.

**Worked example:**
```python
from torchvision import models
model = models.resnet18(weights=None)   # or pretrained weights
# ResNet18 ends in: ...avgpool → Linear(512, 1000) for ImageNet's 1000 classes

model.fc = nn.Linear(model.fc.in_features, 10)   # swap: 512 → YOUR 10 classes

# Optional: freeze the backbone — only train the new head
for p in model.parameters():
    p.requires_grad = False
for p in model.fc.parameters():
    p.requires_grad = True

# Train on CIFAR-10, 2 epochs → ~0.5-0.7 even with random backbone
# weights (the architecture alone helps); pretrained → much higher.
```

**Code:**
```python
model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, num_classes)
```

**Expected output:** After the swap, `model.fc` is
`Linear(in_features=512, out_features=10, bias=True)` and
`model(torch.randn(1,3,224,224)).shape` → `torch.Size([1, 10])`.
~2 epochs on CIFAR-10 → ≈0.5-0.7 test accuracy.

---

### 8. Data Augmentation — `p02`

**What it is:** Manufacture new training examples by randomly
transforming existing ones — flips, rotations, crops, color
jitter. Each epoch the model sees slightly different images, so it
can't memorize the training set and must learn robust features.

**Why it exists:** Labeled data is the bottleneck in applied
vision — collecting and labeling more is expensive. Augmentation
exists as the cheapest way to multiply effective dataset size:
each random transform is a new sample for free.

**Where it's used:** Standard practice in every vision training
pipeline — it's a big part of why CIFAR models reach 85%+ instead
of overfitting at 65%.

**What goes wrong without it:** Without augmentation the model
overfits by ~epoch 10 — train accuracy climbs while test accuracy
plateaus ~65%. Two misuse traps: augment the TRAINING set only —
test data must stay clean (just ToTensor+Normalize) or you're
evaluating on distorted images and the score is meaningless. And
pick transforms that preserve the label: flipping a cat is still a
cat, but flipping a "6" gives a "9" — a wrong label injected into
training.

**Worked example:**
```
transforms.Compose([
    RandomHorizontalFlip(),      # 50% chance: mirror the image
    RandomRotation(15),          # rotate ±15°
    RandomCrop(32, padding=4),   # pad to 40, crop random 32×32
    ColorJitter(0.2),            # wiggle brightness/contrast
    ToTensor(),                  # PIL image → [3,32,32] tensor
    Normalize(...)               # mean/std scaling
])

Epoch 1 sees: cat flipped left, rotated +8°, shifted up
Epoch 2 sees: SAME cat, unflipped, rotated -3°, brighter
→ effectively a bigger, more varied dataset for free
```

**Code:**
```python
from torchvision import transforms
tf = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomCrop(32, padding=4),
    transforms.ToTensor(),
])
```

**Expected output:** Applying `tf` to a 32×32 PIL image returns a
`torch.Size([3, 32, 32])` tensor — the dataset length is
unchanged, but each epoch yields a differently-transformed version
of every image.

---

### 9. Custom nn.Module — `p03`

**What it is:** `nn.Sequential` only does a straight pipeline. Real
models need custom logic — skip connections, multiple outputs,
branching. Subclass `nn.Module`: register layers in `__init__`,
write the data flow in `forward()`.

**Why it exists:** Frameworks can't ship a `nn.Sequential` entry
for every architecture ever invented — ResNet's skip connections,
multi-head outputs, attention all need arbitrary data flow.
`nn.Module` exists as the extension point: `__init__` defines WHAT
exists; `forward` defines HOW data flows.

**Where it's used:** Every real architecture is a custom Module —
once you can write this, any architecture from a paper is
reachable.

**What goes wrong without it:** Forget `super().__init__()` and
your layers never register — `model.parameters()` returns EMPTY
and training updates nothing (silent failure — no error, just a
model that never learns). And you never call `model.forward(x)` —
call `model(x)`; the `__call__` machinery handles hooks and modes
for you.

**Worked example:**
```python
class CustomCNN(nn.Module):
    def __init__(self):
        super().__init__()                    # REQUIRED — registers params
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2)
        self.fc1 = nn.Linear(64*8*8, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):                     # [B,3,32,32]
        x = self.pool(F.relu(self.conv1(x)))  # → [B,32,16,16]
        x = self.pool(F.relu(self.conv2(x)))  # → [B,64, 8, 8]
        x = x.view(x.size(0), -1)             # → [B, 4096]
        return self.fc2(F.relu(self.fc1(x)))  # → [B, 10]

model = CustomCNN()
model(torch.randn(4,3,32,32))          # → [4,10]
sum(p.numel() for p in model.parameters())   # ≈ 545,098 params
```

**Code:**
```python
def count_params(model):
    return sum(p.numel() for p in model.parameters())
x = x.view(x.size(0), -1)   # flatten keeping batch dim
```

**Expected output:** `model(torch.randn(4,3,32,32)).shape` →
`torch.Size([4, 10])`; `count_params(model)` → ≈ 545,098.

---

## Done with concepts? → Try `easy/p01-convolution.py`
