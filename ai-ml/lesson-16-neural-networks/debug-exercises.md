# Lesson 16 — Debug Exercises

## Debug 01 (Easy: No Activation Function
```python
model = Sequential([Dense(64), Dense(1)])
```
<details><summary>Answer</summary>
**Bug:** No activation = linear. Stacked linear layers = one linear layer. Can't learn non-linear patterns.
**Fix:** Add activation: `Dense(64, activation="relu")`.
</details>

## Debug 02 (Medium: Wrong Loss Function
```python
model.compile(loss="mse")  # for classification
```
<details><summary>Answer</summary>
**Bug:** MSE for classification — wrong loss. Use categorical_crossentropy.
**Fix:** `loss="binary_crossentropy"` (binary) or `"categorical_crossentropy"` (multiclass).
</details>

## Debug 03 (Hard: Learning Rate Too High
```python
model.compile(optimizer=SGD(learning_rate=1.0))
# loss = nan
```
<details><summary>Answer</summary>
**Bug:** LR too high — weights oscillate, loss diverges to NaN.
**Fix:** Use 0.001 (Adam default) or 0.01 (SGD). Use learning rate finder.
</details>
