# Lesson 17 — Concepts Explained (Database Basics — SQLite)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## SQLite

**What:** SQLite is a lightweight, file-based database. No server needed — the entire database is one file. Python has it built in (`import sqlite3`).

```python
import sqlite3

# Connect to a database file (creates it if it doesn't exist)
conn = sqlite3.connect("myapp.db")

# Create a cursor to execute SQL
cursor = conn.cursor()

# Execute SQL
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Commit changes
conn.commit()

# Close connection
conn.close()
```

**Why it exists:** Without a database, you'd store data in text files — no querying, no relationships, no concurrency. SQLite gives you SQL power without installing a database server. Perfect for apps, prototypes, and small-to-medium projects.

**Where it's used:** Mobile apps (Android, iOS), desktop apps, browsers (Chrome stores history in SQLite), embedded systems, testing, small web apps, data analysis.

**What goes wrong without it:**
- Storing data in plain text files → no queries (find all users over 25 requires reading the entire file), no relationships, no transactions.
- Using SQLite for high-concurrency write-heavy apps → only one writer at a time → lock contention. Use PostgreSQL for those cases.
- Forgetting `conn.commit()` → changes are lost when the connection closes.

---

## CREATE TABLE

**What:** `CREATE TABLE` defines the structure of a table — columns, types, constraints.

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
```

Key constraints:
- `PRIMARY KEY` — unique identifier for each row
- `NOT NULL` — column must have a value
- `UNIQUE` — no two rows can have the same value
- `DEFAULT` — default value if not specified
- `AUTOINCREMENT` — automatically increment the ID

**Why it exists:** Without table definitions, data has no structure — any row could have any columns → chaos. `CREATE TABLE` enforces a schema so data is consistent.

**Where it's used:** Every database table. The first step in any database project.

**What goes wrong without it:**
- No `IF NOT EXISTS` → running CREATE twice → `sqlite3.OperationalError: table already exists`.
- No `NOT NULL` on critical fields → rows with missing data → bugs in your app.
- Wrong column type → SQLite is flexible (allows any type in any column) but other databases aren't → porting issues.

---

## INSERT

**What:** `INSERT` adds rows to a table.

```python
# Single insert
cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
               ("Akash", "akash@example.com", 25))

# Multiple inserts
users = [("Bob", "bob@example.com", 30), ("Carol", "carol@example.com", 28)]
cursor.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", users)

conn.commit()    # DON'T FORGET!
```

**Why it exists:** Without INSERT, tables are empty — useless. INSERT is how data enters the database.

**Where it's used:** Every time you save data — user registration, form submission, data import, logging.

**What goes wrong without it:**
- **SQL INJECTION**: `cursor.execute(f"INSERT INTO users VALUES ('{name}')")` → if name is `'); DROP TABLE users;--` → your table is deleted. ALWAYS use parameterized queries `VALUES (?, ?, ?)`.
- Forgetting `conn.commit()` → data appears to be inserted but disappears when the program closes.
- `executemany` vs `execute` in a loop → `executemany` is much faster for bulk inserts.

---

## SELECT

**What:** `SELECT` reads data from a table.

```python
# All rows
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()    # list of tuples

# Specific columns
cursor.execute("SELECT name, email FROM users")
rows = cursor.fetchall()    # [("Akash", "akash@example.com"), ...]

# With WHERE clause
cursor.execute("SELECT * FROM users WHERE age > 25")
rows = cursor.fetchall()

# Single row
cursor.execute("SELECT * FROM users WHERE id = 1")
row = cursor.fetchone()    # single tuple or None

# Sorted and limited
cursor.execute("SELECT * FROM users ORDER BY name LIMIT 10")
```

**Why it exists:** Without SELECT, you can't read data. SELECT is the most common SQL operation — it's how you query, filter, sort, and limit data.

**Where it's used:** Every data retrieval — displaying users, searching, generating reports, analytics.

**What goes wrong without it:**
- `SELECT *` → returns all columns → if table has 50 columns and you need 2 → wasteful. Select only what you need.
- `fetchall()` on a million-row table → loads everything into memory → crash. Use `fetchone()` in a loop or `LIMIT`.
- SQL injection in WHERE: `WHERE name = '{user_input}'` → use `WHERE name = ?` with parameters.

---

## UPDATE

**What:** `UPDATE` modifies existing rows.

```python
# Update specific row
cursor.execute("UPDATE users SET age = 26 WHERE id = 1")

# Update multiple fields
cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?",
               ("New Name", "new@example.com", 1))

# Update with condition
cursor.execute("UPDATE users SET age = age + 1 WHERE age < 30")

conn.commit()
```

**Why it exists:** Without UPDATE, data can only be inserted, never changed. Users can't update their profiles, prices can't be adjusted, statuses can't be changed.

**Where it's used:** Profile updates, status changes, price adjustments, data corrections.

**What goes wrong without it:**
- **Forgetting WHERE clause**: `UPDATE users SET age = 30` → ALL users become 30 → data disaster. Always include WHERE.
- Forgetting `commit()` → changes lost.
- No row count check: `cursor.rowcount` tells you how many rows were updated. If 0 → no matching row → maybe the ID doesn't exist.

---

## DELETE

**What:** `DELETE` removes rows from a table.

```python
# Delete specific row
cursor.execute("DELETE FROM users WHERE id = 1")

# Delete with condition
cursor.execute("DELETE FROM users WHERE age < 18")

# Delete all rows (DANGER!)
cursor.execute("DELETE FROM users")    # everything gone!

conn.commit()
```

**Why it exists:** Without DELETE, data accumulates forever — old accounts, expired records, test data. DELETE lets you remove data that's no longer needed.

**Where it's used:** Account deletion, data cleanup, removing expired records, GDPR compliance (right to be forgotten).

**What goes wrong without it:**
- **Forgetting WHERE clause**: `DELETE FROM users` → ALL data gone → catastrophic. Always use WHERE.
- No backup → deleted data is gone permanently. Consider soft deletes (a `deleted_at` column) instead of hard deletes.
- Not checking `rowcount` → you think you deleted a row but it didn't exist → silent failure.

---

## Parameterized Queries (Preventing SQL Injection)

**What:** Use `?` placeholders instead of string formatting. The database safely escapes the values.

```python
# GOOD — parameterized (safe)
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))

# BAD — string formatting (SQL INJECTION VULNERABLE)
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
# If name = "'; DROP TABLE users;--" → your table is DELETED
```

**Why it exists:** Without parameterized queries, user input is directly inserted into SQL → malicious users can inject SQL commands → delete tables, steal data, bypass auth. This is the #1 web security vulnerability (SQL injection).

**Where it's used:** EVERY query that includes user input. No exceptions.

**What goes wrong without it:**
- SQL injection → data theft, data deletion, full database compromise.
- Even if you think input is safe, it might not be — always parameterize.
- Using `%` formatting or f-strings for SQL → same vulnerability. Only `?` placeholders are safe.

---

## Foreign Keys & Relationships

**What:** Foreign keys link tables together — a column in one table references the primary key of another.

```python
cursor.execute("""
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")

# Query with JOIN
cursor.execute("""
    SELECT posts.title, users.name
    FROM posts
    JOIN users ON posts.user_id = users.id
""")
```

**Why it exists:** Without relationships, data is isolated — posts don't know who wrote them, orders don't know who placed them. Foreign keys create connections between tables, modeling real-world relationships.

**Where it's used:** Any multi-table database — users and posts, customers and orders, students and courses.

**What goes wrong without it:**
- No foreign key → orphaned rows: a post with `user_id = 999` but no user 999 → data inconsistency.
- Forgetting to enable foreign keys in SQLite: `conn.execute("PRAGMA foreign_keys = ON")` → SQLite doesn't enforce FKs by default!
- N+1 query problem: fetching 100 posts, then querying the user for each → 101 queries. Use JOIN instead → 1 query.

---

## Context Manager (with statement)

**What:** Use `with` to automatically commit/rollback and close connections.

```python
# Automatic commit on success, rollback on exception
with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Akash",))
    # commit happens automatically when the with block exits

# Note: the connection is NOT closed by the with statement
# You still need to close it:
conn.close()

# Or use a helper:
from contextlib import closing
with closing(sqlite3.connect("myapp.db")) as conn:
    with conn:    # transaction
        conn.execute("INSERT INTO users (name) VALUES (?)", ("Akash",))
```

**Why it exists:** Without the context manager, an exception between `execute` and `commit` → partial data saved → inconsistent state. `with` ensures atomicity — all or nothing.

**Where it's used:** Every database operation in production code. Never use raw `connect()` without error handling.

**What goes wrong without it:**
- Exception during insert → no rollback → half the data saved → corrupted state.
- Forgetting to close the connection → connection leak → database locked.
- `with sqlite3.connect()` does NOT close the connection — it only manages the transaction. Use `closing()` for that.

---

## ORM Introduction

**What:** An ORM (Object-Relational Mapper) lets you interact with the database using Python objects instead of raw SQL.

```python
# Raw SQL (what you've been doing)
cursor.execute("SELECT * FROM users WHERE age > 25")
users = cursor.fetchall()

# With SQLAlchemy ORM
users = session.query(User).filter(User.age > 25).all()
for user in users:
    print(user.name)    # attribute access, not dict keys
```

**Why it exists:** Without an ORM, you write SQL strings everywhere — SQL in Python code is verbose, error-prone, and not type-safe. ORMs map tables to classes, rows to objects, making database code feel like regular Python.

**Where it's used:** Django ORM (Django), SQLAlchemy (most Python frameworks), Peewee (lightweight), Tortoise ORM (async).

**What goes wrong without it:**
- Raw SQL everywhere → SQL injection risk (if not parameterized), repetitive, hard to maintain.
- ORM can generate inefficient queries (N+1 problem) → slow. Understand what SQL the ORM generates.
- ORM abstraction leaks → complex queries are hard in ORM → you drop to raw SQL anyway.
