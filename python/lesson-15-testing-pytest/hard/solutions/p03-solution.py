"""SOLUTION: process_csv with Tests (Hard)"""
import pytest
import csv
import os
import tempfile

def process_csv(filepath):
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

@pytest.fixture
def temp_csv():
    fd, path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        writer.writerow(["Akash", "25"])
        writer.writerow(["Dev", "30"])
    yield path
    os.remove(path)

def test_normal_read(temp_csv):
    data = process_csv(temp_csv)
    assert len(data) == 2
    assert data[0]["name"] == "Akash"

def test_empty_file():
    fd, path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    with open(path, "w") as f:
        f.write("")
    data = process_csv(path)
    assert data == []
    os.remove(path)

if __name__ == "__main__":
    # Manual test
    fd, path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "age"])
        w.writerow(["Akash", "25"])
    data = process_csv(path)
    assert data[0]["name"] == "Akash"
    os.remove(path)
    print("All tests passed!")
