# Lesson 17 — Refactoring Challenges

## Refactor 01 (Easy): String SQL Injection Risk
### Before
```python
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
```
### After
```python
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

## Refactor 02 (Medium): No Connection Context
### Before
```python
conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()
cursor.execute("...")
conn.commit()
conn.close()  # might not run if error
```
### After
```python
with sqlite3.connect("db.sqlite") as conn:
    conn.execute("...")
    # auto-commits, auto-closes
```

## Refactor 03 (Hard): Raw SQL Everywhere
### Before
```python
def get_user(id):
    c = conn.execute("SELECT * FROM users WHERE id = ?", (id,))
    return c.fetchone()
def get_post(id):
    c = conn.execute("SELECT * FROM posts WHERE id = ?", (id,))
    return c.fetchone()
```
### After
```python
# Use SQLAlchemy ORM or at least a repository pattern
class Repository:
    def __init__(self, conn, table):
        self.conn = conn
        self.table = table
    def get(self, id):
        return self.conn.execute(
            f"SELECT * FROM {self.table} WHERE id = ?", (id,)
        ).fetchone()
```
