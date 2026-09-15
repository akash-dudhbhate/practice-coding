"""SOLUTION: Requirements Generator (Hard)"""
import sys
import importlib

# Standard library modules set (Python 3.10+)
STDLIB = {
    "os", "sys", "re", "json", "math", "random", "time", "datetime",
    "collections", "itertools", "functools", "pathlib", "typing",
    "io", "csv", "sqlite3", "urllib", "http", "email", "hashlib",
    "base64", "logging", "argparse", "subprocess", "threading",
    "multiprocessing", "asyncio", "abc", "copy", "enum", "warnings",
}

def extract_imports(filepath):
    """Extract third-party imports from a Python file."""
    third_party = set()
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line.startswith("import "):
                module = line.split()[1].split(".")[0]
            elif line.startswith("from "):
                module = line.split()[1].split(".")[0]
            else:
                continue
            if module not in STDLIB and module != "__future__":
                third_party.add(module)
    return sorted(third_party)

if __name__ == "__main__":
    # Self-test: this file has no third-party imports
    result = extract_imports(__file__)
    assert result == [], f"Expected empty, got {result}"
    print("All tests passed!")
