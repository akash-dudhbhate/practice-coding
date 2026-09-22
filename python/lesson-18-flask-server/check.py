"""
Auto-Check System — Lesson 18 (Flask Server)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import tempfile
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


def _client(module):
    if not hasattr(module, 'app'):
        return None, "No Flask 'app' object found"
    return module.app.test_client(), None


def check_easy_p01(module):
    client, err = _client(module)
    if err:
        return False, err
    for path, needle in [("/", "Home"), ("/about", "About"), ("/contact", "Contact")]:
        r = client.get(path)
        if r.status_code != 200:
            return False, f"GET {path} returned {r.status_code}, expected 200"
        if needle.lower() not in r.data.decode().lower():
            return False, f"GET {path} body should mention '{needle}'"
    return True, "All tests passed!"


def check_easy_p02(module):
    client, err = _client(module)
    if err:
        return False, err
    r = client.get("/api/greet/Akash")
    if r.status_code != 200:
        return False, f"GET /api/greet/Akash returned {r.status_code}"
    if r.get_json() != {"message": "Hello, Akash"}:
        return False, f"expected {{'message': 'Hello, Akash'}}, got {r.get_json()!r}"
    return True, "All tests passed!"


def check_easy_p03(module):
    client, err = _client(module)
    if err:
        return False, err
    r = client.get("/api/search?q=python")
    if r.status_code != 200:
        return False, f"GET /api/search returned {r.status_code}"
    data = r.get_json()
    if data.get("query") != "python" or data.get("results") != []:
        return False, f"expected {{'query': 'python', 'results': []}}, got {data!r}"
    return True, "All tests passed!"


def check_medium_p01(module):
    client, err = _client(module)
    if err:
        return False, err
    r = client.post("/todos", json={"title": "Buy milk"})
    if r.status_code != 201:
        return False, f"POST /todos returned {r.status_code}, expected 201"
    r = client.get("/todos")
    todos = r.get_json()
    if not isinstance(todos, list) or len(todos) != 1 or todos[0].get("title") != "Buy milk":
        return False, f"GET /todos should list the new todo, got {todos!r}"
    todo_id = todos[0].get("id", 1)
    r = client.delete(f"/todos/{todo_id}")
    if r.status_code != 204:
        return False, f"DELETE /todos/{todo_id} returned {r.status_code}, expected 204"
    if client.get("/todos").get_json() != []:
        return False, "after delete, /todos should be empty"
    return True, "All tests passed!"


def check_medium_p02(module):
    client, err = _client(module)
    if err:
        return False, err
    if client.get("/dashboard").status_code != 401:
        return False, "GET /dashboard before login should be 401"
    r = client.post("/login", json={"username": "admin", "password": "password123"})
    if r.status_code != 200:
        return False, f"POST /login with valid creds returned {r.status_code}"
    r = client.get("/dashboard")
    if r.status_code != 200 or r.get_json().get("user") != "admin":
        return False, f"dashboard after login should show admin, got {r.get_json()!r}"
    client.get("/logout")
    if client.get("/dashboard").status_code != 401:
        return False, "GET /dashboard after logout should be 401"
    return True, "All tests passed!"


def check_medium_p03(module):
    client, err = _client(module)
    if err:
        return False, err
    r = client.get("/api/items")
    if r.status_code != 200 or not isinstance(r.get_json(), dict):
        return False, f"GET /api/items should be 200 JSON, got {r.status_code}"
    r = client.post("/api/items", json={"name": "x"})
    if r.status_code != 201:
        return False, f"POST /api/items returned {r.status_code}, expected 201"
    r = client.post("/auth/login", json={"u": "a"})
    if r.status_code != 200:
        return False, f"POST /auth/login returned {r.status_code}"
    r = client.post("/auth/register", json={"u": "a"})
    if r.status_code != 200:
        return False, f"POST /auth/register returned {r.status_code}"
    return True, "All tests passed!"


def check_hard_p01(module):
    client, err = _client(module)
    if err:
        return False, err
    # point the app's DB at a temp file and init it if supported
    fd, dbpath = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.remove(dbpath)
    try:
        if hasattr(module, "DB_PATH"):
            module.DB_PATH = dbpath
        if hasattr(module, "init_db"):
            module.init_db()
        r = client.post("/posts", json={"title": "Hi", "content": "Body", "tag": "py"})
        if r.status_code != 201:
            return False, f"POST /posts returned {r.status_code}, expected 201"
        r = client.get("/posts?tag=py")
        posts = r.get_json()
        if not isinstance(posts, list) or len(posts) != 1:
            return False, f"GET /posts?tag=py should return 1 post, got {posts!r}"
        if client.get("/posts?tag=other").get_json() != []:
            return False, "tag filter should return [] for unknown tag"
        post_id = posts[0].get("id", 1)
        r = client.post(f"/posts/{post_id}/comments", json={"text": "Nice!"})
        if r.status_code != 201:
            return False, f"POST comment returned {r.status_code}, expected 201"
        r = client.get("/definitely-not-a-route")
        if r.status_code != 404:
            return False, "unknown route should be 404"
        r = client.delete(f"/posts/{post_id}")
        if r.status_code != 204:
            return False, f"DELETE /posts/{post_id} returned {r.status_code}"
    finally:
        if os.path.exists(dbpath):
            os.remove(dbpath)
    return True, "All tests passed!"


def check_hard_p02(module):
    client, err = _client(module)
    if err:
        return False, err
    r = client.get("/")
    if r.status_code != 200:
        return False, f"GET / returned {r.status_code}"
    r = client.post("/new", data={"title": "First", "content": "Hello"})
    if r.status_code not in (200, 302):
        return False, f"POST /new returned {r.status_code}"
    body = client.get("/").data.decode()
    if "First" not in body:
        return False, "index page should list the new post 'First'"
    r = client.get("/post/1")
    if r.status_code != 200 or "Hello" not in r.data.decode():
        return False, "GET /post/1 should show the post content"
    return True, "All tests passed!"


def check_hard_p03(module):
    client, err = _client(module)
    if err:
        return False, err
    if not hasattr(module, 'require_auth'):
        return False, "Decorator 'require_auth' not found"
    r = client.get("/api/protected")
    if r.status_code != 401:
        return False, f"GET /api/protected without key should be 401, got {r.status_code}"
    r = client.get("/api/protected", headers={"X-API-Key": "secret123"})
    if r.status_code != 200 or r.get_json().get("data") != "secret":
        return False, f"with API key should return secret data, got {r.status_code} {r.get_json()!r}"
    # hammer to trigger rate limiting (whatever the exact limit is)
    codes = [client.get("/api/protected", headers={"X-API-Key": "secret123"}).status_code
             for _ in range(6)]
    if 429 not in codes:
        return False, f"rate limiter should eventually return 429, got {codes}"
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
        print("  LESSON 18 — AUTO-CHECK ALL")
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
