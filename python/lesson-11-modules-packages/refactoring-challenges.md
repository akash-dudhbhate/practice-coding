# Lesson 11 — Refactoring Challenges

## Refactor 01 (Easy): Wildcard Import
### Before
```python
from math import *
```
### After
```python
import math
# or
from math import sqrt, pi
```

## Refactor 02 (Medium): No __name__ Guard
### Before
```python
# mymodule.py
def main():
    print("Running")
main()  # runs on import!
```
### After
```python
if __name__ == "__main__":
    main()
```

## Refactor 03 (Hard): Flat Structure
### Before
```python
# all files in root: utils.py, db.py, models.py, helpers.py
```
### After
```python
# package structure
# utils/__init__.py, utils/text.py, utils/math.py
# db/__init__.py, db/connection.py
```
