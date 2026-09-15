"""SOLUTION: List .py Files (Medium)"""
import os
from pathlib import Path

def list_py_files(directory="."):
    results = []
    for p in Path(directory).glob("*.py"):
        size = p.stat().st_size
        results.append((str(p), size))
    return results

if __name__ == "__main__":
    for name, size in list_py_files():
        print(f"{name}: {size} bytes")
