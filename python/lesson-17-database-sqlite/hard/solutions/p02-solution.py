"""SOLUTION: generate_report — SQL summary queries (Hard)"""
import sqlite3
from collections import Counter

def generate_report(conn):
    """Generate a summary report using SQL queries."""
    report = {}

    cursor = conn.execute("SELECT COUNT(*) FROM users")
    report["total_users"] = cursor.fetchone()[0]

    cursor = conn.execute("SELECT AVG(age) FROM users")
    report["average_age"] = round(cursor.fetchone()[0] or 0, 1)

    cursor = conn.execute("""
        SELECT
            SUM(CASE WHEN age < 20 THEN 1 ELSE 0 END) as under_20,
            SUM(CASE WHEN age >= 20 AND age < 30 THEN 1 ELSE 0 END) as twenties,
            SUM(CASE WHEN age >= 30 THEN 1 ELSE 0 END) as thirty_plus
        FROM users
    """)
    row = cursor.fetchone()
    report["age_groups"] = {"under_20": row[0], "20_to_30": row[1], "30_plus": row[2]}

    cursor = conn.execute("SELECT email FROM users")
    domains = [email.split("@")[1] if "@" in email else "unknown" for email, in cursor.fetchall()]
    report["most_common_domain"] = Counter(domains).most_common(1)[0] if domains else None

    return report

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER)")
    users = [
        ("Alice", "alice@gmail.com", 18),
        ("Bob", "bob@yahoo.com", 25),
        ("Charlie", "charlie@gmail.com", 35),
        ("Diana", "diana@gmail.com", 28),
    ]
    conn.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", users)
    conn.commit()

    report = generate_report(conn)
    for k, v in report.items():
        print(f"{k}: {v}")
    conn.close()
