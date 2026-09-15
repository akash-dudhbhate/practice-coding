# Image Classifier API (PyTorch) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
medium-08-image-classifier-api/
├── model.py, dataset.py, train.py, predict.py, app.py
└── README.md
```

---

## Implementation Steps

### Step 1: Dataset

Use CIFAR-10 or a custom dataset. Train/val/test split. DataLoaders.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Model Architecture

Simple CNN: conv layers, pooling, FC. Or use transfer learning (ResNet18).

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Training Loop

Forward, loss, backward, step. Track loss and accuracy per epoch. Save best.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Data Augmentation

Random crop, flip, rotation, color jitter. Improve generalization.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Evaluation

Accuracy, per-class precision/recall, confusion matrix. Visualize predictions.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Save Model

torch.save model state_dict. Save class names. Load function.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Prediction Function

Load model, preprocess image, predict, return class + confidence.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: FastAPI Endpoint

POST /classify accepts image file → {class, confidence, all_probs}.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Testing

Test with real images. Handle different formats, sizes, invalid inputs.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] Dataset with DataLoaders
- [ ] CNN model (or transfer learning)
- [ ] Training loop with tracking
- [ ] Data augmentation
- [ ] Evaluation (accuracy, per-class)
- [ ] Confusion matrix
- [ ] Model saved and loadable
- [ ] FastAPI image classification endpoint
- [ ] Handles various image formats
- [ ] Tested with real images

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
