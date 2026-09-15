# Lesson 17 — Coding Check

## Easy

### p01-solve.py — create_db
- [ ] Creates a SQLite database file
- [ ] `users` table has: id (PRIMARY KEY), name (TEXT), email (TEXT), age (INTEGER)
- [ ] Uses `IF NOT EXISTS` (can run multiple times without error)

### p02-solve.py — add_user and get_all_users
- [ ] `add_user` inserts with parameterized query (?, ?, ?)
- [ ] `get_all_users` returns list of users
- [ ] No SQL injection vulnerability (no f-strings in SQL)

### p03-solve.py — find_user_by_email
- [ ] Returns a dict (not tuple) with keys: id, name, email, age
- [ ] Returns None if user not found
- [ ] Uses parameterized query

## Medium

### p01-solve.py — UserManager class
- [ ] `add(name, email, age)` inserts and returns user id
- [ ] `get_by_id(id)` returns user dict or None
- [ ] `update_email(id, new_email)` updates email
- [ ] `delete(id)` removes user
- [ ] `list_all()` returns all users
- [ ] All methods use parameterized queries

### p02-solve.py — Users and Posts with JOIN
- [ ] `posts` table has foreign key to `users`
- [ ] `create_post(user_id, title, content)` inserts a post
- [ ] `get_user_posts(user_id)` returns posts with user name (JOIN)
- [ ] `count_posts_per_user()` returns dict {user_name: post_count}

### p03-solve.py — bulk_insert
- [ ] Uses `executemany` for bulk insert
- [ ] Inserts 100 users
- [ ] Faster than individual inserts (measure and compare)
- [ ] All data is correctly inserted

## Hard

### p01-solve.py — Library system
- [ ] `books` table: id, title, author, borrowed_by (FK to borrowers, nullable)
- [ ] `borrowers` table: id, name, email
- [ ] `add_book(title, author)` adds a book
- [ ] `borrow_book(book_id, borrower_id)` marks book as borrowed
- [ ] `return_book(book_id)` marks book as available
- [ ] `list_available_books()` returns unborrowed books
- [ ] `search_by_title(keyword)` returns matching books (LIKE query)
- [ ] Uses transactions (with statement or commit/rollback)

### p02-solve.py — generate_report
- [ ] Total users count
- [ ] Average age (rounded)
- [ ] Age groups: <20, 20-30, 30+ with counts
- [ ] Most common email domain (e.g., gmail.com)
- [ ] All computed with SQL queries (not Python loops)

### p03-solve.py — Simple ORM
- [ ] `Model` base class with `save()` method
- [ ] `save()` generates INSERT for new rows, UPDATE for existing
- [ ] `User` class extends Model with name, email, age fields
- [ ] Creating a new User and calling `save()` inserts a row
- [ ] Modifying and calling `save()` updates the row
- [ ] Table is auto-created if it doesn't exist
