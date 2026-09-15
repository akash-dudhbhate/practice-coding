# Lesson 11 — Debug Exercises

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
