# Level 17 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

The theme of this whole level: **fine-tuning is about shrinking the
number of parameters you update.** A pretrained model already knows
useful features — you want to nudge it, not retrain it. LoRA is the
industry-standard way to nudge.

---

## Easy

### 1. Freezing Layers (`requires_grad`) — `p01`

**What it is:** Every PyTorch parameter has a `requires_grad` flag.
When it's `True`, PyTorch computes a gradient for it during
`backward()` and the optimizer updates it. Setting it to `False`
"freezes" the parameter — it keeps its value forever. A frozen
layer becomes a fixed feature extractor.

**Worked example:**
```
model = Sequential(Linear(8,32), ReLU, Linear(32,3))

Parameter counts:
  model[0] = Linear(8,32):  8×32 weights + 32 biases  = 288
  model[1] = ReLU:          no parameters            =   0
  model[2] = Linear(32,3): 32×3 weights + 3 biases   =  99
                                          total    = 387

Freeze model[0] → only the head's 99 params can still train.
freeze_backbone(model) returns 99.
```

**Why ML cares:** Fine-tuning a 7-billion-parameter LLM means
updating billions of weights — impossible on one GPU. Freeze 99% of
them and suddenly it's cheap. `requires_grad_(False)` is the switch
that makes parameter-efficient fine-tuning possible at all.

**Code:**
```python
def freeze_backbone(model):
    layers = list(model.children())      # [Linear, ReLU, Linear]
    for layer in layers[:-1]:            # everything but the last
        for p in layer.parameters():
            p.requires_grad_(False)
    return sum(p.numel() for p in model.parameters()
               if p.requires_grad)
```

**Common confusion:** `requires_grad_(False)` with the trailing
underscore modifies in place and returns the tensor; the non-underscore
version `p.requires_grad = False` also works as an attribute set.
What DOESN'T work: freezing after creating the optimizer only matters
if you passed a filtered param list — safest is freeze first, then
build the optimizer over `requires_grad` params.

---

### 2. Counting Parameters (`numel`) — `p02`

**What it is:** `p.numel()` = number of elements in a parameter
tensor. Summing it over `model.parameters()` gives the total;
filtering on `requires_grad` gives the trainable count. These two
numbers are the report card of every fine-tuning method.

**Worked example:**
```
model = Sequential(Linear(8,32), ReLU, Linear(32,3))

model[0].weight  shape (32, 8) → 256 elems
model[0].bias    shape (32,)   →  32 elems     subtotal 288
model[2].weight  shape (3, 32) →  96 elems
model[2].bias    shape (3,)    →   3 elems     subtotal  99

count_trainable(model)           → (387, 387)   all trainable
freeze model[0], recount         → (387, 99)    25.6% trainable
```

**Why ML cares:** Memory during training ≈ parameters + gradients +
optimizer state — Adam stores TWO extra values per trainable param.
387 trainable params → ~1,161 floats; freeze to 99 → ~297 floats.
Scale that to 7B params and it's the difference between "needs 8
GPUs" and "fits on a laptop."

**Code:**
```python
def count_trainable(model):
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters()
                    if p.requires_grad)
    return total, trainable
```

**Common confusion:** `model.parameters()` sees nested modules
automatically — you never walk layers by hand for counting. And
`numel` counts ELEMENTS (256 for a 32×8 matrix), not tensors.

---

### 3. Replacing the Classification Head — `p03`

**What it is:** A pretrained model splits into BACKBONE (everything
that extracts features) and HEAD (the final Linear that maps features
to class scores). New task with a different number of classes? Swap
the head for a fresh `nn.Linear` — the backbone keeps its knowledge.

**Worked example:**
```
model = Sequential(Linear(8,32), ReLU, Linear(32,3))   # 3 classes
replace_head(model, 5)

old head: Linear(in_features=32, out_features=3)   — thrown away
new head: Linear(in_features=32, out_features=5)   — random init

model(torch.randn(4, 8)) → shape (4, 5)   # 4 inputs, 5 class scores
```

**Why ML cares:** This is THE first move in transfer learning. A
ResNet trained on ImageNet's 1000 classes gets a new 10-class head
for your medical images; BERT gets a 2-class head for sentiment.
The head must match the backbone's OUTPUT size (`in_features` of the
old head) — that's the only constraint.

**Code:**
```python
def replace_head(model, n_classes):
    old = model[-1]                       # last Linear
    model[-1] = nn.Linear(old.in_features, n_classes)
    return model
```

**Common confusion:** The new head starts RANDOM — it knows nothing
yet. That's fine: it's small (99 params here) and trains fast. The
mistake is creating `Linear(8, 5)` — copying the model's INPUT size
instead of the old head's `in_features` (32).

---

## Medium

### 4. Feature Extraction (Frozen Backbone + Trained Head) — `p01`

**What it is:** The cheapest fine-tuning strategy: freeze the entire
backbone, train only the head on your new data. Gradients never flow
into the backbone, so its learned features are preserved bit-for-bit.

**Worked example:**
```
Data: 200 samples, 8 features, 3 classes (make_classification)
Model: Linear(8,32) → ReLU → Linear(32,3)
Freeze model[0] → trainable = 99 (head only)

Train head on 150 samples, CrossEntropy + Adam(0.01), 100 epochs:
  → test accuracy ≈ 1.000 on the 50 held-out samples

Why so good? A random-but-frozen 8→32 projection already spreads
the classes apart; the head just draws the boundary.
```

**Why ML cares:** When your dataset is small (hundreds of examples),
training a big backbone WILL overfit — it memorizes. A frozen
backbone + tiny head can't memorize much. This is the standard "I
have 500 labeled images" recipe: frozen ResNet, train a logistic
head.

**Code:**
```python
def feature_extract_finetune(X_tr, y_tr, X_te, y_te):
    torch.manual_seed(42)
    model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(),
                          nn.Linear(32, 3))
    for p in model[0].parameters():
        p.requires_grad_(False)
    opt = torch.optim.Adam(
        [p for p in model.parameters() if p.requires_grad], lr=0.01)
    loss_fn = nn.CrossEntropyLoss()
    for _ in range(100):
        opt.zero_grad()
        loss_fn(model(X_tr), y_tr).backward()
        opt.step()
    preds = model(X_te).argmax(dim=1)
    return (preds == y_te).float().mean().item()
```

**Common confusion:** You must pass ONLY trainable params to Adam
(or freeze before creating it). If the optimizer holds frozen params
it still allocates state for them — and in some setups can still
touch them via weight decay.

---

### 5. LoRA — Low-Rank Adaptation — `p02`

**What it is:** Instead of retraining a weight matrix W (out×in),
freeze it and learn a small correction made of two skinny matrices:
`W_effective = W + B @ A`, where A is (rank×in) and B is (out×rank).
"Low rank" means rank << min(in, out) — a big matrix written as a
product of two small ones.

**Worked example (the whole point of LoRA — parameter math):**
```
Linear(8, 32), rank = 4:
  full W:        8×32            = 256 params (+32 bias = 288)
  LoRA A (4×8):                  =  32
  LoRA B (32×4):                 = 128
  trainable: 32 + 128            = 160   vs 288 for full retrain

LLM-scale — a 768×768 attention matrix, rank 4:
  full W:        768×768         = 589,824
  LoRA A+B:      4×768 + 768×4   =   6,144   ← ~1% !
  ratio = 6144/589824 ≈ 0.0104

Forward:  y = base(x) + (x @ A.T) @ B.T
Init:     A ~ randn·0.01,  B = zeros
  → B@A = 0 → W_eff = W exactly → adapted layer starts IDENTICAL
    to the pretrained one, then learns a small correction.
```

**Why ML cares:** This is how the entire industry adapts LLMs cheaply
(Hugging Face `peft` is exactly this). One frozen base model + dozens
of small adapter files — one adapter per customer/task, a few MB
each instead of a full model copy.

**Code:**
```python
class LoRALinear(nn.Module):
    def __init__(self, in_f, out_f, rank):
        super().__init__()
        self.base = nn.Linear(in_f, out_f)
        for p in self.base.parameters():
            p.requires_grad_(False)
        self.A = nn.Parameter(torch.randn(rank, in_f) * 0.01)
        self.B = nn.Parameter(torch.zeros(out_f, rank))

    def forward(self, x):
        return self.base(x) + (x @ self.A.T) @ self.B.T
```

**Common confusion:** If you init B randomly too, `B@A` starts
non-zero and the adapted layer CHANGES the model before any training.
B = zeros is the trick that makes the adapter a no-op at step 0.

---

### 6. Full Fine-Tune vs Head-Only — `p03`

**What it is:** The two ends of the spectrum. FULL FT trains all 387
params — max flexibility, max cost, max forgetting risk. HEAD-ONLY
trains 99 — cheap and safe, but stuck with whatever features the
backbone already has.

**Worked example:**
```
Same data, same model, 100 epochs each:

  full fine-tune:  trains 387 params → test acc 0.980
  head-only:       trains  99 params → test acc 1.000

Head-only matched — even beat — full FT here, because the frozen
random features already separated this easy dataset.
When head-only LOSES: a new task genuinely different from what the
backbone learned (e.g. ImageNet features → x-ray diagnosis).
```

**Why ML cares:** The lesson isn't "head-only always wins" — it's
"always TRY the cheap option first." If frozen features suffice, you
saved 4× the trainable params and eliminated forgetting risk for
free. Measure before you spend.

**Code:**
```python
def full_vs_head(X_tr, y_tr, X_te, y_te):
    def build():
        torch.manual_seed(42)
        return nn.Sequential(nn.Linear(8, 32), nn.ReLU(),
                             nn.Linear(32, 3))
    def train(m):
        opt = torch.optim.Adam(
            [p for p in m.parameters() if p.requires_grad], lr=0.01)
        lf = nn.CrossEntropyLoss()
        for _ in range(100):
            opt.zero_grad()
            lf(m(X_tr), y_tr).backward()
            opt.step()
        return (m(X_te).argmax(1) == y_te).float().mean().item()

    a = build();  full_acc = train(a)
    b = build()
    for p in b[0].parameters(): p.requires_grad_(False)
    head_acc = train(b)
    return full_acc, head_acc
```

**Common confusion:** Re-seed (`manual_seed(42)`) before building EACH
model, or they start from different random weights and the comparison
is unfair — you'd be measuring init luck, not the strategy.

---

## Hard

### 7. LoRA Fine-Tuning End-to-End — `p01`

**What it is:** Put it together: wrap a backbone layer in a LoRA
adapter (copying the pretrained weights into the frozen base), then
train ONLY the tiny A/B matrices plus the head.

**Worked example:**
```
model = Sequential(Linear(8,32), ReLU, Linear(32,3))
Replace model[0] with LoRALinear(8, 32, rank=4),
copying the old Linear's weights into lora.base.

Trainable params after wrapping:
  A (4×8)  + B (32×4) + head (32×3 + 3)
    32     +   128    +      99          = 259

vs full fine-tune: 387
→ 259/387 ≈ 67% trainable, yet test acc ≈ 0.980 — same as full FT.

(On a real LLM the ratio is ~1%: the head doesn't exist and every
 layer gets rank-4 adapters, so savings stack up.)
```

**Why ML cares:** Near-full-FT accuracy while touching a fraction of
the weights — and the optimizer only allocates Adam state for those
259 params. This is the entire business model of adapter marketplaces
and per-customer LLM customization.

**Code:**
```python
def lora_finetune(X_tr, y_tr, X_te, y_te, rank=4):
    torch.manual_seed(42)
    model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(),
                          nn.Linear(32, 3))
    old = model[0]
    lora = LoRALinear(8, 32, rank)
    lora.base.load_state_dict(old.state_dict())  # keep pretrained wts
    model[0] = lora
    opt = torch.optim.Adam(
        [p for p in model.parameters() if p.requires_grad], lr=0.01)
    lf = nn.CrossEntropyLoss()
    for _ in range(100):
        opt.zero_grad()
        lf(model(X_tr), y_tr).backward()
        opt.step()
    return (model(X_te).argmax(1) == y_te).float().mean().item()
```

**Common confusion:** Forgetting to copy the old weights into
`lora.base`. Without `load_state_dict`, the "base" is a fresh random
Linear — you're not adapting a pretrained model, you're training a
weirdly-shaped new one.

---

### 8. Parameter Efficiency Report — `p02`

**What it is:** The LoRA sales pitch in one number:
`ratio = lora_trainable / full_trainable`. How much of the model do
you actually have to update?

**Worked example:**
```
model:      all params trainable  → full_trainable  = 387
lora_model: backbone frozen       → lora_trainable  =  99

ratio = 99 / 387 = 0.2558 → "we train 25.6% of the params"

Real LoRA on hard/p01:      259 / 387 = 0.669
LLM-scale (768×768, r=4): 6,144 / 589,824 ≈ 0.0104 → ~1%
```

**Why ML cares:** Trainable params drive GPU memory: each trainable
param needs its value + gradient + 2 Adam moments ≈ 16 bytes in
fp32. A 7B model fully trained needs ~112 GB; with 1% trainable, the
optimizer state shrinks to ~1 GB — the rest is just the frozen
weights sitting there. THAT'S why LoRA fits on consumer GPUs.

**Code:**
```python
def param_efficiency(model, lora_model):
    full = sum(p.numel() for p in model.parameters()
               if p.requires_grad)
    lora = sum(p.numel() for p in lora_model.parameters()
               if p.requires_grad)
    return {"full_trainable": full,
            "lora_trainable": lora,
            "ratio": lora / full}
```

**Common confusion:** The denominator is full TRAINABLE params, not
total params. If the baseline model already has frozen layers,
`full_trainable` < total — always filter on `requires_grad` for both.

---

### 9. Catastrophic Forgetting (and Why LoRA Reverses It) — `p03`

**What it is:** Fine-tune a model on a new task and it forgets the
old one — gradient descent happily overwrites the weights that encoded
the original skill. Full FT destroys it permanently. LoRA freezes the
base weights, so removing the adapter restores the original model
exactly — forgetting becomes *reversible*.

**Worked example:**
```
Model trained on task A (orig test acc):
  orig_before   = 0.98

FULL FT on task B, then re-measure on task A:
  after_full    = 0.06   ← original skill WIPED OUT

LORA FT on task B (adapters attached), measure on task A:
  after_lora    = 0.20   ← adapter distorts behavior while attached

RECOVER: rebuild Sequential from the frozen lora.base weights:
  lora_recovered = 0.98  ← original model back, bit for bit
```

**Why ML cares:** Production models serve many tasks. If every
fine-tune destroyed previous abilities, you'd need N separate models.
With LoRA: one frozen base, swap adapters per task, delete the
adapter to roll back a bad fine-tune instantly. It's version control
for model behavior.

**Code:**
```python
# the recovery trick — base weights were never updated:
plain = nn.Sequential(lora0.base, nn.ReLU(), lora2.base)
# plain IS the original pretrained model again

# and the full experiment shape:
#   deepcopy(pretrained) → full FT on new task → acc crashes
#   deepcopy(pretrained) → wrap in LoRA → FT → acc drops while
#     adapter attached → strip adapters → acc restored
```

**Common confusion:** `deepcopy` BEFORE wrapping/training — a shallow
copy shares weight tensors, so "fine-tuning the copy" would silently
mutate the original too. And `after_lora` being low is NOT a bug:
with the adapter attached, outputs shift; the win is that
`lora_recovered` returns to 0.98.

---

## Done with concepts? → Try `easy/p01-freeze-backbone.py`
