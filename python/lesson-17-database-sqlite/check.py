"""
Auto-Check System — Lesson 17 (Database with SQLite)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import sqlite3
import importlib.util


def load_module(filepath):
    spec = importlib.util.spec_from_file_location("solution", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _find_file(level_dir, level, num):
    num_clean = num.lstrip("p")
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    return filepath


def _users_db():
    """Fresh in-memory db with a users table."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                 "name TEXT, email TEXT, age INTEGER)")
    return conn


def check_easy_p01(module):
    if not hasattr(module, 'create_db'):
        return False, "Function 'create_db' not found"
    conn = module.create_db(":memory:")
    try:
        tables = [r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
        if "users" not in tables:
            return False, f"'users' table not created, tables: {tables}"
        cols = [r[1] for r in conn.execute("PRAGMA table_info(users)").fetchall()]
        for col in ("id", "name", "email", "age"):
            if col not in cols:
                return False, f"users table missing column '{col}', has {cols}"
    finally:
        conn.close()
    return True, "All tests passed!"


def check_easy_p02(module):
    for fn in ('add_user', 'get_all_users'):
        if not hasattr(module, fn):
            return False, f"Function '{fn}' not found"
    conn = _users_db()
    try:
        module.add_user(conn, "Alice", "alice@example.com", 30)
        module.add_user(conn, "Bob", "bob@example.com", 25)
        rows = module.get_all_users(conn)
        if len(rows) != 2:
            return False, f"get_all_users should return 2 rows, got {rows!r}"
        flat = str(rows)
        if "Alice" not in flat or "alice@example.com" not in flat:
            return False, f"rows should contain Alice's data, got {rows!r}"
    finally:
        conn.close()
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'find_user_by_email'):
        return False, "Function 'find_user_by_email' not found"
    conn = _users_db()
    try:
        conn.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                     ("Alice", "alice@example.com", 30))
        conn.commit()
        user = module.find_user_by_email(conn, "alice@example.com")
        if not isinstance(user, dict):
            return False, f"should return a dict, got {type(user).__name__}: {user!r}"
        if user.get("name") != "Alice" or user.get("age") != 30:
            return False, f"dict should have name/age fields, got {user!r}"
        if module.find_user_by_email(conn, "nobody@x.com") is not None:
            return False, "unknown email should return None"
    finally:
        conn.close()
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'UserManager'):
        return False, "Class 'UserManager' not found"
    conn = sqlite3.connect(":memory:")
    try:
        mgr = module.UserManager(conn)
        mgr.add("Alice", "alice@example.com", 30)
        mgr.add("Bob", "bob@example.com", 25)
        all_users = mgr.list_all()
        if len(all_users) != 2:
            return False, f"list_all should return 2 users, got {all_users!r}"
        u = mgr.get_by_id(1)
        if not u or u.get("name") != "Alice":
            return False, f"get_by_id(1) should return Alice dict, got {u!r}"
        mgr.update_email(1, "alice@new.com")
        if mgr.get_by_id(1).get("email") != "alice@new.com":
            return False, "update_email did not change the email"
        mgr.delete(2)
        if len(mgr.list_all()) != 1:
            return False, "delete(2) should leave 1 user"
    finally:
        conn.close()
    return True, "All tests passed!"


def check_medium_p02(module):
    for fn in ('setup_db', 'create_post', 'get_posts_by_user', 'count_posts_per_user'):
        if not hasattr(module, fn):
            return False, f"Function '{fn}' not found"
    conn = sqlite3.connect(":memory:")
    try:
        module.setup_db(conn)
        conn.execute("INSERT INTO users (name, email) VALUES ('Alice', 'a@e.com')")
        conn.execute("INSERT INTO users (name, email) VALUES ('Bob', 'b@e.com')")
        conn.commit()
        module.create_post(conn, 1, "Hello World")
        module.create_post(conn, 1, "Second Post")
        module.create_post(conn, 2, "Bob's Post")
        posts = module.get_posts_by_user(conn, 1)
        if len(posts) != 2:
            return False, f"get_posts_by_user(1) should return 2 posts, got {posts!r}"
        counts = {name: cnt for name, cnt in module.count_posts_per_user(conn)}
        if counts.get("Alice") != 2 or counts.get("Bob") != 1:
            return False, f"counts should be Alice=2, Bob=1, got {counts}"
    finally:
        conn.close()
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'bulk_insert'):
        return False, "Function 'bulk_insert' not found"
    conn = _users_db()
    try:
        users = [(f"User{i}", f"user{i}@e.com", 20 + i % 50) for i in range(100)]
        module.bulk_insert(conn, users)
        count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        if count != 100:
            return False, f"should have inserted 100 users, found {count}"
    finally:
        conn.close()
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'Library'):
        return False, "Class 'Library' not found"
    lib = module.Library()
    try:
        lib.add_book("Python 101", "John Doe")
        lib.add_book("Data Science", "Jane Smith")
        lib.conn.execute("INSERT INTO borrowers (name) VALUES ('Alice')")
        lib.conn.commit()
        if len(lib.list_available_books()) != 2:
            return False, "should list 2 available books"
        lib.borrow_book(1, 1)
        avail = lib.list_available_books()
        if len(avail) != 1:
            return False, f"after borrow, 1 book should remain, got {avail!r}"
        found = lib.search_by_title("Data")
        if len(found) != 1:
            return False, f"search_by_title('Data') should find 1 book, got {found!r}"
        try:
            lib.borrow_book(1, 1)
            return False, "borrowing an already-borrowed book should raise"
        except ValueError:
            pass
        lib.return_book(1)
        if len(lib.list_available_books()) != 2:
            return False, "after return, 2 books should be available"
    finally:
        try:
            lib.close()
        except Exception:
            pass
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'generate_report'):
        return False, "Function 'generate_report' not found"
    conn = _users_db()
    try:
        users = [("Alice", "alice@gmail.com", 18),
                 ("Bob", "bob@yahoo.com", 25),
                 ("Charlie", "charlie@gmail.com", 35),
                 ("Diana", "diana@gmail.com", 28)]
        conn.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", users)
        conn.commit()
        report = module.generate_report(conn)
        if report.get("total_users") != 4:
            return False, f"total_users should be 4, got {report!r}"
        if abs(report.get("average_age", 0) - 26.5) > 0.15:
            return False, f"average_age should be ~26.5, got {report!r}"
        ag = report.get("age_groups", {})
        if ag.get("under_20") != 1 or ag.get("20_to_30") != 2 or ag.get("30_plus") != 1:
            return False, f"age_groups should be 1/2/1, got {ag!r}"
        domain = report.get("most_common_domain")
        if "gmail.com" not in str(domain):
            return False, f"most_common_domain should be gmail.com, got {domain!r}"
    finally:
        conn.close()
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'Model'):
        return False, "Class 'Model' not found"
    if not hasattr(module, 'User'):
        return False, "Class 'User' not found"
    conn = _users_db()
    try:
        module.Model.set_connection(conn)
        u = module.User(name="Alice", email="alice@example.com", age=30)
        u.save()
        if not u.id:
            return False, "save() should set id after INSERT"
        row = conn.execute("SELECT name, age FROM users WHERE id = ?",
                           (u.id,)).fetchone()
        if row != ("Alice", 30):
            return False, f"INSERTed row wrong: {row!r}"
        u.age = 31
        u.save()
        row = conn.execute("SELECT age FROM users WHERE id = ?",
                           (u.id,)).fetchone()
        if row[0] != 31:
            return False, "second save() should UPDATE, not re-INSERT"
        count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        if count != 1:
            return False, f"should still be 1 row after update, found {count}"
    finally:
        conn.close()
    return True, "All tests passed!"


CHECKS = {
    "easy/p01": check_easy_p01,
    "easy/p02": check_easy_p02,
    "easy/p03": check_easy_p03,
    "medium/p01": check_medium_p01,
    "medium/p02": check_medium_p02,
    "medium/p03": check_medium_p03,
    "hard/p01": check_hard_p01,
    "hard/p02": check_hard_p02,
    "hard/p03": check_hard_p03,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))

    if target == "all":
        print("=" * 60)
        print("  LESSON 17 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            filepath = _find_file(level_dir, level, num)
            if not os.path.exists(filepath):
                print(f"  {check_id}: FILE NOT FOUND")
                continue
            try:
                module = load_module(filepath)
                passed, msg = check_func(module)
                status = "PASS" if passed else "FAIL"
                print(f"  {check_id}: {status} — {msg}")
            except Exception as e:
                if "NoneType" in str(e):
                    print(f"  {check_id}: FAIL — a function returned None — write the body!")
                else:
                    print(f"  {check_id}: ERROR — {e}")
        print("=" * 60)
        return

    level, num = target.split("/")
    check_id = f"{level}/{num}"
    if check_id not in CHECKS:
        print(f"Error: unknown problem '{check_id}'")
        sys.exit(1)

    filepath = _find_file(level_dir, level, num)
    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    try:
        module = load_module(filepath)
        passed, msg = CHECKS[check_id](module)
        if passed:
            print(f"PASS — {msg}")
            print(f"  Add '# DONE' to the first line of {filepath}")
        else:
            print(f"FAIL — {msg}")
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            print(f"ERROR — {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
