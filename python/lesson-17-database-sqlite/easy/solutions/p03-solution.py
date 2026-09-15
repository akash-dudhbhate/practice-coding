"""SOLUTION: find_user_by_email — return dict (Easy)"""
import sqlite3

def find_user_by_email(conn, email):
    """Return a single user as a dict by email, or None."""
    cursor = conn.execute(
        "SELECT id, name, email, age FROM users WHERE email = ?",
        (email,)
    )
    row = cursor.fetchone()
    if row is None:
        return None
    return {"id": row[0], "name": row[1], "email": row[2], "age": row[3]}

if __name__ == "__main__":
    conn = sqlite3.connect("test.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER)")
    conn.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", ("Alice", "alice@example.com", 30))
    conn.commit()
    user = find_user_by_email(conn, "alice@example.com")
    print(user)
    conn.close()
