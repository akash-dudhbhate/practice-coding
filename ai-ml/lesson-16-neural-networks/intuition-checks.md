# Lesson 16 — Intuition Checks

## Check 01: What is a neural network?
<details><summary>Answer</summary>
Layers of neurons with weights. Each neuron: weighted sum of inputs + bias → activation function. Learns by adjusting weights to minimize loss via backpropagation (gradient descent).
</details>

## Check 02: Activation functions
```python
relu: max(0, x)          # hidden layers (default)
sigmoid: 1/(1+e^-x)      # binary output
softmax: probabilities   # multiclass output
tanh: (-1 to 1)          # hidden layers (alternative)
```
<details><summary>Answer</summary>
relu — fast, no vanishing gradient (default for hidden). sigmoid — binary classification output. softmax — multiclass probabilities. tanh — zero-centered, alternative to relu.
</details>

## Check 03: Epochs vs batch size
```python
model.fit(X, y, epochs=10, batch_size=32)
```
<details><summary>Answer</summary>
Epoch — one pass through all data. Batch size — samples per gradient update. 10 epochs × 32 batch = 10 passes, updating weights every 32 samples.
</details>

## Check 04: Overfitting in NN
```python
train_loss = 0.1
val_loss = 1.5  # big gap
```
<details><summary>Answer</summary>
Overfitting. Fix: dropout, regularization, early stopping, more data, simpler model.
</details>

## Check 05: Backpropagation
<details><summary>Answer</summary>
Algorithm: forward pass computes output. Compare to target (loss). Backward pass computes gradients of loss w.r.t. each weight. Update weights using gradients. Repeat.
</details>
