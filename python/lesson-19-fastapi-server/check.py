"""
Auto-Check System — Lesson 19 (FastAPI Server)
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
        return None, "No FastAPI 'app' object found"
    from fastapi.testclient import TestClient
    return TestClient(module.app), None


def check_easy_p01(module):
    client, err = _client(module)
    if err:
        return False, err
    r = client.get("/")
    if r.status_code != 200 or r.json() != {"status": "ok"}:
        return False, f"GET / should return {{'status': 'ok'}}, got {r.status_code} {r.text!r}"
    r = client.get("/items/42")
    if r.status_code != 200 or r.json() != {"item_id": 42}:
        return False, f"GET /items/42 should return {{'item_id': 42}}, got {r.text!r}"
    return True, "All tests passed!"


def check_easy_p02(module):
    client, err = _client(module)
    if err:
        return False, err
    if not hasattr(module, 'Product'):
        return False, "Pydantic model 'Product' not found"
    r = client.post("/products", json={"name": "Book", "price": 9.99})
    if r.status_code != 200:
        return False, f"POST /products returned {r.status_code}"
    data = r.json()
    if data.get("name") != "Book" or data.get("price") != 9.99 or data.get("in_stock") is not True:
        return False, f"expected product echo with in_stock default True, got {data!r}"
    r = client.post("/products", json={"name": "X"})  # missing price
    if r.status_code != 422:
        return False, f"invalid body should be 422, got {r.status_code}"
    return True, "All tests passed!"


def check_easy_p03(module):
    client, err = _client(module)
    if err:
        return False, err
    r = client.get("/users")
    if r.json() != {"skip": 0, "limit": 10, "active": True}:
        return False, f"default params wrong: {r.json()!r}"
    r = client.get("/users?skip=5&limit=3&active=false")
    if r.json() != {"skip": 5, "limit": 3, "active": False}:
        return False, f"explicit params wrong: {r.json()!r}"
    return True, "All tests passed!"


def check_medium_p01(module):
    client, err = _client(module)
    if err:
        return False, err
    r = client.post("/todos", json={"title": "Buy milk"})
    if r.status_code not in (200, 201):
        return False, f"POST /todos returned {r.status_code}"
    todos = client.get("/todos").json()
    if len(todos) != 1 or todos[0].get("title") != "Buy milk":
        return False, f"GET /todos should list the new todo, got {todos!r}"
    tid = todos[0].get("id", 1)
    r = client.put(f"/todos/{tid}", json={"title": "Buy oat milk", "done": True})
    if r.status_code != 200:
        return False, f"PUT /todos/{tid} returned {r.status_code}"
    r = client.put("/todos/9999", json={"title": "x"})
    if r.status_code != 404:
        return False, f"PUT missing todo should be 404, got {r.status_code}"
    client.delete(f"/todos/{tid}")
    if client.get("/todos").json() != []:
        return False, "after DELETE, /todos should be empty"
    return True, "All tests passed!"


def check_medium_p02(module):
    client, err = _client(module)
    if err:
        return False, err
    if not hasattr(module, 'get_pagination'):
        return False, "Dependency 'get_pagination' not found"
    r = client.get("/items")
    if r.status_code != 200:
        return False, f"GET /items returned {r.status_code}"
    r = client.get("/items?page=3&size=5")
    data = r.json()
    pag = data.get("pagination", data)
    if pag.get("skip") != 10 or pag.get("limit") != 5:
        return False, f"page=3&size=5 should give skip=10 limit=5, got {data!r}"
    return True, "All tests passed!"


def check_medium_p03(module):
    client, err = _client(module)
    if err:
        return False, err
    for m in ('UserCreate', 'UserResponse'):
        if not hasattr(module, m):
            return False, f"Model '{m}' not found"
    r = client.post("/users", json={"name": "Akash", "email": "a@e.com",
                                    "password": "supersecret"})
    if r.status_code not in (200, 201):
        return False, f"POST /users returned {r.status_code}"
    data = r.json()
    if "password" in data:
        return False, f"response must NOT contain password: {data!r}"
    if data.get("name") != "Akash" or data.get("email") != "a@e.com" or "id" not in data:
        return False, f"response should have id/name/email, got {data!r}"
    return True, "All tests passed!"


def check_hard_p01(module):
    client, err = _client(module)
    if err:
        return False, err
    fd, dbpath = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.remove(dbpath)
    try:
        if hasattr(module, "DB_PATH"):
            module.DB_PATH = dbpath
        if hasattr(module, "init_db"):
            module.init_db()
        r = client.post("/books", json={"title": "Dune", "author": "Herbert", "year": 1965})
        if r.status_code != 201:
            return False, f"POST /books returned {r.status_code}, expected 201"
        r = client.post("/books", json={"title": "Other", "author": "Someone", "year": 2000})
        books = client.get("/books?author=Herbert").json()
        if len(books) != 1 or books[0].get("title") != "Dune":
            return False, f"author filter should return only Dune, got {books!r}"
        r = client.get("/books/1")
        if r.status_code != 200 or r.json().get("title") != "Dune":
            return False, f"GET /books/1 failed: {r.status_code} {r.text!r}"
        if client.get("/books/9999").status_code != 404:
            return False, "GET /books/9999 should be 404"
        r = client.delete("/books/2")
        if r.status_code != 200:
            return False, f"DELETE /books/2 returned {r.status_code}"
        if client.delete("/books/9999").status_code != 404:
            return False, "DELETE missing book should be 404"
        allb = client.get("/books").json()
        if len(allb) != 1:
            return False, f"should have 1 book left, got {allb!r}"
    finally:
        if os.path.exists(dbpath):
            os.remove(dbpath)
    return True, "All tests passed!"


def check_hard_p02(module):
    client, err = _client(module)
    if err:
        return False, err
    r = client.post("/register", json={"username": "u1", "password": "pw"})
    if r.status_code not in (200, 201):
        return False, f"POST /register returned {r.status_code}"
    r = client.post("/login", json={"username": "u1", "password": "wrong"})
    if r.status_code != 401:
        return False, f"login with bad password should be 401, got {r.status_code}"
    r = client.post("/login", json={"username": "u1", "password": "pw"})
    if r.status_code != 200 or "access_token" not in r.json():
        return False, f"login should return access_token, got {r.status_code} {r.text!r}"
    token = r.json()["access_token"]
    if client.get("/me").status_code != 401:
        return False, "GET /me without token should be 401"
    r = client.get("/me", headers={"Authorization": f"Bearer {token}"})
    if r.status_code != 200 or r.json().get("username") != "u1":
        return False, f"GET /me with token should return username, got {r.status_code} {r.text!r}"
    return True, "All tests passed!"


def check_hard_p03(module):
    client, err = _client(module)
    if err:
        return False, err
    r = client.get("/weather/Paris")
    if r.status_code != 200:
        return False, f"GET /weather/Paris returned {r.status_code}"
    data = r.json()
    if data.get("city") != "Paris" or "temp" not in data or "condition" not in data:
        return False, f"weather should have city/temp/condition, got {data!r}"
    r = client.post("/notify", json={"users": ["a", "b", "c"], "message": "hi"})
    if r.status_code != 200:
        return False, f"POST /notify returned {r.status_code}"
    notifs = r.json().get("notifications", [])
    if len(notifs) != 3:
        return False, f"should notify 3 users, got {notifs!r}"
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
        print("  LESSON 19 — AUTO-CHECK ALL")
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
