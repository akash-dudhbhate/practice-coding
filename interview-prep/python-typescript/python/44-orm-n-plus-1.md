# 44 — Django ORM / SQLAlchemy basics and the N+1 query problem

> **Interview question:** "How does Django ORM / SQLAlchemy simplify DB work? What is the N+1 problem and how do you fix it?"
> **What the interviewer is really testing:** Whether you've actually hit this bug in production — not just "ORM = objects for tables".

## Theory — what it is

An **ORM** (Object-Relational Mapper) is a layer that lets you talk to a relational database using Python objects instead of writing raw SQL strings. A class maps to a table, an instance maps to a row, and an attribute maps to a column. `User.objects.get(id=7)` in Django or `session.get(User, 7)` in SQLAlchemy both emit `SELECT ... WHERE id = 7` under the hood.

The killer feature is **lazy loading**: when you access a related object (like `book.author`), the ORM quietly fires a new SQL query at that moment to fetch it. Convenient — but dangerous in loops.

The **N+1 problem**: you run 1 query to fetch N rows, then the ORM runs N *more* queries — one per row — to fetch each row's related object. N+1 total queries. With 1,000 books you get 1,001 round-trips to the database.

## Why it was needed

Databases are fast at joins; networks are the bottleneck. Each query costs a round-trip (often 0.5–5 ms even on the same machine). A page that lists 500 books with their authors takes ~1 extra query × 500 = seconds of pure waiting.

Without eager loading, the code *looks* clean and works perfectly in dev with 10 rows — then melts in production with 10,000 rows. That's why this is a classic interview question: it separates people who shipped real apps from people who only wrote tutorials.

## Where it's used in a real project

- **List endpoints**: `/api/orders` returning each order with its customer — must `select_related("customer")` or the endpoint does 1 query per order.
- **Admin dashboards**: Django admin listing pages use `list_select_related` for the same reason.
- **Serializers**: DRF/Pydantic serializers that nest related objects trigger lazy loads per item unless the queryset was prepared.
- **Reports/batch jobs**: looping over thousands of rows — always `prefetch_related` the many-to-many/one-to-many sides first.

## Diagram

```
N+1 (lazy loading):
  Query 1:  SELECT * FROM books LIMIT 3;          -> 3 books
  Loop:     book.author.name
  Query 2:  SELECT * FROM authors WHERE id = 10;  \
  Query 3:  SELECT * FROM authors WHERE id = 11;   } 1 per book!
  Query 4:  SELECT * FROM authors WHERE id = 10;  /
  Total: 4 queries for 3 books  (N+1 = 3+1)

Eager fix (select_related = SQL JOIN):
  Query 1:  SELECT b.*, a.* FROM books b
            JOIN authors a ON a.id = b.author_id;
  Total: 1 query. Authors arrive already attached.

Eager fix (prefetch_related = separate IN query):
  Query 1:  SELECT * FROM books;
  Query 2:  SELECT * FROM authors WHERE id IN (10, 11, 10);
  Python stitches them together. Total: 2 queries (constant).
```

## Code — explained

```python
# models.py (Django)
class Author(models.Model):
    name = models.CharField(max_length=100)                    # 1

class Book(models.Model):
    title = models.CharField(max_length=200)                   # 2
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")                       # 3

# --- the slow way: N+1 ---
for book in Book.objects.all():                                # 4
    print(book.title, book.author.name)                        # 5

# --- fix 1: select_related (JOIN, for FK / one-to-one) ---
for book in Book.objects.select_related("author"):             # 6
    print(book.title, book.author.name)                        # 7

# --- fix 2: prefetch_related (IN query, for many-to-many / reverse FK) ---
for book in Book.objects.prefetch_related("tags"):             # 8
    print(book.title, [t.name for t in book.tags.all()])       # 9
```

1. A Django model class = one DB table; `CharField` = a `VARCHAR` column.
2. Each `Book` row gets its own table row.
3. `ForeignKey` = many books → one author (a `author_id` column). `ManyToManyField` = a hidden join table.
4. `Book.objects.all()` runs ONE query — but the queryset is lazy; rows come back with only `author_id` filled in, not the author object.
5. `book.author` triggers a **new SQL query per book**. 1,000 books = 1,000 extra queries.
6. `select_related("author")` tells Django to write a SQL `JOIN` so the author arrives in the same query — total 1 query.
7. `book.author` now reads from memory — zero extra queries.
8. `prefetch_related` runs a second query `WHERE book_id IN (...)` and Python stitches results in memory — good for many-to-many, where a JOIN would explode row count.
9. `book.tags.all()` is also prefetched, so this is free.

**SQLAlchemy equivalent:** `session.query(Book).options(joinedload(Book.author))` for the JOIN version, `selectinload(Book.tags)` for the IN-query version.

## Problems

### Easy — count the queries
**Problem:** Given a list of author IDs fetched lazily, simulate how many DB queries a lazy ORM issues (1 initial + 1 per row) vs an eager `IN` query (2 total). Return `(lazy_count, eager_count)`.
**Try this input:** `[10, 11, 10, 12]`
**Expected output:** `(5, 2)`
**Solution:**
```python
def count_queries(author_ids):
    lazy = 1 + len(author_ids)   # 1 for the books + 1 per book row
    eager = 2                    # books query + one IN() authors query
    return lazy, eager

print(count_queries([10, 11, 10, 12]))  # (5, 2)
```
**Logic explained:**
1. Lazy loading fires one extra query for *every* row, even duplicates (`id=10` twice = two queries, unless the ORM caches — assume no cache here).
2. Eager loading is always 2 queries regardless of N — that's the whole point.

### Medium — detect the N+1
**Problem:** You're given a tiny fake database. Write `authors_of_books_lazy` (one lookup per book) and `authors_of_books_eager` (single batch fetch), and have each return `(result, queries_run)` so you can prove the difference.
**Try this input:** books `[("Dune", 1), ("1984", 2), ("Dune Messiah", 1)]`, authors `{1: "Herbert", 2: "Orwell"}`
**Expected output:** `(['Herbert', 'Orwell', 'Herbert'], 4)` vs `(['Herbert', 'Orwell', 'Herbert'], 2)`
**Solution:**
```python
AUTHORS = {1: "Herbert", 2: "Orwell"}
BOOKS = [("Dune", 1), ("1984", 2), ("Dune Messiah", 1)]

def get_author(author_id, counter):          # pretend each call = 1 SQL query
    counter[0] += 1
    return AUTHORS[author_id]

def lazy():
    c = [1]                                  # the initial SELECT * FROM books
    names = [get_author(aid, c) for _, aid in BOOKS]
    return names, c[0]

def eager():
    c = [1]                                  # initial books query
    ids = {aid for _, aid in BOOKS}
    fetched = {i: get_author(i, c) for i in ids}   # one IN() query = 1 count
    c[0] = 2                                 # batch fetch counts as ONE query
    return [fetched[aid] for _, aid in BOOKS], c[0]

print(lazy())    # (['Herbert', 'Orwell', 'Herbert'], 4)
print(eager())   # (['Herbert', 'Orwell', 'Herbert'], 2)
```
**Logic explained:**
1. `lazy()` calls `get_author` inside the loop — exactly like `book.author` in Django.
2. `eager()` collects the distinct IDs first, does one batch fetch (`WHERE id IN (1,2)`), then maps names in Python — mirroring `prefetch_related`.
3. Both return identical results; only the query count differs. That's the trap: N+1 code is *correct*, just slow.

### Hard — fix real SQL
**Problem:** Using stdlib `sqlite3`, write the N+1 version and the JOIN version of "print each book with its author name" against an in-memory DB, counting statements executed. Show the JOIN version stays at 1 query.
**Try this input:** seed 3 authors, 5 books
**Expected output:** lazy prints 5 books using 6 queries; join prints the same 5 books using 1 query
**Solution:**
```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE authors(id INTEGER PRIMARY KEY, name TEXT)")
db.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, author_id INT)")
db.executemany("INSERT INTO authors VALUES(?, ?)",
               [(1, "Herbert"), (2, "Orwell"), (3, "Le Guin")])
db.executemany("INSERT INTO books VALUES(?, ?, ?)",
               [(1, "Dune", 1), (2, "1984", 2), (3, "Earthsea", 3),
                (4, "Dune Messiah", 1), (5, "Animal Farm", 2)])

queries = [0]
def q(sql, params=()):
    queries[0] += 1
    return db.execute(sql, params)

# --- N+1 version ---
queries[0] = 0
for title, aid in q("SELECT title, author_id FROM books"):
    name = q("SELECT name FROM authors WHERE id=?", (aid,)).fetchone()[0]
    print(title, "->", name)
print("lazy queries:", queries[0])     # 6

# --- JOIN version ---
queries[0] = 0
for title, name in q("""SELECT b.title, a.name FROM books b
                        JOIN authors a ON a.id = b.author_id"""):
    print(title, "->", name)
print("join queries:", queries[0])     # 1
```
**Logic explained:**
1. `q()` wraps `db.execute` and counts every statement — this is what `django.db.connection.queries` or `assertNumQueries` does in a real test.
2. The lazy loop fires `SELECT name FROM authors WHERE id=?` once per row → 1 + 5 = 6.
3. The JOIN pulls both tables in a single statement — the database does the matching, which is what it's optimized for.
4. Same printed output, 6× fewer round-trips. At 5,000 rows the gap is 5,001 vs 1.

## The 30-second interview answer

"An ORM maps tables to classes and rows to objects, so I write Python instead of SQL strings. Its convenience trap is lazy loading: iterating a queryset and touching `obj.related` fires one SQL query per row — that's N+1. I fix it by telling the ORM to fetch relations upfront: `select_related` for foreign keys, which does a SQL JOIN, or `prefetch_related` for many-to-many and reverse relations, which does one `IN` query and stitches in Python. In SQLAlchemy the equivalents are `joinedload` and `selectinload`. I usually catch N+1s by counting queries in tests or watching the SQL log in dev."

## Follow-up trap

**"How do you *detect* an N+1 problem — before it hits prod?"** Good answers: Django's `assertNumQueries(n)` in tests, `connection.queries` logging, the `nplusone`/`django-auto-prefetch` packages, SQLAlchemy `echo=True` to print every statement, or APM tools (Sentry/DataDog) that flag repeated query patterns. Bonus trap: "when would you NOT eager-load?" — when the related object is huge (a `TEXT` blob you don't display) or fetched for thousands of rows you only partially use; eager loading wastes memory. Then `defer()`/`only()` or lazy loading is actually right.
