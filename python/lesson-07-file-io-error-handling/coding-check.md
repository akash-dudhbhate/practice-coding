# Lesson 07 — Coding Check

Use this to verify your solutions before asking me to review. Each problem file has its own expected behavior — check against these.

## Easy

### p01-solve.py (read_file)
- [ ] `read_file` on an existing file returns its contents as a string
- [ ] `read_file("nonexistent.txt")` returns `None` (no crash)
- [ ] Uses `with open(...)`

### p02-solve.py (write_file)
- [ ] `write_file("test.txt", "hello")` creates/overwrites the file with `hello`
- [ ] File contains exactly the text written
- [ ] Returns `True` on success
- [ ] Uses `with open(..., "w")`

### p03-solve.py (safe_int)
- [ ] `safe_int("42")` returns `42`
- [ ] `safe_int("abc")` returns `None`
- [ ] `safe_int("")` returns `None`
- [ ] Catches `ValueError`

## Medium

### p01-solve.py (count_lines)
- [ ] On a 3-line file, returns `3`
- [ ] On a missing file, returns `0` (no crash)
- [ ] On an empty file, returns `0`

### p02-solve.py (append_log)
- [ ] Appends `message` + newline to an existing file
- [ ] Creates the file if it doesn't exist
- [ ] Two calls produce two lines
- [ ] Uses `"a"` mode

### p03-solve.py (read_json)
- [ ] On a valid JSON file `{"a": 1}`, returns `{"a": 1}`
- [ ] On a missing file, returns `None`
- [ ] On malformed JSON, returns `None`
- [ ] Uses `json.load`

## Hard

### p01-solve.py (safe_divide)
- [ ] `safe_divide(10, 2)` returns `5.0`
- [ ] `safe_divide(1, 0)` raises `DivideByZeroError`
- [ ] `safe_divide("a", 2)` raises `TypeError`
- [ ] `DivideByZeroError` subclasses `Exception`

### p02-solve.py (process_file)
- [ ] On a file with lines `1`, `2`, `3`, returns `6`
- [ ] Skips blank lines without error
- [ ] Skips non-numeric lines (prints a warning)
- [ ] On missing file, raises `FileNotFoundError` with a clear message

### p03-solve.py (config_loader)
- [ ] On `{"host": "localhost"}`, returns the dict
- [ ] On a config missing `"host"`, raises `ConfigError`
- [ ] On missing file, raises `ConfigError` (not FileNotFoundError)
- [ ] On bad JSON, raises `ConfigError` (not JSONDecodeError)

## How to verify

Create test files in a temp directory and run:
```bash
python easy/p01-solve.py
```

Example JSON test:
```bash
echo '{"host": "localhost"}' > /tmp/cfg.json
python -c "from hard.p03_solve import config_loader; print(config_loader('/tmp/cfg.json'))"
```
