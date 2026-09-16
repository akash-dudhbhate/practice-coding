# Level 08 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

---

## Easy

### 1. The Perceptron — `p01`

**What it is:** The simplest possible neuron: take a weighted sum
of inputs, add a bias, and output 1 if the result is positive,
else 0. `output = step(x·w + b)`. It learns by a dead-simple rule:
when the prediction is wrong, nudge the weights toward the input.

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

**Why ML cares:** Every neuron in every network is this pattern
(dot product + bias + a decision function) — deep learning just
chains millions of them. The perceptron update rule is the great-
grandparent of gradient descent.

**Code:**
```python
import numpy as np
pred = 1 if np.dot(x, w) + b > 0 else 0
if y == 1 and pred == 0:   # missed a positive → push weights up
    w += x; b += 0.1
elif y == 0 and pred == 1: # false alarm → push weights down
    w -= x; b -= 0.1
```

**Common confusion:** A perceptron can only draw ONE straight
decision boundary. It solves OR and AND but famously CANNOT solve
XOR — that limitation (next level: medium/p01) is why hidden
layers exist.

---

### 2. Activation Functions — `p02`

**What it is:** A nonlinear function applied after each neuron's
weighted sum. Without it, stacking layers is pointless — a stack
of linear layers collapses into a single linear layer.
Activations are what let networks learn curves.

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

**Why ML cares:** ReLU is the default hidden activation in almost
every modern network (cheap, trains well). Sigmoid appears on
binary outputs; softmax on multi-class outputs. The choice of
activation literally shapes what your network can express.

**Code:**
```python
import numpy as np
def sigmoid(z): return 1 / (1 + np.exp(-z))
def relu(z):    return np.maximum(0, z)
def tanh(z):    return np.tanh(z)
```

**Common confusion:** ReLU "kills" negative inputs — and their
gradients too (dead neurons). That's fine for hidden layers, but
never put ReLU on the final regression output — it can never
predict a negative number.

---

### 3. PyTorch Tensors — `p03`

**What it is:** PyTorch's core data type — think NumPy array that
can also run on a GPU and automatically track gradients.
`requires_grad=True` tells torch to record every operation;
`.backward()` then computes all gradients via the chain rule.

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

**Why ML cares:** Autograd is WHY deep learning frameworks exist.
Manually deriving gradients for a 100-layer network is impossible;
`.backward()` does it in one line. Everything in levels 08-09 is
tensors flowing through layers with gradients flowing back.

**Code:**
```python
x = torch.tensor(np_array, dtype=torch.float32)  # numpy → tensor
y = torch.tensor(labels, dtype=torch.long)       # class labels need long
```

**Common confusion:** `requires_grad` only works on FLOAT tensors
(integers can't have gradients — what would d(integer)/dw even be?).
And `*` is element-wise multiply; `@`/`torch.dot`/`torch.matmul` is
real multiplication — same trap as NumPy.

---

## Medium

### 4. XOR & Why Hidden Layers Exist — `p01`

**What it is:** XOR outputs 1 when inputs differ: `[0,0]→0, [0,1]→1,
[1,0]→1, [1,1]→0`. No single straight line separates the 1s from
the 0s — a lone perceptron provably fails. A hidden layer
(2→2→1) can bend the boundary and solve it.

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

**Why ML cares:** This 1969 problem ("perceptrons can't do XOR")
nearly killed neural-net research — the fix (hidden layers +
backprop) IS deep learning. Every modern architecture is this
idea scaled up: more layers = more space-warping.

**Code:**
```python
h   = sigmoid(X @ W1 + b1)        # forward: hidden
out = sigmoid(h @ W2 + b2)        # forward: output
# backward: adjust W2,b2 from output error, then W1,b1 through the chain
```

**Common confusion:** "More layers" isn't automatically better —
XOR needs exactly ONE hidden layer. Depth adds power but also
training difficulty; add it because the problem needs it.

---

### 5. The PyTorch Training Loop — `p02`

**What it is:** The canonical 5-step loop every PyTorch model
uses. Memorize it once, use it forever:
1. forward pass → 2. compute loss → 3. zero gradients →
4. backward pass → 5. optimizer step.

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

**Why ML cares:** This exact loop trains everything — MNIST nets,
CNNs, transformers. The details change (batches, schedulers, mixed
precision) but the skeleton never does. It's THE PyTorch pattern.

**Code:**
```python
import torch.nn as nn, torch.optim as optim
model.weight.item(), model.bias.item()   # read learned params
```

**Common confusion:** Forgetting `optimizer.zero_grad()` is THE
beginner bug — PyTorch ACCUMULATES gradients across backward()
calls, so without zeroing, each step uses stale summed gradients
and training goes haywire.

---

### 6. MLP Classifier (nn.Sequential + CrossEntropy) — `p03`

**What it is:** MLP = Multi-Layer Perceptron: stack Linear layers
with activations between them. For classification, the final layer
outputs raw scores ("logits") — one per class — and
CrossEntropyLoss turns them into a probability distribution.

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

**Why ML cares:** This is the "default neural network" — tabular
classification, the base case before CNNs (level-09) or anything
fancier. Adam is the default optimizer (adaptive learning rates
per parameter — usually beats plain SGD).

**Code:**
```python
X_t = torch.tensor(X, dtype=torch.float32)
y_t = torch.tensor(y, dtype=torch.long)      # class INDICES, not one-hot!
preds = model(X_t).argmax(dim=1)             # highest logit wins
```

**Common confusion:** CrossEntropyLoss wants raw LOGITS and class
INDICES — do NOT softmax yourself (it's built in) and do NOT
one-hot encode y (it expects `y=[0,1,1,0,...]` of dtype long).

---

## Hard

### 7. Manual Backpropagation — `p01`

**What it is:** Compute every gradient by hand with the chain rule —
what `.backward()` does for you, exposed. For each weight, the
gradient answers: "if I nudge this weight, how much does the loss
change?" Then update: `w -= lr × gradient`.

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

**Why ML cares:** You'll never write this in production — autograd
does it — but understanding it explains everything: vanishing
gradients, why ReLU helps, what `.backward()` actually computes.
This is the "how does a car engine work" lesson for ML.

**Code:**
```python
def sigmoid(z): return 1/(1+np.exp(-z))
def d_sigmoid(s): return s*(1-s)     # takes the ACTIVATED value
W2 -= lr * (h.T @ delta2);  W1 -= lr * (X.T @ delta1)
```

**Common confusion:** The error flows BACKWARD through the SAME
weights it used going forward (`delta2 @ W2.T`), and each layer's
gradient is error × local-derivative × input — forget any factor
and the network learns nothing (loss just sits there).

---

### 8. Full Training Loop: DataLoader + train/eval modes — `p02`

**What it is:** Real training feeds data in mini-batches (not all
at once), and models behave differently when training vs.
evaluating — `model.train()`/`model.eval()` and `torch.no_grad()`
manage that.

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

**Why ML cares:** Batching is how you train on datasets bigger than
memory and get gradient-estimate noise that actually helps escape
bad minima. `eval()`/`no_grad()` are what make dropout behave and
inference fast — production code always wraps prediction in them.

**Code:**
```python
from torch.utils.data import TensorDataset, DataLoader
with torch.no_grad():               # inside = pure inference
    logits = model(X_test)
```

**Common confusion:** `model.eval()` does NOT turn off gradient
tracking — it only changes layer behavior (dropout, batchnorm).
You need BOTH `model.eval()` AND `torch.no_grad()` for proper
inference. And `train()`/`eval()` don't return anything — they set
a flag on the model in place.

---

### 9. MNIST Digit Classification — `p03`

**What it is:** The "hello world" of deep learning: 70,000
handwritten digits, each a 28×28 grayscale image, labels 0-9.
`torchvision.datasets.MNIST` downloads it for you. An MLP that
flattens each image into 784 pixels hits ~97% in a few epochs.

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

**Why ML cares:** MNIST is the standard sanity check — every
framework tutorial, every new-idea paper starts here. It also
proves the MLP pipeline end-to-end on real data: download →
DataLoader → train → evaluate. Level-09 swaps the MLP for a CNN
and pushes past 99%.

**Code:**
```python
from torchvision import datasets, transforms
train = datasets.MNIST('./data', train=True, download=True,
                       transform=transforms.ToTensor())
# model(x.view(-1, 784)) — flatten each batch before Linear
```

**Common confusion:** Images arrive as [batch, 1, 28, 28] — a
Linear layer needs [batch, 784]. Forgetting to flatten gives a
shape error. Also `download=True` needs internet the first run.

---

## Done with concepts? → Try `easy/p01-perceptron.py`
