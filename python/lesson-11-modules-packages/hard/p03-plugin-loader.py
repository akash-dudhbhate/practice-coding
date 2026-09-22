"""
LESSON 11 — Modules & Packages
HARD P03 — Plugin Loader
============================================

CONCEPT:
  A plugin system loads code at runtime instead of import time.
  `importlib.util.spec_from_file_location` + `module_from_spec` +
  `spec.loader.exec_module(mod)` let you turn any .py file on disk into
  a live module object — the trick behind plugin architectures.

PROBLEM:
  Write `load_plugins(plugins_dir)` that scans a directory for `.py`
  files (skip names starting with "_"), dynamically loads each as a
  module, and returns a list of the modules that define a `run()`
  function. Return an empty list if the directory does not exist.

TRY THIS INPUT:
  ```python
  # given plugins/hello.py containing:  def run(): return "hi"
  plugins = load_plugins("plugins")
  for p in plugins:
      print(p.run())
  ```

EXPECTED OUTPUT:
  ```
  hi
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
