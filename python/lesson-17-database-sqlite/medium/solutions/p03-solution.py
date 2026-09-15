"""SOLUTION: bulk_insert with executemany (Medium)"""
import sqlite3
import time

def bulk_insert(conn, users_list):
    """Insert many users efficiently using executemany."""
    conn.executemany(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        users_list
    )
    conn.commit()

def individual_insert(conn, users_list):
    """Insert one by one for comparison."""
    for name, email, age in users_list:
        conn.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
    conn.commit()

if __name__ == "__main__":
    users = [(f"User{i}", f"user{i}@e.com", 20 + i % 50) for i in range(100)]

    conn1 = sqlite3.connect(":memory:")
    conn1.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER)")

    start = time.time()
    bulk_insert(conn1, users)
    bulk_time = time.time() - start
    print(f"executemany: {bulk_time:.4f}s")

    conn2 = sqlite3.connect(":memory:")
    conn2.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER)")

    start = time.time()
    individual_insert(conn2, users)
    indiv_time = time.time() - start
    print(f"individual: {indiv_time:.4f}s")
    print(f"Speedup: {indiv_time / bulk_time:.1f}x")
    conn1.close()
    conn2.close()
