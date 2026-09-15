"""SOLUTION: Simple ORM-like Model class (Hard)"""
import sqlite3

class Model:
    """Base model with save() that auto-generates INSERT or UPDATE."""

    table_name = None
    fields = []

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        for field in self.fields:
            setattr(self, field, kwargs.get(field))

    @classmethod
    def set_connection(cls, conn):
        cls._conn = conn

    def save(self):
        if self.id:
            self._update()
        else:
            self._insert()

    def _insert(self):
        values = [getattr(self, f) for f in self.fields]
        placeholders = ", ".join(["?"] * len(self.fields))
        columns = ", ".join(self.fields)
        cursor = self._conn.execute(
            f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})",
            values
        )
        self._conn.commit()
        self.id = cursor.lastrowid

    def _update(self):
        set_clause = ", ".join([f"{f} = ?" for f in self.fields])
        values = [getattr(self, f) for f in self.fields] + [self.id]
        self._conn.execute(
            f"UPDATE {self.table_name} SET {set_clause} WHERE id = ?",
            values
        )
        self._conn.commit()

class User(Model):
    table_name = "users"
    fields = ["name", "email", "age"]

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, age INTEGER)")
    Model.set_connection(conn)

    user = User(name="Alice", email="alice@example.com", age=30)
    user.save()
    print(f"Created user with id={user.id}")

    user.age = 31
    user.save()
    cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user.id,))
    print("After update:", cursor.fetchone())
    conn.close()
