# Lesson 16 — Coding Check

## Easy

### p01-solve.py — Activation functions
- [ ] ReLU implemented: max(0, z)
- [ ] Sigmoid implemented: 1 / (1 + exp(-z))
- [ ] Tanh implemented
- [ ] All three plotted on same graph
- [ ] Input range -5 to 5
- [ ] Ranges verified (ReLU: 0+, sigmoid: 0-1, tanh: -1 to 1)

### p02-solve.py — MLP on Iris
- [ ] Iris dataset loaded and scaled
- [ ] `MLPClassifier` trained
- [ ] Accuracy printed
- [ ] Logistic regression also trained
- [ ] Comparison: MLP ≥ LR accuracy

### p03-solve.py — Single neuron
- [ ] Weighted sum calculated (dot product + bias)
- [ ] Sigmoid activation applied
- [ ] 3 inputs, 3 weights, 1 bias used
- [ ] Output printed (between 0 and 1)
- [ ] No sklearn used

## Medium

### p01-solve.py — Forward propagation
- [ ] Input layer (3 features) to hidden (4 neurons)
- [ ] ReLU activation on hidden layer
- [ ] Hidden to output (1 neuron)
- [ ] Sigmoid activation on output
- [ ] Random weights used
- [ ] Output printed for a batch
- [ ] Matrix dimensions correct

### p02-solve.py — Architecture comparison
- [ ] (8,) architecture tested
- [ ] (16, 8) architecture tested
- [ ] (32, 16, 8) architecture tested
- [ ] Accuracy printed for each
- [ ] Training time measured for each
- [ ] Best architecture identified
- [ ] Data scaled

### p03-solve.py — Overfitting demo
- [ ] Large MLP (100, 100, 100) trained
- [ ] Small dataset used
- [ ] Training accuracy = 100% (overfitting)
- [ ] Test accuracy is low
- [ ] L2 regularization (alpha=0.1) added
- [ ] Test accuracy improved
- [ ] Overfitting reduced

## Hard

### p01-solve.py — NN from scratch
- [ ] Forward propagation implemented
- [ ] Backpropagation implemented (chain rule)
- [ ] Gradient descent implemented
- [ ] ReLU + sigmoid activations used
- [ ] Trained on make_moons dataset
- [ ] Loss curve plotted (decreasing)
- [ ] Decision boundary plotted
- [ ] No sklearn used for the network

### p02-solve.py — MLP regression pipeline
- [ ] Non-linear regression dataset created
- [ ] Multiple hidden layer sizes tested
- [ ] Predictions vs actual plotted for each
- [ ] Overfitting shown with too many neurons
- [ ] Best architecture identified
- [ ] R² score reported for each

### p03-solve.py — Hyperparameter study
- [ ] Learning rate [0.001, 0.01, 0.1] varied
- [ ] Batch size [16, 32, 64] varied
- [ ] Architecture [(32,), (64, 32), (128, 64, 32)] varied
- [ ] Final loss recorded for each combination
- [ ] Accuracy recorded for each combination
- [ ] Results in a table or heatmap
- [ ] Best combination identified
- [ ] Trends analyzed (e.g., high LR = unstable)
