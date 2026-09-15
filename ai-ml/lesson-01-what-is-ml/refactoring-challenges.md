# Lesson 01 — Refactoring Challenges

## Refactor 01 (Easy): Manual Train/Test Split
### Before
```python
import random
random.shuffle(data)
split = int(0.8 * len(data))
train, test = data[:split], data[split:]
```
### After
```python
from sklearn.model_selection import train_test_split
train, test = train_test_split(data, test_size=0.2, random_state=42)
```

## Refactor 02 (Medium): Manual Accuracy
### Before
```python
correct = 0
for true, pred in zip(y_true, y_pred):
    if true == pred: correct += 1
accuracy = correct / len(y_true)
```
### After
```python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)
```

## Refactor 03 (Hard): Manual Model
### Before
```python
# Implementing linear regression from scratch
def predict(x, w, b): return w * x + b
def fit(X, y): # gradient descent
```
### After
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X, y)
```
