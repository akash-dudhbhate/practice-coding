"""SOLUTION: add_user and get_all_users — parameterized queries (Easy)"""
import sqlite3

def add_user(conn, name, email, age):
    """Insert a user using parameterized query."""
    conn.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        (name, email, age)
    )
    conn.commit()

def get_all_users(conn):
    """Retrieve all users."""
    cursor = conn.execute("SELECT id, name, email, age FROM users")
    return cursor.fetchall()

if __name__ == "__main__":
    conn = sqlite3.connect("test.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER)")
    add_user(conn, "Alice", "alice@example.com", 30)
    add_user(conn, "Bob", "bob@example.com", 25)
    print(get_all_users(conn))
    conn.close()
