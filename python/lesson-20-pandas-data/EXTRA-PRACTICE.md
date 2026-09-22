# lesson-20-pandas-data — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Project Structure
What goes in `__init__.py`?
<details><summary>Answer</summary>
Package initialization code, public API exports. Can be empty. Example: `from .models import User` makes `User` available as `package.User`.
</details>

## Check 02: Separation of Concerns
Why separate data, logic, and presentation?
<details><summary>Answer</summary>
Each can change independently. Swap database without touching UI. Change UI without touching logic. Test logic without database.
</details>

## Check 03: Configuration
```python
# Why is this bad?
DB_PATH = "/home/user/data.db"
```
<details><summary>Answer</summary>
Hardcoded path breaks on other machines. Use env vars: `os.getenv("DB_PATH", "default.db")`.
</details>

## Check 04: Logging vs Print
Why use logging instead of print?
<details><summary>Answer</summary>
Logging has levels (DEBUG, INFO, WARNING, ERROR), can go to files, can be formatted, can be disabled in production. Print is for user output only.
</details>

## Check 05: Type Hints in Production
```python
def process(data: list[dict]) -> dict[str, int]:
    ...
```
<details><summary>Answer</summary>
Type hints document the contract, enable IDE support and mypy checking. Essential for production code.
</details>

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: Everything in one file
```python
# WRONG — 1000-line main.py
# CORRECT — split into modules
project/
  models.py
  services.py
  views.py
  main.py
```

## Mistake 02: Hardcoded configuration
```python
# WRONG
API_URL = "https://api.example.com"

# CORRECT
API_URL = os.getenv("API_URL", "https://default.example.com")
```

## Mistake 03: No error handling
```python
# WRONG — crashes on any error
def process(data):
    return transform(clean(data))

# CORRECT — graceful degradation
def process(data):
    try:
        return transform(clean(data))
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        return None
```

## Mistake 04: No documentation
```python
# WRONG — no docstring
def process(data): ...

# CORRECT
def process(data: list[dict]) -> dict[str, int]:
    """Process raw data into summary statistics.

    Args:
        data: List of raw records.
    Returns:
        Summary dict mapping category to count.
    """
```

## Mistake 05: No tests
```python
# Always write tests for critical functions
def test_process():
    assert process([{"cat": "a"}]) == {"a": 1}
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Iterrows for Transformation
### Before
```python
for idx, row in df.iterrows():
    df.loc[idx, "double"] = row["value"] * 2
```
### After
```python
df["double"] = df["value"] * 2
```

## Refactor 02 (Medium): Chained Indexing
### Before
```python
df[df["age"] > 18]["category"] = "adult"
```
### After
```python
df.loc[df["age"] > 18, "category"] = "adult"
```

## Refactor 03 (Hard): Multiple Intermediate Variables
### Before
```python
filtered = df[df["age"] > 18]
filtered = filtered[filtered["income"] > 50000]
filtered["tax"] = filtered["income"] * 0.2
result = filtered.groupby("city")["tax"].mean()
```
### After
```python
result = (df
    .query("age > 18 and income > 50000")
    .assign(tax=lambda x: x["income"] * 0.2)
    .groupby("city")["tax"]
    .mean()
)
```

---

## Approach Comparison — different ways to solve it

## Problem: Project Structure

### Approach 1: Flat
```
project/
  main.py
  utils.py
  models.py
```
**Cons:** Hard to navigate as project grows.

### Approach 2: Layered
```
project/
  main.py
  config.py
  models/
    __init__.py
    user.py
    product.py
  services/
    __init__.py
    auth.py
    email.py
  views/
    __init__.py
    user_view.py
```
**Pros:** Clear separation, scalable.

**Winner:** Approach 2 — scales with project size.

---

## Problem: Configuration Management

### Approach 1: Constants file
```python
# config.py
DB_URL = "postgresql://..."
API_KEY = "abc123"
```
**Cons:** Can't change without redeploying. Secrets in code.

### Approach 2: Environment variables
```python
# config.py
import os
DB_URL = os.environ["DB_URL"]
API_KEY = os.environ["API_KEY"]
```
**Pros:** 12-factor app compliant. Secrets not in code.

### Approach 3: pydantic Settings
```python
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    db_url: str
    api_key: str
    class Config:
        env_file = ".env"
```
**Pros:** Type validation, .env support, defaults.

**Winner:** Approach 3 (pydantic) for production. Approach 2 for simple projects.
