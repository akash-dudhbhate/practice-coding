# Lesson 17 — Database Basics (SQLite)

## What you'll learn
- SQLite database connection and cursor
- CREATE TABLE with constraints
- INSERT, SELECT, UPDATE, DELETE
- Parameterized queries (SQL injection prevention)
- Foreign keys and JOINs
- Context manager for transactions
- ORM introduction

## Lesson

### Connect and create table
```python
import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER)""")
conn.commit()
```

### CRUD operations
```python
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Akash", 25))
cursor.execute("SELECT * FROM users WHERE age > ?", (20,))
cursor.execute("UPDATE users SET age = ? WHERE id = ?", (26, 1))
cursor.execute("DELETE FROM users WHERE id = ?", (1,))
conn.commit()
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Write a function `create_db(db_path)` that creates a SQLite database with a `users` table (id, name, email, age).
2. `easy/p02-solve.py` — Write functions `add_user(conn, name, email, age)` and `get_all_users(conn)` that insert and retrieve users using parameterized queries.
3. `easy/p03-solve.py` — Write a function `find_user_by_email(conn, email)` that returns a single user dict (not tuple) by email.

### Medium
4. `medium/p01-solve.py` — Write a `UserManager` class with methods: add, get_by_id, update_email, delete, list_all. Uses a single connection. All queries are parameterized.
5. `medium/p02-solve.py` — Create two tables: `users` and `posts` (with foreign key). Write functions to: create a post for a user, get all posts by a user (using JOIN), count posts per user.
6. `medium/p03-solve.py` — Write a function `bulk_insert(conn, users_list)` that uses `executemany` to insert 100 users efficiently. Compare timing with individual inserts.

### Hard
7. `hard/p01-solve.py` — Build a `Library` class with books and borrowers tables. Methods: add_book, borrow_book (marks as borrowed), return_book, list_available_books, search_by_title. Use foreign keys and transactions.
8. `hard/p02-solve.py` — Write a function `generate_report(conn)` that generates a summary: total users, average age, users by age group (<20, 20-30, 30+), most common email domain. All using SQL queries.
9. `hard/p03-solve.py` — Write a simple ORM-like class `Model` with a `save()` method that automatically generates INSERT or UPDATE SQL based on whether the row exists. Demonstrate with a User class.

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
- Test with a real SQLite database file.
