"""SOLUTION: Library class with transactions (Hard)"""
import sqlite3

class Library:
    """Library system with books and borrowers using foreign keys and transactions."""

    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self._setup()

    def _setup(self):
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY, title TEXT, author TEXT, borrowed INTEGER DEFAULT 0
            );
            CREATE TABLE IF NOT EXISTS borrowers (
                id INTEGER PRIMARY KEY, name TEXT
            );
            CREATE TABLE IF NOT EXISTS loans (
                id INTEGER PRIMARY KEY,
                book_id INTEGER, borrower_id INTEGER,
                FOREIGN KEY (book_id) REFERENCES books(id),
                FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
            );
        """)
        self.conn.commit()

    def add_book(self, title, author):
        self.conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        self.conn.commit()

    def borrow_book(self, book_id, borrower_id):
        try:
            self.conn.execute("BEGIN")
            book = self.conn.execute("SELECT borrowed FROM books WHERE id = ?", (book_id,)).fetchone()
            if not book:
                raise ValueError("Book not found")
            if book[0]:
                raise ValueError("Book already borrowed")
            self.conn.execute("UPDATE books SET borrowed = 1 WHERE id = ?", (book_id,))
            self.conn.execute("INSERT INTO loans (book_id, borrower_id) VALUES (?, ?)", (book_id, borrower_id))
            self.conn.execute("COMMIT")
        except Exception:
            self.conn.execute("ROLLBACK")
            raise

    def return_book(self, book_id):
        self.conn.execute("UPDATE books SET borrowed = 0 WHERE id = ?", (book_id,))
        self.conn.execute("DELETE FROM loans WHERE book_id = ?", (book_id,))
        self.conn.commit()

    def list_available_books(self):
        cursor = self.conn.execute("SELECT id, title, author FROM books WHERE borrowed = 0")
        return cursor.fetchall()

    def search_by_title(self, keyword):
        cursor = self.conn.execute("SELECT id, title, author FROM books WHERE title LIKE ?", (f"%{keyword}%",))
        return cursor.fetchall()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    lib = Library()
    lib.add_book("Python 101", "John Doe")
    lib.add_book("Data Science", "Jane Smith")
    lib.conn.execute("INSERT INTO borrowers (name) VALUES ('Alice')")
    lib.conn.commit()
    lib.borrow_book(1, 1)
    print("Available:", lib.list_available_books())
    print("Search 'Python':", lib.search_by_title("Python"))
    lib.return_book(1)
    print("After return:", lib.list_available_books())
    lib.close()
