"""
Auto-Check System — Lesson 16 (REST APIs)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all

Note: HTTP calls are MOCKED — no network access needed.
"""

import os
import sys
import glob
import tempfile
import importlib.util
from unittest.mock import patch, MagicMock


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


class FakeResp:
    """Minimal requests.Response stand-in for mocked calls."""
    def __init__(self, data=None, status=200, headers=None, chunks=None):
        self._data = data
        self.status_code = status
        self.headers = headers or {}
        self.content = b"x" if data is not None else b""
        self._chunks = chunks or []

    def json(self):
        return self._data

    def raise_for_status(self):
        if self.status_code >= 400:
            import requests
            raise requests.HTTPError(f"HTTP {self.status_code}")

    def iter_content(self, chunk_size=8192):
        return iter(self._chunks)


def check_easy_p01(module):
    if not hasattr(module, 'get_user'):
        return False, "Function 'get_user' not found"
    with patch("requests.get", return_value=FakeResp({"name": "Linus Torvalds"})) as mock_get:
        result = module.get_user("torvalds")
    if result.get("name") != "Linus Torvalds":
        return False, f"get_user should return the parsed JSON dict, got {result!r}"
    if "users/torvalds" not in str(mock_get.call_args):
        return False, "should GET https://api.github.com/users/{username}"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'get_repos'):
        return False, "Function 'get_repos' not found"
    fake = [{"name": "linux"}, {"name": "subsurface"}]
    with patch("requests.get", return_value=FakeResp(fake)):
        result = module.get_repos("torvalds")
    if result != ["linux", "subsurface"]:
        return False, f"get_repos should return ['linux', 'subsurface'], got {result!r}"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'search_joke'):
        return False, "Function 'search_joke' not found"
    fake = {"setup": "Why did the chicken", "punchline": "to cross the road"}
    with patch("requests.get", return_value=FakeResp(fake)):
        result = module.search_joke()
    if "Why did the chicken" not in str(result) or "cross the road" not in str(result):
        return False, f"search_joke should combine setup + punchline, got {result!r}"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'get_all_repos'):
        return False, "Function 'get_all_repos' not found"
    page1 = [{"name": f"repo{i}"} for i in range(100)]
    page2 = [{"name": "last1"}, {"name": "last2"}]
    with patch("requests.get", side_effect=[FakeResp(page1), FakeResp(page2)]):
        result = module.get_all_repos("someuser")
    if len(result) != 102:
        return False, f"get_all_repos should follow pagination and return 102 names, got {len(result)}"
    if result[-1] != "last2":
        return False, "should include repos from later pages"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'create_issue'):
        return False, "Function 'create_issue' not found"
    with patch("requests.post", return_value=FakeResp({"number": 42}, status=201)):
        result = module.create_issue("me", "repo", "Bug", "details", "TOKEN")
    if result.get("number") != 42:
        return False, f"create_issue should return parsed JSON, got {result!r}"
    with patch("requests.post", return_value=FakeResp({"msg": "bad"}, status=401)):
        try:
            module.create_issue("me", "repo", "Bug", "details", "BAD")
            return False, "401 response should raise an exception (ValueError)"
        except ValueError:
            pass
        except Exception as e:
            if "NoneType" in str(e):
                print(f"FAIL — a function returned None — write the body!")
            else:
                return False, f"401 raised {type(e).__name__}, expected ValueError"
    return True, "All tests passed!"


def check_medium_p03(module):
    import requests
    if not hasattr(module, 'fetch_with_retry'):
        return False, "Function 'fetch_with_retry' not found"
    with patch("time.sleep"):
        with patch("requests.get",
                   side_effect=[requests.Timeout(), requests.Timeout(),
                                FakeResp({"ok": True})]):
            result = module.fetch_with_retry("https://x.test")
    if result != {"ok": True}:
        return False, f"fetch_with_retry should succeed after 2 timeouts, got {result!r}"
    with patch("time.sleep"):
        with patch("requests.get", side_effect=requests.Timeout()):
            try:
                module.fetch_with_retry("https://x.test", max_retries=2)
                return False, "should raise after exhausting retries"
            except Exception:
                pass
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'APIClient'):
        return False, "Class 'APIClient' not found"
    client = module.APIClient("https://api.test", token="t123")
    for m in ("get", "post", "put", "delete"):
        if not hasattr(client, m):
            return False, f"APIClient.{m}() not found"
    auth = client.session.headers.get("Authorization", "")
    if "t123" not in auth:
        return False, "session should carry Authorization header with the token"
    with patch.object(client.session, "request",
                      return_value=FakeResp({"ok": 1})) as mock_req:
        out = client.get("/things")
    if out != {"ok": 1}:
        return False, f"client.get should return parsed JSON, got {out!r}"
    called = str(mock_req.call_args)
    if "api.test/things" not in called:
        return False, f"should request base_url + path, got {called}"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'download_large_file'):
        return False, "Function 'download_large_file' not found"
    fake = FakeResp(headers={"content-length": "6"}, chunks=[b"abc", b"def"])
    path = tempfile.mktemp()
    try:
        with patch("requests.get", return_value=fake):
            out = module.download_large_file("https://x.test/file", path)
        with open(path, "rb") as f:
            content = f.read()
        if content != b"abcdef":
            return False, f"file should contain b'abcdef', got {content!r}"
        if out != path:
            return False, "should return the filepath"
    finally:
        if os.path.exists(path):
            os.remove(path)
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'scrape_api'):
        return False, "Function 'scrape_api' not found"
    page1 = [{"id": i} for i in range(100)]
    page2 = [{"id": 100}, {"id": 101}]
    with patch("time.sleep"):
        with patch("requests.get",
                   side_effect=[FakeResp(page1), FakeResp(page2)]):
            result = module.scrape_api("https://x.test", "items")
    if len(result) != 102:
        return False, f"scrape_api should return 102 items across pages, got {len(result)}"
    # 429 handling: first response rate-limited, then a short page
    with patch("time.sleep"):
        with patch("requests.get", side_effect=[
                FakeResp(status=429, headers={"Retry-After": "0"}),
                FakeResp([{"id": 1}])]):
            result2 = module.scrape_api("https://x.test", "items")
    if len(result2) != 1:
        return False, "should retry after a 429 and still collect results"
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
        print("  LESSON 16 — AUTO-CHECK ALL")
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
