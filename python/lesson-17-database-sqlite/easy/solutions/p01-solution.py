"""SOLUTION: create_db — create SQLite database with users table (Easy)"""
import sqlite3

def create_db(db_path):
    """Create a SQLite database with a users table."""
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()
    return conn

if __name__ == "__main__":
    conn = create_db("test.db")
    print("Database created!")
    conn.close()
