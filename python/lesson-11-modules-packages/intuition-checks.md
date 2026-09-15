# Lesson 11 — Intuition Checks

## Check 01: __name__
```python
# mymodule.py
print(__name__)
```
What prints when run directly vs imported?
<details><summary>Answer</summary>
- Run directly: `__main__`
- Imported: `mymodule`
This is why `if __name__ == "__main__":` works — it only runs when executed directly.
</details>

## Check 02: Import Variations
```python
import math
from math import sqrt
from math import *
```
What's the difference?
<details><summary>Answer</summary>
- `import math` — use as `math.sqrt(4)`
- `from math import sqrt` — use as `sqrt(4)`
- `from math import *` — imports everything, pollutes namespace. AVOID.
</details>

## Check 03: __init__.py
What does an empty `__init__.py` do?
<details><summary>Answer</summary>
Marks a directory as a Python package. Without it (in older Python), the directory isn't importable. In Python 3.3+, namespace packages work without it, but explicit `__init__.py` is still recommended.
</details>

## Check 04: Module Search Path
```python
import sys
print(sys.path[0])
```
What prints when you run `python script.py`?
<details><summary>Answer</summary>
The directory containing `script.py` — Python adds the script's directory to `sys.path` first. This is why local modules are found.
</details>

## Check 05: Reload
```python
import mymodule
# edit mymodule.py
import mymodule  # does this reload?
```
<details><summary>Answer</summary>
No — `import` only loads once. Subsequent imports return the cached module. Use `importlib.reload(mymodule)` to reload.
</details>
