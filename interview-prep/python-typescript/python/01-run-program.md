# 01 — What happens when you run a Python program?

> **Interview question:** "What happens when you run `python app.py`?"
> **What the interviewer is really testing:** Whether you know Python compiles to bytecode first, and that a virtual machine — not the OS — executes it.

## Theory — what it is

When you type `python app.py`, the CPython interpreter does **not** read your file line-by-line and execute the text. Instead it runs a two-stage pipeline. Stage one: **compile** your human-readable source into **bytecode** — a set of low-level numeric instructions like `LOAD_FAST`, `BINARY_OP`, `CALL`. Stage two: a loop called the **Python Virtual Machine (PVM)** fetches each bytecode instruction and executes it, one at a time.

The compile stage itself has sub-steps: the **tokenizer** splits the raw text into tokens (`NAME`, `NUMBER`, `OP`...), the **parser** arranges tokens into an **AST** (abstract syntax tree — a tree of the program's structure), and the **compiler** walks the tree and emits bytecode stored in a **code object** (`my_func.__code__`).

Two practical consequences: (1) the whole file is checked for syntax errors *before* a single line runs — that's why a typo on line 500 kills the program instantly, even though line 1 never executed. (2) Bytecode gets cached in `__pycache__/app.cpython-3XX.pyc`; on the next run, if the source file's timestamp/hash is unchanged, CPython skips compilation and loads the `.pyc` directly.

"Bytecode" is just CPython's own instruction set — portable across operating systems but **not** across Python versions (a 3.11 `.pyc` won't run on 3.12).

## Why it was needed

Why not interpret the text directly? Because parsing text is expensive and must be repeated for every line of every loop iteration — early interpreters did exactly that and were dog-slow. Compiling once means the PVM loop works on compact integers instead of re-parsing `total = price * qty` a million times.

The bytecode layer also decouples "what the language means" from "how it runs": Python-the-language targets bytecode, and *any* VM that understands it can run it (PyPy, Jython, MicroPython all reuse the front-end idea). It also gives a clean hook for tooling — `dis` for disassembly, coverage tools, debuggers that map bytecode offsets back to source lines.

## Where it's used in a real project

- **`__pycache__` directories** appear in every repo — that's the compile cache. Deployment Docker images often pre-compile with `python -m compileall` for faster cold starts.
- **`dis` module** for debugging performance mysteries — e.g., checking whether a "fast" comprehension actually generates less bytecode than a loop.
- **`compile()` / `exec()` / `eval()`** builtins expose the pipeline directly — used by templating engines, DSLs, REPLs, Jupyter kernels.
- **Packaging tools** (PyInstaller, zipapp) ship `.pyc` bytecode instead of source; linters like `ast`/`flake8` stop at the AST stage.

## Diagram

```
 app.py (source text)
      |
      v
 [Tokenizer]  -->  tokens:  NAME(x) OP(=) NUMBER(1) ...
      |
      v
 [Parser]     -->  AST:     Assign(target=x, value=1)
      |
      v
 [Compiler]   -->  code object: bytecode bytes + consts + names
      |                    \
      |                     \__> cached to __pycache__/app.cpython-3XX.pyc
      v
 +------------------------------------------+
 | PVM (Python Virtual Machine)             |
 |   loop: fetch instr -> decode -> execute |
 |   LOAD_CONST 1   STORE_NAME x   ...      |
 +------------------------------------------+
      |
      v
   output
```

## Code — explained

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)                     # human-readable bytecode
print(add.__code__.co_consts)    # (None,) — constants in the code object
print(add.__code__.co_varnames)  # ('a', 'b') — local variable names
print(add.__code__.co_argcount)  # 2 — number of positional params

# compile() runs the front half of the pipeline yourself:
code = compile("x * 2 + 1", "<demo>", "eval")   # -> a code object
x = 5
print(eval(code))                               # 11
```

1. `dis.dis(add)` prints the bytecode instructions the PVM will run — you'll see ops like `LOAD_FAST a`, `LOAD_FAST b`, `BINARY_ADD`/`BINARY_OP`, `RETURN_VALUE`.
2. `__code__` is the compiled code object — the actual product of the compile stage. It holds the bytecode bytes plus metadata (`co_consts`, `co_varnames`, `co_argcount`).
3. `compile(src, filename, mode)` manually does tokenize→parse→compile and returns a code object; `"eval"` mode means "single expression," `"exec"` means statements.
4. `eval(code)` hands the code object to the PVM — exactly what happens when CPython runs your file, minus the caching.

## Problems

### Easy — syntax gate
**Problem:** Write `is_valid(source)` that returns `True` if the source compiles, `False` if it has a `SyntaxError` — without executing it.
**Try this input:** `is_valid("x = 1 + 2")` and `is_valid("x = 1 +")`
**Expected output:**
```
True
False
```
**Solution:**
```python
def is_valid(source):
    try:
        compile(source, "<check>", "exec")
        return True
    except SyntaxError:
        return False

print(is_valid("x = 1 + 2"))
print(is_valid("x = 1 +"))
```
**Logic explained:**
1. `compile()` runs the full front-end (tokenize → parse → bytecode) but returns before the PVM executes anything.
2. A bad program fails at compile time, raising `SyntaxError` — exactly what CPython does before running your script.
3. `"<check>"` is just a fake filename used in error messages.

### Medium — compile once, run many
**Problem:** Given the expression `"x * x + 1"`, compile it **once**, then evaluate it for `x = 1, 2, 3, 4`. Print all results on one line.
**Try this input:** `x` in `range(1, 5)`
**Expected output:** `2 5 10 17`
**Solution:**
```python
code = compile("x * x + 1", "<expr>", "eval")
results = []
for x in range(1, 5):
    results.append(eval(code))
print(*results)
```
**Logic explained:**
1. `compile(..., "eval")` turns the string into a code object once — this is the expensive step (tokenizing + parsing) done a single time.
2. Each `eval(code)` reuses the compiled bytecode; only the variable `x` changes. This is why template engines compile a template once and render it thousands of times.
3. `print(*results)` unpacks the list into space-separated output.

### Hard — tiny bytecode VM
**Problem:** Implement `run(program)` — a mini stack-machine interpreter (your own PVM). Instructions: `("PUSH", n)` pushes `n`; `"ADD"`, `"SUB"`, `"MUL"` pop two values and push the result; `"PRINT"` pops and prints. Run the program `PUSH 6, PUSH 7, MUL, PUSH 8, ADD, PRINT`.
**Try this input:** `[("PUSH", 6), ("PUSH", 7), ("MUL",), ("PUSH", 8), ("ADD",), ("PRINT",)]`
**Expected output:** `50`
**Solution:**
```python
def run(program):
    stack = []
    for instr in program:
        op = instr[0]
        if op == "PUSH":
            stack.append(instr[1])
        elif op == "ADD":
            stack.append(stack.pop() + stack.pop())
        elif op == "MUL":
            stack.append(stack.pop() * stack.pop())
        elif op == "SUB":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif op == "PRINT":
            print(stack.pop())

run([("PUSH", 6), ("PUSH", 7), ("MUL",), ("PUSH", 8), ("ADD",), ("PRINT",)])
```
**Logic explained:**
1. CPython's PVM is a **stack machine**: most instructions push or pop an operand stack instead of naming registers — this mirrors it exactly.
2. `PUSH 6`, `PUSH 7` leave `[6, 7]`; `MUL` pops both and pushes `42` → `[42]`; `PUSH 8` → `[42, 8]`; `ADD` → `[50]`; `PRINT` emits `50`.
3. Order matters for non-commutative ops: `SUB` pops `b` (top) then `a`, computing `a - b`.
4. Your `for` loop is the "fetch → decode → execute" cycle — the literal core of the interpreter.

## The 30-second interview answer

"Running `python app.py` is two stages. First CPython compiles the source: it tokenizes the text, parses it into an AST, and compiles that into bytecode — a low-level instruction set — stored in code objects and cached in `__pycache__/*.pyc` so re-runs skip compilation. Second, the Python Virtual Machine executes the bytecode one instruction at a time in a fetch-decode-execute loop. Because the whole file compiles up front, syntax errors surface before anything executes, and because it's bytecode — not machine code — Python is portable but slower than compiled languages. You can see the bytecode yourself with the `dis` module."

## Follow-up trap

**"So Python is interpreted — is it ever compiled?"** The honest answer: it *is* compiled, just to bytecode rather than machine code — "interpreted vs compiled" isn't binary. Traps they may add: `.pyc` files are version-specific (not portable across 3.11/3.12); sourceless execution (`python` can run a `.pyc` directly); and PyPy/Cython/Numba JIT-compile hot paths to real machine code. If asked *"does importing compile too?"* — yes, imports trigger the same compile-and-cache pipeline, which is why a `SyntaxError` in an unused module still kills your program.
