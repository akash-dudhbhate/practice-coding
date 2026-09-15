"""SOLUTION: UserManager class (Medium)"""
import sqlite3

class UserManager:
    """Manage users with CRUD operations using parameterized queries."""

    def __init__(self, conn):
        self.conn = conn
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER
            )
        """)
        self.conn.commit()

    def add(self, name, email, age):
        self.conn.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )
        self.conn.commit()

    def get_by_id(self, user_id):
        cursor = self.conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        return {"id": row[0], "name": row[1], "email": row[2], "age": row[3]} if row else None

    def update_email(self, user_id, new_email):
        self.conn.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
        self.conn.commit()

    def delete(self, user_id):
        self.conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

    def list_all(self):
        cursor = self.conn.execute("SELECT * FROM users")
        return [{"id": r[0], "name": r[1], "email": r[2], "age": r[3]} for r in cursor.fetchall()]

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    mgr = UserManager(conn)
    mgr.add("Alice", "alice@example.com", 30)
    mgr.add("Bob", "bob@example.com", 25)
    print(mgr.list_all())
    mgr.update_email(1, "alice@new.com")
    print(mgr.get_by_id(1))
    mgr.delete(2)
    print(mgr.list_all())
    conn.close()
