# Lesson 17 — Debug Exercises

## Debug 01 (Easy: Forgot zero_grad
```python
for x, y in dataloader:
    output = model(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()
    # gradients accumulate!
```
<details><summary>Answer</summary>
**Bug:** Forgot `optimizer.zero_grad()` — gradients accumulate across batches.
**Fix:** Add `optimizer.zero_grad()` before `loss.backward()`.
</details>

## Debug 02 (Medium: No model.train()/eval()
```python
model(x)  # during evaluation
# dropout and batchnorm still active
```
<details><summary>Answer</summary>
**Bug:** Model in train mode during evaluation — dropout active, batchnorm uses batch stats.
**Fix:** `model.eval()` before evaluation, `model.train()` before training.
</details>

## Debug 03 (Hard: No torch.no_grad() for inference
```python
for x, y in test_loader:
    output = model(x)  # builds computation graph
```
<details><summary>Answer</summary>
**Bug:** No `torch.no_grad()` — wastes memory building graph for inference.
**Fix:** `with torch.no_grad(): output = model(x)`.
</details>
