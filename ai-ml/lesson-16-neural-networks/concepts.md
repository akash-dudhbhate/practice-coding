# Lesson 16 — Concepts Explained (Neural Networks)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is a Neural Network?

**What:** A model inspired by the brain — layers of neurons that learn by adjusting weights.

```python
# A neural network:
# Input layer → Hidden layer(s) → Output layer
# Each layer has neurons with weights and biases
# Each connection has a weight
# Each neuron applies: output = activation(weight * input + bias)

# Example: 3 inputs → 4 hidden → 2 outputs
# Input: [age, income, score]
# Hidden: learns patterns
# Output: [prob_buy, prob_not_buy]
```

**Why it exists:** Traditional ML (linear regression, trees) can't learn complex non-linear patterns (images, text, speech). Neural networks with multiple layers can approximate any function → universal approximator → handles complex patterns.

**Where it's used:** Image recognition, NLP, speech recognition, game playing (AlphaGo), any complex pattern matching.

**What goes wrong without it:**
- Too few neurons → can't learn complex patterns → underfitting.
- Too many neurons → memorizes training data → overfitting.
- Not enough data → neural networks overfit easily → need regularization or more data.

---

## Neurons and Activation Functions

**What:** A neuron computes a weighted sum and applies an activation function.

```python
import numpy as np

# Neuron computation
def neuron(x, weights, bias, activation):
    z = np.dot(x, weights) + bias
    return activation(z)

# Common activation functions:
def relu(z): return np.maximum(0, z)           # ReLU: max(0, z)
def sigmoid(z): return 1 / (1 + np.exp(-z))    # Sigmoid: 0 to 1
def tanh(z): return np.tanh(z)                  # Tanh: -1 to 1
def softmax(z):
    e = np.exp(z - z.max())
    return e / e.sum()                          # Softmax: probabilities
```

**Why it exists:** Without activation functions, a neural network is just a linear model (composition of linear functions is linear). Activation functions add non-linearity → can learn complex patterns.

**Where it's used:** Every neural network layer. ReLU for hidden layers, sigmoid for binary output, softmax for multiclass output.

**What goes wrong without it:**
- Sigmoid in deep networks → vanishing gradient (derivative is small for large |z|) → early layers don't learn. Use ReLU.
- ReLU with negative inputs → output is 0 → "dead neuron" → doesn't learn. Use Leaky ReLU.
- Linear activation → network is just a linear model → can't learn non-linear patterns.

---

## Forward Propagation

**What:** Data flows from input → hidden → output to make a prediction.

```python
# Forward pass for a 2-layer network
def forward(X, W1, b1, W2, b2):
    # Layer 1: input → hidden
    z1 = X @ W1 + b1
    a1 = relu(z1)              # activation

    # Layer 2: hidden → output
    z2 = a1 @ W2 + b2
    a2 = sigmoid(z2)           # output activation

    return a2

# X: (batch, input_size)
# W1: (input_size, hidden_size)
# W2: (hidden_size, output_size)
```

**Why it exists:** Forward propagation is how the network makes predictions. Understanding it is essential — it's the "inference" part of the network.

**Where it's used:** Every prediction (inference) call.

**What goes wrong without it:**
- Matrix dimensions must match: `X @ W1` → X is (batch, in), W1 is (in, hidden) → output is (batch, hidden). Mismatch → error.
- Forgetting activation → just linear transformation → no non-linearity → poor model.
- Not batching → processing one sample at a time → slow. Use mini-batches.

---

## Backpropagation and Gradient Descent

**What:** Backpropagation calculates gradients; gradient descent updates weights to minimize loss.

```python
# Backpropagation: chain rule to calculate gradients
# Gradient descent: update weights in opposite direction of gradient

# Simplified training loop:
for epoch in range(100):
    # Forward
    pred = forward(X, W1, b1, W2, b2)

    # Loss (MSE for regression)
    loss = np.mean((pred - y) ** 2)

    # Backward (calculate gradients — simplified)
    d_loss = 2 * (pred - y) / len(y)
    d_W2 = a1.T @ d_loss
    d_a1 = d_loss @ W2.T
    d_z1 = d_a1 * (z1 > 0)  # ReLU derivative
    d_W1 = X.T @ d_z1

    # Update weights
    W1 -= learning_rate * d_W1
    W2 -= learning_rate * d_W2
```

**Why it exists:** Without backpropagation, you can't train neural networks (no way to know how to adjust weights). Backprop + gradient descent is the standard training algorithm.

**Where it's used:** Every neural network training — PyTorch, TensorFlow, all use backpropagation.

**What goes wrong without it:**
- Learning rate too high → loss diverges (NaN). Too low → doesn't learn.
- Vanishing gradient → deep networks → early layers don't learn. Use ReLU, batch normalization, residual connections.
- Exploding gradient → weights become huge → NaN. Use gradient clipping.

---

## Using scikit-learn MLP

**What:** sklearn provides `MLPClassifier` and `MLPRegressor` for simple neural networks.

```python
from sklearn.neural_network import MLPClassifier

model = MLPClassifier(
    hidden_layer_sizes=(64, 32),  # 2 hidden layers: 64 and 32 neurons
    activation='relu',
    learning_rate_init=0.001,
    max_iter=500,
    random_state=42,
)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

# Warnings: "ConvergenceWarning: Stochastic Optimizer reached max_iter"
# → increase max_iter or the model hasn't converged
```

**Why it exists:** For simple neural network tasks, sklearn is enough → no need for PyTorch/TensorFlow. Good for learning and small datasets.

**Where it's used:** Simple NN tasks, baseline neural network, educational purposes.

**What goes wrong without it:**
- Not scaling → MLP is sensitive to feature scales → slow convergence, poor performance. Always scale.
- `max_iter` too low → "ConvergenceWarning" → model hasn't converged → increase it.
- For deep learning (CNNs, RNNs, transformers) → sklearn can't do it → use PyTorch.

---

## Loss Functions

**What:** Loss functions measure how wrong the predictions are.

```python
# Regression: MSE (Mean Squared Error)
loss = np.mean((pred - y) ** 2)

# Binary classification: Binary Cross-Entropy
loss = -np.mean(y * np.log(pred) + (1 - y) * np.log(1 - pred))

# Multiclass: Categorical Cross-Entropy
loss = -np.mean(np.sum(y_onehot * np.log(pred), axis=1))
```

**Why it exists:** Without a loss function, you can't train the network (no signal for gradient descent). The loss function defines what "good" means → the network optimizes it.

**Where it's used:** Every neural network training.

**What goes wrong without it:**
- Wrong loss function → network optimizes the wrong thing → poor results. Use MSE for regression, cross-entropy for classification.
- `np.log(0)` → -inf → NaN loss. Add epsilon: `np.log(pred + 1e-15)`.
- Not one-hot encoding for multiclass → cross-entropy needs one-hot targets.

---

## Overfitting in Neural Networks

**What:** Neural networks have many parameters → easily memorize training data.

```python
# Signs of overfitting:
# - Training loss decreases, validation loss increases
# - Training accuracy >> validation accuracy
# - Model performs well on training, poorly on new data

# Solutions:
# 1. Dropout: randomly turn off neurons during training
# 2. L2 regularization: penalize large weights
# 3. Early stopping: stop when validation loss increases
# 4. Data augmentation: create more training data
# 5. Batch normalization: stabilize training
```

**Why it exists:** Neural networks are so flexible they can memorize anything → including noise → overfitting. Regularization techniques constrain the network → better generalization.

**Where it's used:** Every neural network training — always use at least one regularization technique.

**What goes wrong without it:**
- No regularization + large network + small data → severe overfitting → useless model.
- Too much dropout (0.5+) → network can't learn → underfitting.
- Not monitoring validation loss → you don't know if you're overfitting → always track both.

---

## Epochs, Batch Size, and Learning Rate

**What:** The three key training hyperparameters.

```python
# Epoch: one full pass through the training data
# Batch size: number of samples per gradient update
# Learning rate: step size for weight updates

# Typical values:
# Epochs: 10-100 (with early stopping)
# Batch size: 32, 64, 128 (powers of 2)
# Learning rate: 0.001 (Adam default), 0.01 (SGD)

# Training loop:
for epoch in range(epochs):
    for batch in batches(X, y, batch_size=32):
        pred = forward(batch_X)
        loss = compute_loss(pred, batch_y)
        gradients = backward(loss)
        update_weights(gradients, learning_rate)
```

**Why it exists:** These control the training dynamics. Wrong values → slow training, poor convergence, or divergence. Understanding them is essential for training neural networks.

**Where it's used:** Every neural network training.

**What goes wrong without it:**
- Batch size too large → slow convergence, poor generalization. Too small → noisy gradients, slow.
- Learning rate too high → diverges. Too low → never converges. Use learning rate schedulers.
- Too many epochs without early stopping → overfits. Too few → underfits.
