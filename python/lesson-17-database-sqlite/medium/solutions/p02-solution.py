"""SOLUTION: users and posts with foreign key + JOIN (Medium)"""
import sqlite3

def setup_db(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    conn.execute("""CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )""")
    conn.commit()

def create_post(conn, user_id, title):
    conn.execute("INSERT INTO posts (user_id, title) VALUES (?, ?)", (user_id, title))
    conn.commit()

def get_posts_by_user(conn, user_id):
    cursor = conn.execute("""
        SELECT u.name, p.title FROM posts p
        JOIN users u ON p.user_id = u.id WHERE u.id = ?
    """, (user_id,))
    return cursor.fetchall()

def count_posts_per_user(conn):
    cursor = conn.execute("""
        SELECT u.name, COUNT(p.id) as post_count FROM users u
        LEFT JOIN posts p ON u.id = p.user_id
        GROUP BY u.id
    """)
    return cursor.fetchall()

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    setup_db(conn)
    conn.execute("INSERT INTO users (name, email) VALUES ('Alice', 'a@e.com')")
    conn.execute("INSERT INTO users (name, email) VALUES ('Bob', 'b@e.com')")
    conn.commit()
    create_post(conn, 1, "Hello World")
    create_post(conn, 1, "Second Post")
    create_post(conn, 2, "Bob's Post")
    print(get_posts_by_user(conn, 1))
    print(count_posts_per_user(conn))
    conn.close()
