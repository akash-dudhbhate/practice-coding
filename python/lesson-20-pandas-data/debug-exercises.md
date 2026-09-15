# Lesson 20 — Debug Exercises

## Debug 01 (Easy): Missing Main Guard
```python
# app.py
def main():
    app.run()

main()  # runs on import!
```
<details><summary>Answer</summary>
**Bug:** `main()` runs when module is imported.
**Fix:** `if __name__ == "__main__": main()`.
</details>

## Debug 02 (Medium): Config Hardcoded
```python
def connect():
    return sqlite3.connect("/home/user/app.db")
```
<details><summary>Answer</summary>
**Bug:** Path is hardcoded — breaks on other machines.
**Fix:** Use config file or environment variable.
</details>

## Debug 03 (Hard): No Error Handling in Pipeline
```python
def pipeline(data):
    cleaned = clean(data)
    transformed = transform(cleaned)
    return analyze(transformed)
```
<details><summary>Answer</summary>
**Bug:** If any step fails, the entire pipeline crashes with no context.
**Fix:** Add try/except at each step with logging, or use a pipeline library.
</details>
