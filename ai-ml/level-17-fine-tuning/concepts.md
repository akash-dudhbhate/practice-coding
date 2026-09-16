# Level 17 — Concepts Reference

## Easy

### Freezing Layers
- `param.requires_grad_(False)` → PyTorch won't compute gradients for it
- A frozen layer keeps its pretrained weights — it becomes a fixed feature extractor
- The optimizer only updates params where `requires_grad == True`

### Counting Parameters
- `sum(p.numel() for p in model.parameters())` → total
- `sum(p.numel() for p in model.parameters() if p.requires_grad)` → trainable
- Fine-tuning is largely about *shrinking the second number*

### Head Replacement
- The "head" = final classifier layer; the "backbone" = everything before it
- New task, new classes? Swap `model[-1]` for a fresh `nn.Linear(hidden, n_classes)`
- New head starts random; the backbone keeps its learned features

## Medium

### Feature Extraction
- Freeze backbone → forward pass still works, backward only reaches the head
- Fast, cheap, and hard to overfit — but limited by what the backbone already knows

### LoRA (Low-Rank Adaptation)
- Idea: don't retrain W (out×in). Learn a small correction instead:
  `W_eff = W + B @ A` where A is (rank × in) and B is (out × rank)
- Trainable params per layer: `rank*(in + out)` instead of `in*out`
  — rank 4 on a 32×8 layer: 160 vs 288
- Init B = 0 so the adapted layer starts identical to the original
- This is how LLMs are adapted cheaply (peft, Hugging Face)

### Full FT vs Head-Only
- Full FT: most flexible, most params, most forgetting risk
- Head-only: cheapest, but frozen features may not fit the new task
- LoRA sits in between: adapts internal features with <10% of the params

## Hard

### LoRA Fine-Tuning
- Wrap a Linear in a module that computes `base(x) + (x @ A.T) @ B.T`
- Freeze base, train only A and B (and optionally the head)
- Near-full-FT accuracy with a fraction of the trainable weights

### Parameter Efficiency
- `ratio = lora_trainable / full_trainable` — often 0.01–0.1 in real models
- Fewer trainable params → less memory, less optimizer state, faster updates

### Catastrophic Forgetting
- Full FT on a new task overwrites the weights → original skill is destroyed
- LoRA leaves base weights untouched → *remove the adapter, get the
  original model back exactly*
- Forgetting isn't avoided, it's *reversible* — that's the real LoRA win
