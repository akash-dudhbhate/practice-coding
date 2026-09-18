# Level 08 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept explains:
What it is · Why it exists · Where it's used · What goes wrong without it ·
worked example · code · expected output.

---

## Easy

### 1. The Perceptron — `p01`

**What it is:** The simplest possible neuron: take a weighted sum
of inputs, add a bias, and output 1 if the result is positive,
else 0. `output = step(x·w + b)`. It learns by a dead-simple rule:
when the prediction is wrong, nudge the weights toward the input.

**Why it exists:** Before the perceptron (1957), "learning a rule
from data" had no concrete algorithm — you hand-coded every
decision boundary. The perceptron was the first machine that could
*find* a separating boundary by trial and error: wrong answer →
adjust weights, right answer → leave them alone.

**Where it's used:** Every neuron in every modern network is this
exact pattern (dot product + bias + a decision function) — deep
learning just chains millions of them. The perceptron update rule
is the great-grandparent of gradient descent.

**What goes wrong without it:** Without the update rule the
weights never change — the model can't learn, period. Without a
bias, the boundary is forced through the origin and can't even
fit OR's offset. And a single perceptron can only draw ONE
straight decision boundary: it solves OR and AND but famously
CANNOT solve XOR — that limitation (medium/p01) is why hidden
layers exist.

**Worked example:** Learning the OR gate: `y=[0,1,1,1]` for
`X=[[0,0],[0,1],[1,0],[1,1]]`. Start w=[0.1,0.1], b=0.0:
```
Epoch 1:
  x=[0,0]: x·w+b = 0.0 → pred 0, y=0 ✓ (no update)
  x=[0,1]: x·w+b = 0.1 → pred 1, y=1 ✓
  x=[1,0]: x·w+b = 0.1 → pred 1, y=1 ✓
  x=[1,1]: x·w+b = 0.2 → pred 1, y=1 ✓
Already solved in epoch 1 — the update rule only fires on errors.

If instead we trained AND (y=[0,0,0,1]):
  x=[0,1]: x·w+b=0.1 → pred 1, y=0 ✗ → w -= x → w=[0.1,0.0], b -= 0.1
  The weights shrink until [0,1] and [1,0] no longer fire alone.
```

**Code:**
```python
import numpy as np
pred = 1 if np.dot(x, w) + b > 0 else 0
if y == 1 and pred == 0:   # missed a positive → push weights up
    w += x; b += 0.1
elif y == 0 and pred == 1: # false alarm → push weights down
    w -= x; b -= 0.1
```

**Expected output:** On OR data with w=[0.1,0.1], b=0.0, all 4
predictions are already correct in epoch 1 — `[0, 1, 1, 1]` — so
no updates fire. On AND data the same starting weights mislabel
`[0,1]` and `[1,0]`; updates shrink w until only `[1,1]` fires.

---

### 2. Activation Functions — `p02`

**What it is:** A nonlinear function applied after each neuron's
weighted sum. Without it, stacking layers is pointless — a stack
of linear layers collapses into a single linear layer.
Activations are what let networks learn curves.

**Why it exists:** A deep network's whole promise is "more layers
= more power." But two linear layers compose into one:
`y = (x·W1)·W2 = x·(W1·W2)` — still a single linear map!
Activations were introduced specifically to break that collapse so
depth actually adds expressive power.

**Where it's used:** ReLU is the default hidden activation in
almost every modern network (cheap, trains well). Sigmoid appears
on binary outputs; softmax on multi-class outputs; tanh inside
RNNs. The choice of activation literally shapes what your network
can express.

**What goes wrong without it:** Stack 10 linear layers with no
activation → you get the power of ONE layer; a 10-layer "deep" net
can't fit XOR or any curve. And misuse hurts too: ReLU "kills"
negative inputs — and their gradients too (dead neurons). That's
fine for hidden layers, but never put ReLU on the final regression
output — it can never predict a negative number.

**Worked example:**
```
sigmoid(0)   = 1/(1+e^0)   = 0.5     → squashes to (0,1), like a probability
sigmoid(10)  ≈ 0.99995                → big input ≈ 1
relu(-2)     = max(0, -2)  = 0        → negatives die
relu(3)      = max(0, 3)   = 3        → positives pass through
tanh(0)      = 0.0                    → like sigmoid but (-1,1)
```

Why it matters: two linear layers `y = (x·W1)·W2` = `x·(W1·W2)` —
still one linear map! With ReLU between them, the composition is
nonlinear and can carve any shape.

**Code:**
```python
import numpy as np
def sigmoid(z): return 1 / (1 + np.exp(-z))
def relu(z):    return np.maximum(0, z)
def tanh(z):    return np.tanh(z)
```

**Expected output:**
```
sigmoid(0.0)   → 0.5
sigmoid(10.0)  → 0.9999546021312976
relu(np.array([-2, 3])) → array([0, 3])
tanh(0.0)      → 0.0
```

---

### 3. PyTorch Tensors — `p03`

**What it is:** PyTorch's core data type — think NumPy array that
can also run on a GPU and automatically track gradients.
`requires_grad=True` tells torch to record every operation;
`.backward()` then computes all gradients via the chain rule.

**Why it exists:** Training a neural net means computing
derivatives of the loss w.r.t. EVERY weight — thousands to
billions of them. Deriving those by hand doesn't scale, and NumPy
can't use GPUs or track gradients. Tensors exist to solve both:
GPU-resident arrays that record their own computation graph.

**Where it's used:** Autograd is WHY deep learning frameworks
exist. Everything in levels 08-09 is tensors flowing through
layers with gradients flowing back — training loops, backprop,
optimizer updates.

**What goes wrong without it:** Without autograd you'd write a
manual derivative for every weight — fine for 2→2→1 (see hard/p01),
impossible for a 100-layer network. Also: `requires_grad` only
works on FLOAT tensors — `torch.tensor([1,2,3], requires_grad=True)`
raises `RuntimeError: only Tensors of floating point dtype can
require gradients` (what would d(integer)/dw even be?). And `*` is
element-wise multiply; `@`/`torch.dot`/`torch.matmul` is real
multiplication — same trap as NumPy.

**Worked example:**
```python
import torch
a = torch.tensor([1., 2., 3.], requires_grad=True)
b = torch.tensor([4., 5., 6.])

a + b          # tensor([5., 7., 9.])
a * b          # tensor([ 4., 10., 18.])  element-wise
torch.dot(a, b) # 1*4 + 2*5 + 3*6 = tensor(32.)

# The magic: gradients for free
loss = torch.dot(a, b)     # scalar
loss.backward()
print(a.grad)   # tensor([4., 5., 6.]) = d(dot)/da = b ✓
```

**Code:**
```python
x = torch.tensor(np_array, dtype=torch.float32)  # numpy → tensor
y = torch.tensor(labels, dtype=torch.long)       # class labels need long
```

**Expected output:**
```
a + b           → tensor([5., 7., 9.])
a * b           → tensor([ 4., 10., 18.])
torch.dot(a, b) → tensor(32.)
loss.backward() → a.grad = tensor([4., 5., 6.])  (= b)
```

---

## Medium

### 4. XOR & Why Hidden Layers Exist — `p01`

**What it is:** XOR outputs 1 when inputs differ: `[0,0]→0, [0,1]→1,
[1,0]→1, [1,1]→0`. No single straight line separates the 1s from
the 0s — a lone perceptron provably fails. A hidden layer
(2→2→1) can bend the boundary and solve it.

**Why it exists:** In 1969 Minsky & Papert proved perceptrons
can't do XOR — and neural-net research nearly died. Hidden layers
were the fix: an intermediate layer warps the input space so
classes that weren't linearly separable become separable. That
insight (hidden layers + backprop) IS deep learning.

**Where it's used:** Every modern architecture is this idea scaled
up — more layers = more space-warping. Any problem whose classes
aren't separable by one straight boundary (images, audio, language)
needs hidden layers.

**What goes wrong without it:** Train a lone perceptron on XOR and
the update rule cycles forever — errors never reach zero, the loss
never falls, because no straight line can possibly fit. Note the
flip side too: "more layers" isn't automatically better — XOR
needs exactly ONE hidden layer. Depth adds power but also training
difficulty; add it because the problem needs it.

**Worked example:**
```
The 4 XOR points in a square:
  (0,1)=1    (1,1)=0
  (0,0)=0    (1,0)=1
1s are on diagonal corners — no line separates them. ✗ perceptron

A 2→2→1 network (sigmoid everywhere), trained 1000 epochs:
  h = sigmoid(X @ W1 + b1)      # hidden layer: 2 new "features"
  out = sigmoid(h @ W2 + b2)    # output layer on top of h

Result: preds ≈ [0.05, 0.95, 0.95, 0.04], loss → ~0.002
The hidden layer warps the space so the classes DO separate.
```

**Code:**
```python
h   = sigmoid(X @ W1 + b1)        # forward: hidden
out = sigmoid(h @ W2 + b2)        # forward: output
# backward: adjust W2,b2 from output error, then W1,b1 through the chain
```

**Expected output:** After ~1000 epochs of training on XOR,
`out ≈ [[0.05], [0.95], [0.95], [0.04]]` — matching `y=[0,1,1,0]`
within ~0.05 — and loss drops to ≈ 0.002.

---

### 5. The PyTorch Training Loop — `p02`

**What it is:** The canonical 5-step loop every PyTorch model
uses. Memorize it once, use it forever:
1. forward pass → 2. compute loss → 3. zero gradients →
4. backward pass → 5. optimizer step.

**Why it exists:** Gradient descent is inherently a cycle: measure
error, find the direction that reduces it, take a step, repeat.
PyTorch keeps the steps explicit (instead of hiding them in one
`fit()` call) so you can customize each stage — that's the whole
point of a framework over a fixed recipe.

**Where it's used:** This exact loop trains everything — MNIST
nets, CNNs, transformers. The details change (batches, schedulers,
mixed precision) but the skeleton never does. It's THE PyTorch
pattern.

**What goes wrong without it:** Forgetting `optimizer.zero_grad()`
is THE beginner bug — PyTorch ACCUMULATES gradients across
`backward()` calls, so without zeroing, each step uses stale
summed gradients and training goes haywire (loss bounces or
explodes). Skip `backward()` and weights never move; skip `step()`
and you compute gradients but never apply them — loss sits flat.

**Worked example:** Learn `y = 3x + 2` from noisy data:
```python
model = nn.Linear(1, 1)                      # y = w·x + b
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    pred = model(X)                          # 1. forward
    loss = criterion(pred, y)                # 2. how wrong?
    optimizer.zero_grad()                    # 3. clear old grads
    loss.backward()                          # 4. compute new grads
    optimizer.step()                         # 5. w -= lr·grad

# After training: model.weight ≈ 3.0, model.bias ≈ 2.0  ✓
```

**Code:**
```python
import torch.nn as nn, torch.optim as optim
model.weight.item(), model.bias.item()   # read learned params
```

**Expected output:** After ~100 epochs, `model.weight.item()` ≈
3.0 and `model.bias.item()` ≈ 2.0 (recovering `y = 3x + 2` up to
the noise), and the printed loss falls from ~10+ to near 0.

---

### 6. MLP Classifier (nn.Sequential + CrossEntropy) — `p03`

**What it is:** MLP = Multi-Layer Perceptron: stack Linear layers
with activations between them. For classification, the final layer
outputs raw scores ("logits") — one per class — and
CrossEntropyLoss turns them into a probability distribution.

**Why it exists:** Flat feature vectors have no spatial structure,
so convolutions don't apply — the MLP is the general-purpose
network for tabular data. CrossEntropyLoss exists because "argmax
of logits" isn't differentiable: it applies softmax internally and
penalizes the distance between predicted and true class
distributions.

**Where it's used:** This is the "default neural network" —
tabular classification, the base case before CNNs (level-09) or
anything fancier. Adam is the default optimizer (adaptive learning
rates per parameter — usually beats plain SGD).

**What goes wrong without it:** CrossEntropyLoss wants raw LOGITS
and class INDICES — if you softmax yourself, you double-softmax
and gradients break; if you one-hot encode y, you get a dtype
error (it expects `y=[0,1,1,0,...]` of dtype long). Also: reading
predictions requires `argmax` — the raw logits themselves aren't
labels.

**Worked example:**
```python
model = nn.Sequential(
    nn.Linear(5, 10),    # 5 features → 10 hidden units
    nn.ReLU(),
    nn.Linear(10, 2)     # 10 hidden → 2 class logits
)
# Input [x1..x5] → logits e.g. [2.1, -0.7]
# CrossEntropyLoss internally: softmax → [0.94, 0.06] → compare to true class

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)
# 200 epochs on make_classification data → ~0.95 test accuracy
```

**Code:**
```python
X_t = torch.tensor(X, dtype=torch.float32)
y_t = torch.tensor(y, dtype=torch.long)      # class INDICES, not one-hot!
preds = model(X_t).argmax(dim=1)             # highest logit wins
```

**Expected output:** `model(X_t)` returns raw logits like
`tensor([[ 2.1, -0.7], ...])`; `argmax(dim=1)` → `tensor([0, ...])`.
After ~200 epochs on make_classification data, test accuracy ≈
0.95.

---

## Hard

### 7. Manual Backpropagation — `p01`

**What it is:** Compute every gradient by hand with the chain rule —
what `.backward()` does for you, exposed. For each weight, the
gradient answers: "if I nudge this weight, how much does the loss
change?" Then update: `w -= lr × gradient`.

**Why it exists:** Someone has to know how to assign "blame" for
the loss to each of millions of weights. Doing it numerically
(wiggle each weight, re-run the network) costs 2 forward passes
PER WEIGHT — hopeless at scale. Backprop computes all gradients in
ONE backward pass by reusing shared error terms through the chain
rule.

**Where it's used:** You'll never write this in production —
autograd does it — but understanding it explains everything:
vanishing gradients, why ReLU helps, what `.backward()` actually
computes. This is the "how does a car engine work" lesson for ML.

**What goes wrong without it:** Without the chain rule, deeper
layers get no usable error signal — the error must flow BACKWARD
through the SAME weights it used going forward (`delta2 @ W2.T`).
Each layer's gradient is error × local-derivative × input — forget
any factor and the network learns nothing (loss just sits there).
And with sigmoid everywhere, gradients shrink layer by layer
(vanishing gradients) — the reason ReLU took over.

**Worked example:** 2→2→1 net on XOR, one forward+backward trace:
```
Forward:
  h   = sigmoid(X @ W1 + b1)
  out = sigmoid(h @ W2 + b2)
  loss = mean((out - y)²)

Backward (chain rule, output→input):
  d_out   = (out - y)                        # d(MSE)/d(out), up to const
  delta2  = d_out * sigmoid'(out)            # sigmoid'(x)=x(1-x)
  dL/dW2  = h.T @ delta2                     # ← update W2, b2 with this
  d_h     = delta2 @ W2.T                    # error flows back through W2
  delta1  = d_h * sigmoid'(h)
  dL/dW1  = X.T @ delta1                     # ← update W1, b1 with this

Each weight's gradient = (error that reached it) × (its input).
5000 epochs, lr=0.5 → loss ≈ 0.0005, XOR solved.
```

**Code:**
```python
def sigmoid(z): return 1/(1+np.exp(-z))
def d_sigmoid(s): return s*(1-s)     # takes the ACTIVATED value
W2 -= lr * (h.T @ delta2);  W1 -= lr * (X.T @ delta1)
```

**Expected output:** After 5000 epochs at lr=0.5, the loss falls
from ~0.25 (random guessing) to ≈ 0.0005, and `out` rounds to
`[0, 1, 1, 0]` — XOR solved.

---

### 8. Full Training Loop: DataLoader + train/eval modes — `p02`

**What it is:** Real training feeds data in mini-batches (not all
at once), and models behave differently when training vs.
evaluating — `model.train()`/`model.eval()` and `torch.no_grad()`
manage that.

**Why it exists:** Two problems: (1) datasets bigger than memory
can't be fed in one forward pass — mini-batches fix that AND the
noisy gradient estimates help escape bad minima; (2) layers like
dropout and batchnorm NEED different behavior during training vs.
inference, so PyTorch gives the model a mode flag.

**Where it's used:** Every real training pipeline uses DataLoader
batching; every production inference wraps prediction in
`model.eval()` + `torch.no_grad()`.

**What goes wrong without it:** Train on the full dataset every
step → slow epochs and memory blowups on big data. Evaluate in
`train()` mode → dropout keeps randomly zeroing units and
predictions change run to run (flaky, unreproducible accuracy).
Evaluate without `no_grad()` → PyTorch builds a gradient graph it
never uses → memory grows until OOM. Note: `model.eval()` alone
does NOT stop gradient tracking — it only changes layer behavior;
you need BOTH. And `train()`/`eval()` don't return anything —
they set a flag in place.

**Worked example:**
```python
ds = TensorDataset(X_t, y_t)
dl = DataLoader(ds, batch_size=32, shuffle=True)
# 400 samples → ~13 batches of 32 per epoch

for epoch in range(50):
    model.train()                          # dropout/BN ON, grads tracked
    for xb, yb in dl:
        loss = criterion(model(xb), yb)
        optimizer.zero_grad(); loss.backward(); optimizer.step()

    model.eval()                           # dropout/BN OFF
    with torch.no_grad():                  # don't build grad graph
        acc = (model(X_val).argmax(1) == y_val).float().mean()

# train loss falls 0.x → 0.0x; val acc reaches ~0.95+
```

**Code:**
```python
from torch.utils.data import TensorDataset, DataLoader
with torch.no_grad():               # inside = pure inference
    logits = model(X_test)
```

**Expected output:** 400 samples at batch_size=32 → 13 batches per
epoch. Train loss falls from ~0.x to ~0.0x over 50 epochs;
`acc` (a 0-dim tensor) reaches ≈ `tensor(0.95)` on validation.

---

### 9. MNIST Digit Classification — `p03`

**What it is:** The "hello world" of deep learning: 70,000
handwritten digits, each a 28×28 grayscale image, labels 0-9.
`torchvision.datasets.MNIST` downloads it for you. An MLP that
flattens each image into 784 pixels hits ~97% in a few epochs.

**Why it exists:** You need a standard, real dataset to sanity-
check the entire pipeline end-to-end — MNIST is small enough to
train in minutes but real enough to prove a network actually
learned. It became the shared benchmark every framework and paper
uses as a first test.

**Where it's used:** The standard sanity check — every framework
tutorial, every new-idea paper starts here. It proves the MLP
pipeline end-to-end on real data: download → DataLoader → train →
evaluate. Level-09 swaps the MLP for a CNN and pushes past 99%.

**What goes wrong without it:** Images arrive as `[batch, 1, 28,
28]` — a Linear layer needs `[batch, 784]`. Forgetting to flatten
(`x.view(-1, 784)`) gives a shape mismatch error. `ToTensor()`
scales pixels to [0.0, 1.0] — feed raw 0-255 values and gradients
explode. Also `download=True` needs internet the first run.

**Worked example:**
```
One image: 28×28 grid of pixel values 0-255
ToTensor() → tensor[1, 28, 28], scaled to [0.0, 1.0]
Flatten    → vector of 784 numbers

Model: Linear(784→128) → ReLU → Linear(128→10)
       784 inputs (pixels) → 10 outputs (digit logits)

Data: 60,000 train / 10,000 test
3 epochs, Adam(0.001), CrossEntropyLoss → test accuracy ≈ 0.97

Meaning: of 10,000 handwritten digits the model has NEVER seen,
it reads ~9,700 correctly.
```

**Code:**
```python
from torchvision import datasets, transforms
train = datasets.MNIST('./data', train=True, download=True,
                       transform=transforms.ToTensor())
# model(x.view(-1, 784)) — flatten each batch before Linear
```

**Expected output:** `len(train)` → 60000; each item is a
`[1, 28, 28]` tensor plus a label 0-9. After ~3 epochs with
Adam(0.001) and CrossEntropyLoss, test accuracy ≈ 0.97 (~9,700 of
10,000 unseen digits read correctly).

---

## Done with concepts? → Try `easy/p01-perceptron.py`
