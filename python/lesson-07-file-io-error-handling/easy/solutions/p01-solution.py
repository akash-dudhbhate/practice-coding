"""SOLUTION: Read File (Easy)"""
def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    with open("/tmp/test_read.txt", "w") as f:
        f.write("hello")
    assert read_file("/tmp/test_read.txt") == "hello"
    assert read_file("/nonexistent") is None
    print("All tests passed!")
