"""SOLUTION: Fixture with yield (Medium)"""
import pytest
import os
import tempfile

@pytest.fixture
def temp_file():
    fd, path = tempfile.mkstemp(suffix=".txt")
    os.close(fd)
    with open(path, "w") as f:
        f.write("test content")
    yield path
    if os.path.exists(path):
        os.remove(path)

def test_read_temp_file(temp_file):
    with open(temp_file) as f:
        content = f.read()
    assert content == "test content"

if __name__ == "__main__":
    fd, path = tempfile.mkstemp(suffix=".txt")
    os.close(fd)
    with open(path, "w") as f:
        f.write("test content")
    with open(path) as f:
        assert f.read() == "test content"
    os.remove(path)
    print("All tests passed!")
