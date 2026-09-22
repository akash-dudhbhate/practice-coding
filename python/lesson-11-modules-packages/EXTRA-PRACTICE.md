# lesson-11-modules-packages — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Circular Import
```python
# a.py
from b import greet
def hello(): greet()

# b.py
from a import hello
def greet(): print("Hi!")
```
<details><summary>Answer</summary>
**Bug:** Circular import — a imports b which imports a. Python can't resolve this.
**Fix:** Move the import inside the function, or restructure modules to avoid the cycle.
</details>

## Debug 02 (Medium): Wrong Import Path
```python
from utils.helper import format_text
```
**Hint:** File is at `utils/helpers/format_text.py`

<details><summary>Answer</summary>
**Bug:** Path is wrong — `helper` vs `helpers`, and `format_text` is a module not a function.
**Fix:** `from utils.helpers import format_text` (import the module) then use `format_text.format_text()`.
</details>

## Debug 03 (Hard): __name__ Check Missing
```python
# mymodule.py
def main():
    print("Running")

main()  # runs on import!

# test.py
import mymodule  # prints "Running" — unwanted side effect
```
<details><summary>Answer</summary>
**Bug:** `main()` runs on import because there's no `if __name__ == "__main__":` guard.
**Fix:** `if __name__ == "__main__": main()`.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

## Problem: Organize a Project

### Approach 1: Flat structure
```
project/
  main.py
  utils.py
  db.py
  models.py
```
**Cons:** Hard to find things as project grows.

### Approach 2: Package structure
```
project/
  __init__.py
  main.py
  utils/
    __init__.py
    text.py
    math.py
  db/
    __init__.py
    connection.py
```
**Pros:** Scalable, clear organization.

**Winner:** Approach 2 — packages scale better.
