"""SOLUTION: ThreadPoolExecutor (Medium)"""
from concurrent.futures import ThreadPoolExecutor
import time

def download(filename):
    time.sleep(0.2)  # simulate download
    return f"Downloaded {filename}"

if __name__ == "__main__":
    files = [f"file_{i}.zip" for i in range(5)]
    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(download, files))
    elapsed = time.time() - start
    assert len(results) == 5
    assert elapsed < 1.0  # should be ~0.2, not 1.0
    print(f"Downloaded 5 files in {elapsed:.2f}s — tests passed!")
