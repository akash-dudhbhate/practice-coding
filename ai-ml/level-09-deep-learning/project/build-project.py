"""
LEVEL 09 PROJECT — CIFAR-10 Classifier with Augmentation
=========================================================

Combine the whole level: custom nn.Module + augmentation + training.

BUILD `train_cifar(epochs=2)`:
  1. Data: CIFAR-10 via torchvision (auto-downloads to ./data)
     Train transform: RandomHorizontalFlip + RandomCrop(32,pad=4)
                      + ToTensor + Normalize
     Test transform:  ToTensor + Normalize only (never augment test!)
  2. Model: a CustomCNN class (nn.Module):
       conv(3→32) → relu → pool → conv(32→64) → relu → pool
       → flatten → fc(64*8*8 → 256) → relu → fc(256→10)
  3. CrossEntropyLoss + Adam(0.001), `epochs` epochs
  4. Return (test_acc, model)

EXPECTED OUTPUT:
  ```
  Test accuracy: ~0.55-0.65   (2 epochs — CIFAR is hard)
  ```

BONUS EXPERIMENTS (comment what you observe):
  - epochs=5 → how much does accuracy improve?
  - remove augmentation → does test acc drop? (memorization)
  - add Dropout(0.3) before fc2 → overfitting less?

WHY AUGMENT TEST SET IS NEVER AUGMENTED: you'd be measuring the
model on data it can't see in production — the test must be the
"real world" distribution.
"""

# === WRITE YOUR CODE BELOW ===

def train_cifar(epochs=2):
    # TODO
    pass


if __name__ == "__main__":
    acc, _ = train_cifar()
    print(f"Test accuracy: {acc:.4f}")
