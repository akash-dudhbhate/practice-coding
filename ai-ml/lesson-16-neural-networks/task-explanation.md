# Lesson 16 — Neural Networks

## What you'll learn
- What neural networks are (layers, neurons, weights)
- Activation functions (ReLU, sigmoid, tanh, softmax)
- Forward propagation (making predictions)
- Backpropagation and gradient descent (training)
- Using sklearn MLPClassifier/MLPRegressor
- Loss functions (MSE, cross-entropy)
- Overfitting and regularization (dropout, L2, early stopping)
- Training hyperparameters (epochs, batch size, learning rate)

## Lesson

### sklearn MLP
```python
from sklearn.neural_network import MLPClassifier
model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500)
model.fit(X_scaled, y_train)
```

### Activation functions
```python
relu(z) = max(0, z)
sigmoid(z) = 1 / (1 + exp(-z))
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Implement ReLU, sigmoid, and tanh from scratch. Plot all three on the same graph for input range -5 to 5. Verify their ranges (ReLU: 0+, sigmoid: 0-1, tanh: -1 to 1).
2. `easy/p02-solve.py` — Train sklearn's `MLPClassifier` on the Iris dataset (scaled). Print accuracy. Compare with logistic regression. Show that NN can match or beat LR.
3. `easy/p03-solve.py` — Implement a single neuron from scratch: weighted sum + sigmoid activation. Test with 3 inputs, 3 weights, and a bias. Print the output.

### Medium
4. `medium/p01-solve.py` — Implement forward propagation for a 2-layer network from scratch: input (3) → hidden (4, ReLU) → output (1, sigmoid). Use random weights. Print the output for a batch of inputs.
5. `medium/p02-solve.py` — Train MLPClassifier with different architectures: (8,), (16, 8), (32, 16, 8). Compare accuracy and training time. Identify the best architecture for the dataset.
6. `medium/p03-solve.py` — Demonstrate overfitting: train a large MLP (100, 100, 100) on a small dataset. Show training accuracy = 100% but test accuracy is low. Then add `alpha=0.1` (L2 regularization) and show improvement.

### Hard
7. `hard/p01-solve.py` — Implement a complete neural network from scratch: forward prop, backprop, gradient descent. Train on a 2D classification dataset (make_moons). Plot the decision boundary and loss curve. Use ReLU + sigmoid.
8. `hard/p02-solve.py` — Build an MLP regression pipeline: create a non-linear regression dataset, train MLPRegressor with different hidden layer sizes, plot the predictions vs actual for each, and identify the best architecture. Show overfitting with too many neurons.
9. `hard/p03-solve.py` — Build a neural network hyperparameter study: fix a dataset, vary (a) learning rate [0.001, 0.01, 0.1], (b) batch size [16, 32, 64], (c) architecture [(32,), (64, 32), (128, 64, 32)]. For each combination, record final loss and accuracy. Create a heatmap or table of results.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
