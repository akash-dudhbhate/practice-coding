"""
Auto-Check System — Lesson 14 (Async & Concurrency)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import io
import time
import asyncio
import contextlib
import importlib.util


def load_module(filepath):
    spec = importlib.util.spec_from_file_location("solution", filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module.__name__] = module  # so pools can pickle its functions
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


def check_easy_p01(module):
    if not hasattr(module, 'async_greet'):
        return False, "Async function 'async_greet' not found"
    result = asyncio.run(module.async_greet("Akash"))
    if result != "Hello, Akash!":
        return False, f"async_greet('Akash') should return 'Hello, Akash!', got {result!r}"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'start_end'):
        return False, "Async function 'start_end' not found"
    buf = io.StringIO()
    start = time.time()
    with contextlib.redirect_stdout(buf):
        asyncio.run(module.start_end())
    elapsed = time.time() - start
    out = buf.getvalue()
    if "Start" not in out or "End" not in out:
        return False, f"start_end() should print 'Start' then 'End', got {out!r}"
    if not (0.4 < elapsed < 0.9):
        return False, f"start_end() should take ~0.5s, took {elapsed:.2f}s"
    return True, "All tests passed!"


def check_easy_p03(module):
    for fn in ('task1', 'task2', 'main'):
        if not hasattr(module, fn):
            return False, f"Async function '{fn}' not found"
    start = time.time()
    results = asyncio.run(module.main())
    elapsed = time.time() - start
    if results != ["task1 done", "task2 done"]:
        return False, f"main() should return ['task1 done', 'task2 done'], got {results!r}"
    if elapsed >= 0.75:
        return False, f"tasks ran serially ({elapsed:.2f}s) — use asyncio.gather for concurrency"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'fetch_all'):
        return False, "Async function 'fetch_all' not found"
    urls = ["https://a.com", "https://b.com", "https://c.com"]
    start = time.time()
    results = asyncio.run(module.fetch_all(urls))
    elapsed = time.time() - start
    if not isinstance(results, (list, tuple)) or len(results) != 3:
        return False, f"fetch_all should return 3 results, got {results!r}"
    if "a.com" not in str(results[0]):
        return False, f"first result should mention a.com, got {results[0]!r}"
    if elapsed >= 0.25:
        return False, f"fetches look serial ({elapsed:.2f}s) — use asyncio.gather"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'download'):
        return False, "Function 'download' not found"
    if module.download("file_0.zip") != "Downloaded file_0.zip":
        return False, "download('file_0.zip') should return 'Downloaded file_0.zip'"
    from concurrent.futures import ThreadPoolExecutor
    files = [f"file_{i}.zip" for i in range(5)]
    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(module.download, files))
    elapsed = time.time() - start
    if len(results) != 5:
        return False, "should download 5 files"
    if elapsed >= 0.9:
        return False, f"downloads look serial ({elapsed:.2f}s) — use a thread pool"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'square'):
        return False, "Function 'square' not found"
    if module.square(5) != 25:
        return False, "square(5) should be 25"
    sys.modules[module.__name__] = module  # make square picklable for workers
    from concurrent.futures import ProcessPoolExecutor
    nums = list(range(1, 21))
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(module.square, nums))
    if results != [n * n for n in nums]:
        return False, "process pool should compute squares of 1..20"
    return True, "All tests passed!"


def check_hard_p01(module):
    for fn in ('limited_task', 'main'):
        if not hasattr(module, fn):
            return False, f"Async function '{fn}' not found"
    results = asyncio.run(module.main())
    if sorted(results) != list(range(10)):
        return False, f"main() should complete all 10 tasks, got {results!r}"
    return True, "All tests passed!"


def check_hard_p02(module):
    for fn in ('fetch_with_timeout', 'scrape_all'):
        if not hasattr(module, fn):
            return False, f"Async function '{fn}' not found"
    urls = [f"https://api{i}.example.com" for i in range(5)]
    results = asyncio.run(module.scrape_all(urls))
    if len(results) != 5:
        return False, f"scrape_all should return 5 results, got {len(results)}"
    if not all("OK" in str(r) for r in results):
        return False, f"all results should be OK, got {results!r}"
    return True, "All tests passed!"


def check_hard_p03(module):
    for fn in ('producer', 'consumer', 'main'):
        if not hasattr(module, fn):
            return False, f"Async function '{fn}' not found"
    try:
        total = asyncio.run(asyncio.wait_for(module.main(), timeout=10))
    except asyncio.TimeoutError:
        return False, "main() timed out — consumers may never stop (sentinels?)"
    if total != 10:
        return False, f"main() should return 10 items processed, got {total!r}"
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
        print("  LESSON 14 — AUTO-CHECK ALL")
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
