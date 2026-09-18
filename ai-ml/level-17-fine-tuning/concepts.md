# Level 17 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept explains:
What it is · Why it exists · Where it's used · What goes wrong without
it · worked example · code · expected output.

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

**Why it exists:** Fine-tuning a 7-billion-parameter LLM means
updating billions of weights — impossible on one GPU. Freezing was
invented to keep pretrained knowledge while training only what must
change: freeze 99% of the params and suddenly fine-tuning is cheap.
`requires_grad_(False)` is the switch that makes parameter-efficient
fine-tuning possible at all.

**Where it's used:** Every PEFT method — feature extraction, LoRA
(medium/p02), prompt tuning — starts by freezing the backbone. Any
time a pretrained model is reused as a fixed feature extractor.

**What goes wrong without it:**
- `requires_grad_(False)` (trailing underscore) modifies in place;
  `p.requires_grad = False` also works as an attribute set. What
  DOESN'T work reliably: freezing AFTER creating the optimizer — if
  you passed the full param list, the optimizer still allocates
  state for frozen params and can touch them via weight decay.
  Safest: freeze first, then build the optimizer over
  `requires_grad` params.
- No freezing → full backprop through 7B params → OOM on consumer
  hardware, plus catastrophic forgetting risk (hard/p03).

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

**Expected output:**
```python
freeze_backbone(model)   # → 99   (head params still trainable)
model[0].weight.requires_grad      # → False
model[2].weight.requires_grad      # → True
```

---

### 2. Counting Parameters (`numel`) — `p02`

**What it is:** `p.numel()` = number of elements in a parameter
tensor. Summing it over `model.parameters()` gives the total;
filtering on `requires_grad` gives the trainable count. These two
numbers are the report card of every fine-tuning method.

**Why it exists:** Trainable params drive training memory —
parameters + gradients + optimizer state (Adam stores TWO extra
values per trainable param). The count exists so you know before
you train whether the job fits: 387 trainable → ~1,161 floats;
freeze to 99 → ~297 floats. Scale that to 7B params and it's the
difference between "needs 8 GPUs" and "fits on a laptop."

**Where it's used:** Sizing every fine-tune and PEFT method,
reporting efficiency (hard/p02's ratio is built on this), and
estimating GPU memory before you commit to a training run.

**What goes wrong without it:**
- `model.parameters()` sees nested modules automatically — you
  never walk layers by hand for counting.
- `numel` counts ELEMENTS (256 for a 32×8 matrix), not tensors —
  counting `len(list(parameters()))` gives number of tensors (4),
  not params (387).
- Without the count, the OOM arrives mid-epoch instead of in a
  two-line check before training.

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

**Code:**
```python
def count_trainable(model):
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters()
                    if p.requires_grad)
    return total, trainable
```

**Expected output:**
```python
count_trainable(model)              # → (387, 387)   before freezing
# after freeze_backbone(model):
count_trainable(model)              # → (387, 99)
```

---

### 3. Replacing the Classification Head — `p03`

**What it is:** A pretrained model splits into BACKBONE (everything
that extracts features) and HEAD (the final Linear that maps features
to class scores). New task with a different number of classes? Swap
the head for a fresh `nn.Linear` — the backbone keeps its knowledge.

**Why it exists:** A pretrained backbone's features are
task-agnostic until the head maps them to YOUR classes. Head
swapping was invented as THE first move in transfer learning —
reuse 99% of a trained model, re-learn only the class mapping. The
head must match the backbone's OUTPUT size (`in_features` of the
old head) — that's the only constraint.

**Where it's used:** A ResNet trained on ImageNet's 1000 classes
gets a new 10-class head for your medical images; BERT gets a
2-class head for sentiment. Every transfer-learning tutorial starts
here.

**What goes wrong without it:**
- The mistake is creating `Linear(8, 5)` — copying the model's
  INPUT size instead of the old head's `in_features` (32). The new
  head then can't consume the backbone's 32-dim output → shape
  mismatch crash on the first forward pass.
- The new head starts RANDOM — it knows nothing yet. That's fine:
  it's small (99 params here) and trains fast. Panicking about the
  random init is wasted worry.
- Without a head swap, a 3-class model literally cannot emit 5
  class scores — output shape is hardwired to the old task.

**Worked example:**
```
model = Sequential(Linear(8,32), ReLU, Linear(32,3))   # 3 classes
replace_head(model, 5)

old head: Linear(in_features=32, out_features=3)   — thrown away
new head: Linear(in_features=32, out_features=5)   — random init

model(torch.randn(4, 8)) → shape (4, 5)   # 4 inputs, 5 class scores
```

**Code:**
```python
def replace_head(model, n_classes):
    old = model[-1]                       # last Linear
    model[-1] = nn.Linear(old.in_features, n_classes)
    return model
```

**Expected output:**
```python
replace_head(model, 5)
model(torch.randn(4, 8)).shape    # → torch.Size([4, 5])
model[-1]                         # → Linear(in_features=32,
                                  #          out_features=5)
```

---

## Medium

### 4. Feature Extraction (Frozen Backbone + Trained Head) — `p01`

**What it is:** The cheapest fine-tuning strategy: freeze the entire
backbone, train only the head on your new data. Gradients never flow
into the backbone, so its learned features are preserved bit-for-bit.

**Why it exists:** When your dataset is small (hundreds of
examples), training a big backbone WILL overfit — it memorizes.
Freezing was invented as the regularizer: a frozen backbone + tiny
head can't memorize much. It's also the cheapest possible
fine-tune — least memory, fastest epochs.

**Where it's used:** The standard "I have 500 labeled images"
recipe: frozen ResNet, train a logistic head. Any small-data
transfer task — classification, detection backbones, embedding
extractors.

**What goes wrong without it:**
- You must pass ONLY trainable params to Adam (or freeze before
  creating it). If the optimizer holds frozen params it still
  allocates state for them — and in some setups can still touch
  them via weight decay, slowly corrupting your "frozen" features.
- Small data + unfrozen backbone → the model memorizes the training
  set → great train accuracy, poor test accuracy.
- No freezing → you pay full fine-tune memory for a job that needed
  1% of it.

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

**Expected output:**
```python
feature_extract_finetune(X_tr, y_tr, X_te, y_te)
# → ≈ 1.000     (test accuracy on the 50 held-out samples)
```

---

### 5. LoRA — Low-Rank Adaptation — `p02`

**What it is:** Instead of retraining a weight matrix W (out×in),
freeze it and learn a small correction made of two skinny matrices:
`W_effective = W + B @ A`, where A is (rank×in) and B is (out×rank).
"Low rank" means rank << min(in, out) — a big matrix written as a
product of two small ones.

**Why it exists:** Full fine-tuning retrains every weight —
expensive in memory and in forgetting risk. LoRA was invented on
the observation that the *update* a new task needs is low-rank: a
768×768 matrix's useful correction fits in rank 4. So you freeze W
and learn only B@A — ~1% of the params, nearly all of the benefit.
B = zeros at init so `B@A = 0` → `W_eff = W` exactly → the adapted
layer starts IDENTICAL to the pretrained one, then learns a small
correction.

**Where it's used:** This is how the entire industry adapts LLMs
cheaply (Hugging Face `peft` is exactly this). One frozen base
model + dozens of small adapter files — one adapter per
customer/task, a few MB each instead of a full model copy.

**What goes wrong without it:**
- If you init B randomly too, `B@A` starts non-zero and the adapted
  layer CHANGES the model before any training — you're fine-tuning
  from a corrupted start. B = zeros is the trick that makes the
  adapter a no-op at step 0.
- Without LoRA (or another PEFT), each task/customer needs a full
  copy of a multi-GB model → storage and serving costs multiply by
  the number of adaptations.
- Rank too large → the adapter approaches full-FT cost anyway;
  rank too small → the correction can't express the task's needs.

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

**Expected output:**
```python
lora = LoRALinear(8, 32, rank=4)
sum(p.numel() for p in lora.parameters() if p.requires_grad)
# → 160        (A:32 + B:128; the 288 base params are frozen)
# at init: lora(x) == lora.base(x) exactly, since B @ A = 0
```

---

### 6. Full Fine-Tune vs Head-Only — `p03`

**What it is:** The two ends of the spectrum. FULL FT trains all 387
params — max flexibility, max cost, max forgetting risk. HEAD-ONLY
trains 99 — cheap and safe, but stuck with whatever features the
backbone already has.

**Why it exists:** Every fine-tune is a trade-off between
adaptability and cost/risk, and you can't know which strategy a task
needs without measuring. The comparison exists to teach the real
lesson — not "head-only always wins," but "always TRY the cheap
option first": if frozen features suffice, you saved 4× the
trainable params and eliminated forgetting risk for free.

**Where it's used:** Deciding a fine-tune strategy on any new task.
When head-only LOSES: a new task genuinely different from what the
backbone learned (e.g. ImageNet features → x-ray diagnosis).

**What goes wrong without it:**
- Re-seed (`manual_seed(42)`) before building EACH model, or they
  start from different random weights and the comparison is unfair —
  you'd be measuring init luck, not the strategy.
- Skipping the comparison → you either overpay (full FT when
  head-only sufficed) or underperform (head-only when the task
  needed backbone changes).

**Worked example:**
```
Same data, same model, 100 epochs each:

  full fine-tune:  trains 387 params → test acc 0.980
  head-only:       trains  99 params → test acc 1.000

Head-only matched — even beat — full FT here, because the frozen
random features already separated this easy dataset.
```

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

**Expected output:**
```python
full_vs_head(X_tr, y_tr, X_te, y_te)
# → (0.98, 1.0)    # (full_acc, head_acc) — head-only wins here
```

---

## Hard

### 7. LoRA Fine-Tuning End-to-End — `p01`

**What it is:** Put it together: wrap a backbone layer in a LoRA
adapter (copying the pretrained weights into the frozen base), then
train ONLY the tiny A/B matrices plus the head.

**Why it exists:** Near-full-FT accuracy while touching a fraction
of the weights — and the optimizer only allocates Adam state for
those params. This pattern was invented to make per-task LLM
adaptation economically viable: it's the entire business model of
adapter marketplaces and per-customer LLM customization.

**Where it's used:** Production LoRA fine-tunes — every
"fine-tune our model on your data" product ships essentially this:
frozen base + small trained adapters.

**What goes wrong without it:**
- Forgetting to copy the old weights into `lora.base`. Without
  `load_state_dict`, the "base" is a fresh random Linear — you're
  not adapting a pretrained model, you're training a weirdly-shaped
  new one, and all the pretrained features are gone.
- Training the base weights too → you're back to full-FT cost and
  forgetting risk with extra steps.

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

**Expected output:**
```python
lora_finetune(X_tr, y_tr, X_te, y_te, rank=4)
# → ≈ 0.98      # same ballpark as full FT, training only 259/387
```

---

### 8. Parameter Efficiency Report — `p02`

**What it is:** The LoRA sales pitch in one number:
`ratio = lora_trainable / full_trainable`. How much of the model do
you actually have to update?

**Why it exists:** Trainable params drive GPU memory: each trainable
param needs its value + gradient + 2 Adam moments ≈ 16 bytes in
fp32. The ratio exists to quantify the saving — a 7B model fully
trained needs ~112 GB; with 1% trainable, the optimizer state
shrinks to ~1 GB and the rest is just frozen weights sitting there.
THAT'S why LoRA fits on consumer GPUs.

**Where it's used:** Every PEFT paper and fine-tuning proposal —
the efficiency claim is meaningless without this number. Reporting
"we train X% of params" is the standard way to compare methods.

**What goes wrong without it:**
- The denominator is full TRAINABLE params, not total params. If
  the baseline model already has frozen layers, `full_trainable` <
  total — always filter on `requires_grad` for both, or your ratio
  is silently inflated.
- Without the number, "LoRA is efficient" is a vibe, not evidence —
  you can't compare methods or predict memory.

**Worked example:**
```
model:      all params trainable  → full_trainable  = 387
lora_model: backbone frozen       → lora_trainable  =  99

ratio = 99 / 387 = 0.2558 → "we train 25.6% of the params"

Real LoRA on hard/p01:      259 / 387 = 0.669
LLM-scale (768×768, r=4): 6,144 / 589,824 ≈ 0.0104 → ~1%
```

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

**Expected output:**
```python
param_efficiency(model, frozen_model)
# → {"full_trainable": 387, "lora_trainable": 99, "ratio": 0.2558}
param_efficiency(model, lora_wrapped_model)
# → {"full_trainable": 387, "lora_trainable": 259, "ratio": 0.669}
```

---

### 9. Catastrophic Forgetting (and Why LoRA Reverses It) — `p03`

**What it is:** Fine-tune a model on a new task and it forgets the
old one — gradient descent happily overwrites the weights that encoded
the original skill. Full FT destroys it permanently. LoRA freezes the
base weights, so removing the adapter restores the original model
exactly — forgetting becomes *reversible*.

**Why it exists:** Production models serve many tasks — if every
fine-tune destroyed previous abilities, you'd need N separate
models. LoRA's frozen base was invented (in part) to make
adaptation non-destructive: one frozen base, swap adapters per
task, delete the adapter to roll back a bad fine-tune instantly.
It's version control for model behavior.

**Where it's used:** Multi-tenant LLM serving (one base + per-
customer adapters), safe experimentation (roll back instantly), and
continual-learning research where forgetting is the enemy.

**What goes wrong without it:**
- `deepcopy` BEFORE wrapping/training — a shallow copy shares
  weight tensors, so "fine-tuning the copy" would silently mutate
  the original too. You'd corrupt your baseline while measuring it.
- `after_lora` being low is NOT a bug: with the adapter attached,
  outputs shift; the win is that `lora_recovered` returns to 0.98.
- Full FT on the new task → original skill wiped out permanently —
  no undo, you'd have to retrain from scratch to get it back.

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

**Expected output:**
```python
orig_before, after_full, after_lora, lora_recovered
# → (0.98, 0.06, 0.20, 0.98)
#   full FT destroys task A; LoRA distorts it while attached but
#   the original model is recovered exactly when adapters come off
```

---

## Done with concepts? → Try `easy/p01-freeze-backbone.py`
