# Lesson 20 — Intuition Checks

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
