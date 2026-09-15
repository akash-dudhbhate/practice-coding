# Lesson 16 — Refactoring Challenges

## Refactor 01 (Easy): Manual Weight Init
### Before
```python
W = np.random.randn(10, 5) * 0.01
```
### After
```python
# Use framework defaults (PyTorch/TF handle this)
```

## Refactor 02 (Medium): Manual Training Loop
### Before
```python
for epoch in range(10):
    for x, y in data:
        pred = model(x)
        loss = criterion(pred, y)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
```
### After
```python
# Use a trainer/lightning module or higher-level API
import pytorch_lightning as pl
trainer = pl.Trainer(max_epochs=10)
trainer.fit(model, data)
```

## Refactor 03 (Hard): No Validation Split
### Before
```python
model.fit(X, y, epochs=100)  # no validation, can't detect overfit
```
### After
```python
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100,
          callbacks=[EarlyStopping(patience=5)])
```
