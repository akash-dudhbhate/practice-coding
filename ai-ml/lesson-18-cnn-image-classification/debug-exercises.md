# Lesson 18 — Debug Exercises

## Debug 01 (Easy: Wrong Input Shape
```python
model(x)  # x shape: (32, 784) — flattened
# model expects (batch, channels, height, width)
```
<details><summary>Answer</summary>
**Bug:** CNN expects 4D input (B, C, H, W). Input is 2D (flattened).
**Fix:** `x = x.view(-1, 1, 28, 28)` — reshape to (batch, 1, 28, 28).
</details>

## Debug 02 (Medium: No Normalization
```python
transform = ToTensor()  # only scales to 0-1
# no normalization
```
<details><summary>Answer</summary>
**Bug:** Not normalizing — model trains slower, less stable.
**Fix:** `transforms.Normalize(mean=[0.5], std=[0.5])`.
</details>

## Debug 03 (Hard: No Data Augmentation
```python
transform = transforms.Compose([ToTensor()])
# model overfits on small dataset
```
<details><summary>Answer</summary>
**Bug:** No augmentation — small dataset leads to overfitting.
**Fix:** Add `RandomFlip, RandomRotation, ColorJitter`.
</details>
