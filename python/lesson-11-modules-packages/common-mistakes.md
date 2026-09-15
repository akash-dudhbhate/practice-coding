# Lesson 11 — Common Mistakes

## Mistake 01: Using `from module import *`
```python
# WRONG — pollutes namespace
from math import *

# CORRECT — explicit imports
import math
# or
from math import sqrt, pi
```

## Mistake 02: No `if __name__ == "__main__":` guard
```python
# WRONG — runs on import
def main(): ...
main()

# CORRECT
if __name__ == "__main__":
    main()
```

## Mistake 03: Circular imports
```python
# a.py imports b.py which imports a.py → ImportError
# Fix: move imports inside functions, or restructure
```

## Mistake 04: Not organizing into packages
```python
# WRONG — all files in root
project/
  main.py
  utils.py
  helpers.py

# CORRECT — package structure
project/
  main.py
  utils/
    __init__.py
    helpers.py
```

## Mistake 05: Hardcoding paths
```python
# WRONG
with open("/home/user/data.txt") as f: ...

# CORRECT — use relative paths or pathlib
from pathlib import Path
data_path = Path(__file__).parent / "data.txt"
```
