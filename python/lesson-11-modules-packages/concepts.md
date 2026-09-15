# Lesson 11 — Concepts Explained (Modules & Packages)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Module

**What:** A module is a `.py` file containing Python code — functions, classes, variables — that can be imported and reused by other files.

```python
# math_utils.py
def add(a, b): return a + b
PI = 3.14159

# main.py
import math_utils
math_utils.add(2, 3)       # 5
math_utils.PI              # 3.14159

# or import specific names:
from math_utils import add, PI
add(2, 3)                  # 5 (no module prefix needed)
```

**Why it exists:** Without modules, all your code would be in one giant file. Modules let you split code into logical units — `math_utils.py` for math, `file_utils.py` for file operations. This makes code organized, reusable, and maintainable.

**Where it's used:** Every Python project. The standard library itself is a collection of modules (`os`, `sys`, `json`, `datetime`, `random`). Third-party packages (installed via pip) are also modules.

**What goes wrong without it:**
- One 10,000-line file — impossible to navigate, maintain, or debug.
- Code duplication — you rewrite the same function in every project.
- No way to share code between projects or with other developers.
- Name collisions — two functions with the same name in one file → the second overwrites the first.

---

## import Statement

**What:** The `import` statement loads a module and makes its contents available.

```python
import os                    # import whole module
os.getcwd()                  # access via module name

from os import getcwd        # import specific function
getcwd()                     # use directly (no module prefix)

from os import *             # import everything (AVOID THIS)
getcwd()                     # works but pollutes namespace

import os.path as osp        # import with alias
osp.join("a", "b")           # use alias
```

**Why it exists:** `import` is how Python connects code across files. Without it, you'd have to copy-paste code or use `exec()` (which is dangerous and slow).

**Where it's used:** Every Python file that uses code from another file — which is almost every file.

**What goes wrong without it:**
- `from module import *` → pollutes your namespace. If two modules have a function named `utils`, the second import silently overwrites the first. Always use `import module` or `from module import specific_name`.
- Importing a module that doesn't exist → `ModuleNotFoundError`. Check spelling, check if it's installed (`pip install`).
- Circular imports: `a.py` imports `b.py`, `b.py` imports `a.py` → `ImportError`. Restructure to avoid.

---

## from ... import ...

**What:** Import specific names from a module instead of the whole module.

```python
from datetime import datetime, timedelta
now = datetime.now()           # no need for datetime.datetime.now()

from random import randint
randint(1, 10)                 # clean, no prefix
```

**Why it exists:** Typing `datetime.datetime.now()` is verbose. `from ... import` lets you pull out just what you need, making code cleaner.

**Where it's used:** Most Python code. Very common for small, specific imports.

**What goes wrong without it:**
- `from module import *` → imports everything → name collisions, unclear where a name came from.
- Importing a name that doesn't exist → `ImportError: cannot import name 'xyz'`.
- Shadowing builtins: `from time import time` → `time` now refers to the function, not the module → `import time` later fails.

---

## __name__ == "__main__"

**What:** This check lets a Python file work BOTH as a module (imported by others) AND as a script (run directly).

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    # This only runs when you do: python mymodule.py
    # It does NOT run when someone does: import mymodule
    print(greet("World"))
```

- Running `python mymodule.py` → `__name__` is `"__main__"` → the block runs.
- `import mymodule` → `__name__` is `"mymodule"` → the block is skipped.

**Why it exists:** Without this, importing a module would execute all its test/demo code. You want the module's functions available when imported, but you don't want it to print "Hello, World" every time someone imports it.

**Where it's used:** Every well-written Python module. It's the standard way to include test code, CLI entry points, or demos in a module file.

**What goes wrong without it:**
- Importing your module runs all its print statements, test code, and side effects → pollutes the importer's output, slows down imports.
- No way to run the file standalone for testing → you'd need a separate test file.
- Forgetting it → `import mymodule` prints "Hello, World" → confusing for users of your module.

---

## Package (__init__.py)

**What:** A package is a folder of modules. The `__init__.py` file marks the folder as a package and can run initialization code.

```
myproject/
├── __init__.py          # marks myproject as a package
├── utils.py             # myproject.utils
├── models/
│   ├── __init__.py      # marks models as a sub-package
│   ├── user.py          # myproject.models.user
│   └── product.py       # myproject.models.product
```

```python
from myproject.models.user import User
from myproject.utils import helper_function
```

**Why it exists:** Modules are single files. Packages let you organize multiple modules into a folder hierarchy. Without packages, a large project would be a flat directory of 100 `.py` files.

**Where it's used:** Every real Python project. Django apps are packages. Flask blueprints are packages. Installed libraries (numpy, pandas, requests) are packages.

**What goes wrong without it:**
- Missing `__init__.py` → Python doesn't recognize the folder as a package → `ImportError` (in Python 3.3+, namespace packages work without it, but it's still best practice to include it).
- Empty `__init__.py` → works but doesn't expose anything at the package level. Users must import submodules: `from myproject.models.user import User` instead of `from myproject import User`.
- Putting too much code in `__init__.py` → slows down package import, makes it hard to find where things are defined.

---

## pip (Package Installer)

**What:** `pip` is the tool for installing third-party Python packages from PyPI (Python Package Index).

```bash
pip install requests           # install a package
pip install requests==2.28.0   # install specific version
pip install "requests>=2.28"   # install minimum version
pip uninstall requests         # remove a package
pip list                       # show installed packages
pip freeze                     # show installed packages with versions
```

**Why it exists:** Without pip, you'd have to download packages manually, extract them, and place them in the right directory. Pip handles downloading, dependency resolution, and installation automatically.

**Where it's used:** Every time you need a third-party library — `pip install flask`, `pip install numpy`, `pip install requests`.

**What goes wrong without it:**
- Installing without a virtual environment → packages go to the system Python → can break OS tools that depend on Python, or conflict between projects.
- No version pinning → `pip install requests` gets the latest → a new version breaks your code → "it worked yesterday" syndrome.
- `pip install` without `requirements.txt` → can't reproduce the environment on another machine.

---

## Virtual Environments (venv)

**What:** A virtual environment is an isolated Python environment — it has its own Python interpreter and installed packages, separate from the system Python.

```bash
python -m venv myenv          # create virtual environment
source myenv/bin/activate     # activate (Linux/Mac)
myenv\Scripts\activate        # activate (Windows)
pip install requests          # installs into myenv, not system
deactivate                    # exit virtual environment
```

**Why it exists:** Without virtual environments, all projects share the same Python installation. Project A needs Django 3, Project B needs Django 4 → conflict. Virtual environments give each project its own isolated set of packages.

**Where it's used:** Every professional Python project. You should ALWAYS use a virtual environment — never install project dependencies into the system Python.

**What goes wrong without it:**
- System Python gets polluted with project-specific packages → OS tools that depend on Python may break.
- Version conflicts between projects → Project A breaks when you upgrade a package for Project B.
- Can't reproduce the environment → "works on my machine" but not on the server.
- Forgetting to activate → `pip install` goes to system Python → defeats the purpose.

---

## requirements.txt

**What:** A text file listing all packages (with versions) your project needs. Used to reproduce the environment.

```bash
# requirements.txt
requests==2.28.0
flask==2.2.2
numpy>=1.21.0
pandas~=1.5.0   # compatible with 1.5.x
```

```bash
pip install -r requirements.txt   # install all dependencies
pip freeze > requirements.txt      # generate from current env
```

**Why it exists:** Without `requirements.txt`, there's no way to know which packages (and which versions) a project needs. Deploying to a new server or onboarding a new developer would be guesswork.

**Where it's used:** Every Python project that has dependencies. It's the standard way to specify project requirements.

**What goes wrong without it:**
- New developer clones your repo → doesn't know what to install → spends hours guessing.
- Deploy to server → missing packages → crashes in production.
- No version pinning → `pip install -r requirements.txt` gets different versions each time → inconsistent behavior.
- `pip freeze` captures EVERYTHING including unused packages → bloat. Better to manually maintain or use `pip-tools`.

---

## if __name__ guard with CLI

**What:** Using `__name__ == "__main__"` to create a command-line entry point for your module.

```python
# converter.py
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        c = float(sys.argv[1])
        print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
    else:
        print("Usage: python converter.py <celsius>")
```

```bash
python converter.py 25    # 25°C = 77.0°F
```

**Why it exists:** This lets the same file work as both a library (import the function) and a CLI tool (run it directly). No need for a separate CLI file.

**Where it's used:** Utility scripts, data processing tools, any module that has both a programmatic API and a CLI interface.

**What goes wrong without it:**
- Importing the module runs the CLI → tries to read sys.argv → crashes if no arguments provided.
- Can't use the function in other code without triggering the CLI output.
- No usage message → users don't know how to run the script.

---

## Standard Library Overview

**What:** Python comes with a large standard library — modules built into Python that you don't need to install.

Common modules:
```python
import os           # operating system: files, paths, environment
import sys          # system: argv, exit, path
import json         # JSON encoding/decoding
import datetime     # dates and times
import random       # random numbers, choices, shuffling
import math         # math functions: sqrt, pi, sin, cos
import collections  # specialized containers: Counter, defaultdict, deque
import itertools    # iterators: chain, combinations, permutations
import re           # regular expressions
import pathlib      # object-oriented file paths
import typing       # type hints: List, Dict, Optional, Union
```

**Why it exists:** Without a standard library, you'd need to install packages for basic tasks — reading a file, generating random numbers, parsing JSON. The standard library provides these out of the box, making Python immediately useful.

**Where it's used:** Every Python program uses standard library modules. They're the foundation of Python development.

**What goes wrong without it:**
- Reinventing the wheel — writing your own JSON parser instead of `import json`.
- Not knowing what's available → installing third-party packages for things the standard library already does (e.g., `pip install python-dateutil` when `datetime` suffices for basic use).
- Using deprecated modules: `import urllib2` (Python 2) → should be `import urllib.request` (Python 3).

---

## Relative vs Absolute Imports

**What:**
- **Absolute import:** full path from the project root: `from myproject.models.user import User`
- **Relative import:** relative to current file: `from .user import User` (same package) or `from ..models import User` (parent package)

```python
# myproject/models/user.py
from .base import BaseModel       # relative: same package
from ..utils import helper        # relative: parent package
from myproject.utils import helper  # absolute: from project root
```

**Why it exists:** Relative imports are shorter within a package. Absolute imports are clearer and less ambiguous. PEP 8 recommends absolute imports for clarity.

**Where it's used:** Inside packages with multiple modules. Single-file scripts don't need either.

**What goes wrong without it:**
- `from .user import User` outside a package → `ImportError: attempted relative import with no known parent package`.
- Too many `..` in relative imports → hard to understand which package you're referencing.
- Mixing relative and absolute → inconsistent, confusing for other developers.
- Relative imports break if you rename or move the package → absolute imports are more robust.
