# 30 — `if __name__ == "__main__"`

> **Interview question:** "What does `if __name__ == '__main__'` do, and why do you need it?"
> **What the interviewer is really testing:** Do you understand that importing a module *executes* it, and that `__name__` is how a file can tell "am I being run" from "am I being imported"?

## Theory — what it is

Every Python file gets a built-in variable called `__name__` before any of its code runs. Python sets it to the string `"__main__"` when the file is launched directly (`python script.py`), and to the module's own name (like `"helpers"`) when the file is pulled in via `import helpers`.

So `if __name__ == "__main__":` is a gate: the code inside runs **only** when the file is executed directly, and is skipped when the file is imported. It's how one file can be both a *reusable library* (functions others import) and a *runnable script* (something with a `main` behavior).

Key fact that makes this necessary: **importing a module runs it**. `import helpers` executes every top-level statement in `helpers.py` — every `def`, every `print`, every function call sitting at the top level. The guard lets you keep the `def`s (harmless, they just define functions) while skipping the "do the thing now" part.

## Why it was needed

Without the guard, any top-level code runs on import. Imagine `report.py` that queries a database and emails 10,000 users — sitting at the top level of the file. Now another file does `from report import format_row` just to reuse one helper... and the database gets queried and 10,000 emails go out. Importing should be a safe, side-effect-free operation.

It also prevents a real crash: `multiprocessing` (on macOS/Windows) and tools like `pytest` import your file in a fresh interpreter. If launching work sits at top level, the child process re-runs it and spawns children of its own — an infinite fork bomb. The guard confines "start the program" code to the real entry point.

Finally, it makes files **testable**: test code can `import` your functions without triggering the script's behavior.

## Where it's used in a real project

- **CLI tools / scripts**: `if __name__ == "__main__": main()` so the same file can be run (`python train.py`) and imported (`from train import load_data`).
- **Demo/manual-test blocks**: quick sanity checks at the bottom of a module that run only when you execute the file directly.
- **`multiprocessing` entry points**: mandatory guard so worker processes don't re-execute startup code (spawn method imports the main module).
- **Example code in libraries**: usage examples guarded so they don't fire when users import the package.
- **Runnable packages**: a file literally named `__main__.py` inside a package is what `python -m mypackage` executes — same mechanism, taken one step further.

## A subtle detail: what counts as "top level"

Code inside a `def` or `class` body is safe — it only runs when called (a `class` body *does* run once to build the class, but it shouldn't contain side effects anyway). "Top level" means statements with no indentation: `print(...)`, `x = compute()`, `main()`. Those all fire on import. The rule of thumb while writing a module: **top level should only define things** — functions, classes, constants — never *do* things.

## Diagram

```
$ python greet.py                $ python other.py  (which does: import greet)
        |                                |
   __name__ = "__main__"          __name__ = "greet"
        |                                |
   +----v------------------+      +------v----------------+
   | top-level defs: RUN   |      | top-level defs: RUN   |
   | top-level prints: RUN |      | top-level prints: RUN |  <- import executes code!
   | guard block:     RUN  |      | guard block:   SKIP   |  <- the whole point
   +-----------------------+      +-----------------------+
   "script mode"                  "library mode"
```

## Code — explained

```python
# greet.py
def main():                                      # 1
    print("running as a script")

print("top-level always runs")                   # 2

if __name__ == "__main__":                       # 3
    main()                                       # 4
```

1. `def main():` — defines a function; defining is safe at top level because nothing executes yet.
2. A top-level `print` — this runs on **both** `python greet.py` and `import greet`. Anything at top level executes on import.
3. The guard: `__name__` is `"__main__"` only in the file Python was launched on.
4. `main()` is inside the guard → it runs in script mode, is skipped in library mode.

Actual behavior:

```
$ python greet.py
top-level always runs        <- top-level code runs
running as a script          <- guard passed

$ python -c "import greet"
top-level always runs        <- top-level code still runs (import executes!)
                             <- main() skipped: __name__ was "greet", not "__main__"
```

## Problems

### Easy — one file, two modes
**Problem:** Write a file that defines `double(x)` and prints `double(21)` only when run directly — importing it must print nothing extra.
**Try this input:** `python calc.py` vs `python -c "import calc"`
**Expected output:** `42` when run directly; **nothing** when imported.
**Solution:**
```python
# calc.py
def double(x):
    return x * 2

if __name__ == "__main__":
    print(double(21))
```
**Logic explained:**
1. `double` is defined at top level — safe, since a `def` only creates a function object.
2. The `print` is inside the guard, so it only executes when `__name__ == "__main__"` — i.e., `python calc.py`.
3. On `import calc`, `__name__` is `"calc"`, the guard is `False`, and the import is silent — the file is now a reusable library.

### Medium — see `__name__` change
**Problem:** Write a one-line file that proves `__name__` has a different value depending on how the file is used.
**Try this input:** `python demo.py`, then `python -c "import demo"`
**Expected output:**
```
my __name__ is: __main__     <- direct run
my __name__ is: demo         <- imported
```
**Solution:**
```python
# demo.py
print(f"my __name__ is: {__name__}")
```
**Logic explained:**
1. `__name__` is assigned by Python before the file's code runs — you never set it yourself.
2. Direct run: the launched file is always `"__main__"` (literally that string, not the filename).
3. Import: `__name__` becomes the module name — the filename minus `.py` (here `"demo"`).
4. This single variable is the entire mechanism behind the guard — the `if` is just checking it.

### Hard — refactor a script into a testable program
**Problem:** Turn an untestable script (`a, b = input()`, print the sum) into a proper entry point: a pure `add()` function plus a `main(argv)` that reads command-line arguments and returns an exit code — all launch logic behind the guard.
**Try this input:** `python calc.py 3 4`
**Expected output:** `7.0`
**Solution:**
```python
# calc.py
import sys

def add(a: float, b: float) -> float:
    return a + b

def main(argv: list[str]) -> int:
    a, b = float(argv[1]), float(argv[2])   # argv[0] is the script name
    print(add(a, b))
    return 0                                # 0 = success

if __name__ == "__main__":
    sys.exit(main(sys.argv))
```
**Logic explained:**
1. `sys.argv` is the list of command-line words; `sys.argv[0]` is the script's own name, so the numbers are at indexes 1 and 2.
2. `add()` is pure — no I/O, no globals — so tests can call `add(3, 4)` without touching `argv`.
3. `main(argv)` takes the argument list as a *parameter* instead of reading the global `sys.argv` directly — now tests can call `main(["calc.py", "1", "2"])` and check the return code.
4. `sys.exit(main(sys.argv))` turns `main`'s return value into the process exit code (`0` = success). The guard ensures none of this runs on `import calc`.
5. Pattern summary: **keep top level clean** (defs only), put behavior in `main()`, call `main()` under the guard.

## The 30-second interview answer

"`__name__` is a variable Python sets for every module: it's `'__main__'` in the file you launched directly, and the module's own name when the file is imported. Since importing executes all top-level code, the guard marks the section that should only run in script mode — so one file can be both an importable library and a runnable program. It's also required for `multiprocessing` on platforms that spawn workers by re-importing the main module, otherwise the startup code would recursively re-run."

## Follow-up trap

**"Does importing a module run its code?"** — Yes, exactly once (Python caches modules in `sys.modules`; a second `import` returns the cached module without re-running). This is the fact the whole question rests on — top-level code always executes on first import; the guard only decides whether the *guarded* part also runs.

**"What happens if you put `multiprocessing` code at top level without the guard?"** — On Windows/macOS the default start method is `spawn`: each child process re-imports your main module to find the target function. Without the guard, the child re-executes the code that creates processes → children spawn children → fork bomb. That's why the docs say the entry point *must* be behind `if __name__ == "__main__"`. (On Linux the default `fork` method copies memory instead of re-importing, so it often "works" there and explodes only in production on another OS.)
