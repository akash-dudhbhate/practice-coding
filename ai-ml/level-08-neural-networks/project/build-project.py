"""
LEVEL 08 PROJECT — Handwritten Digit Recognizer (built-in data)
================================================================

MNIST needs a download. sklearn's `load_digits()` is the same idea —
1797 tiny 8×8 digit images, built-in, instant.

BUILD `train_digits()`:
  1. load_digits() → X (1797×64), y (0-9)
  2. Scale: X / 16.0 (pixels are 0-16)
  3. Split 80/20, convert to torch tensors
  4. nn.Sequential: Linear(64,64) → ReLU → Linear(64,10)
     CrossEntropyLoss + Adam(lr=0.001), train 300 epochs (full batch)
  5. Return (test_accuracy, model, X_test, y_test)

ALSO write `show_mistakes(model, X_test, y_test, n=5)`:
  prints the n test samples the model got wrong
  (predicted vs true label) — looking at errors is how
  real practitioners debug.

EXPECTED OUTPUT:
  ```
  Test accuracy: ~0.97
  Mistakes:
    predicted 8, was 9
    predicted 5, was 6
    ...
  ```

WHY IT MATTERS: this is the SAME architecture as MNIST — just
smaller images (8×8=64 inputs instead of 28×28=784).
"""

# === WRITE YOUR CODE BELOW ===

def train_digits():
    # TODO
    pass


def show_mistakes(model, X_test, y_test, n=5):
    # TODO
    pass


if __name__ == "__main__":
    acc, model, X_te, y_te = train_digits()
    print(f"Test accuracy: {acc:.4f}")
    show_mistakes(model, X_te, y_te)
