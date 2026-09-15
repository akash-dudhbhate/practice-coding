# Lesson 16 — Common Mistakes

## Mistake 01: No activation in hidden layers
```python
# WRONG — linear, can't learn complex patterns
Dense(64)
# CORRECT
Dense(64, activation="relu")
```

## Mistake 02: Wrong loss function
```python
# WRONG — MSE for classification
model.compile(loss="mse")
# CORRECT
model.compile(loss="binary_crossentropy")  # binary
model.compile(loss="categorical_crossentropy")  # multiclass
```

## Mistake 03: No scaling
```python
# NNs are very sensitive to input scale
# Always scale inputs
StandardScaler().fit_transform(X)
```

## Mistake 04: Not using dropout
```python
# Add dropout to prevent overfitting
Dense(64, activation="relu"),
Dropout(0.5),
Dense(64, activation="relu"),
Dropout(0.5),
```

## Mistake 05: Too many epochs without early stopping
```python
# WRONG — overfits
model.fit(X, y, epochs=1000)
# CORRECT
EarlyStopping(monitor="val_loss", patience=10)
model.fit(X, y, epochs=1000, callbacks=[early_stop])
```
