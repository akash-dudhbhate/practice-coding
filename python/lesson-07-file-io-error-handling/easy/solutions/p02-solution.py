"""SOLUTION: Write File (Easy)"""
def write_file(path, text):
    try:
        with open(path, "w") as f:
            f.write(text)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    assert write_file("/tmp/test_write.txt", "content") == True
    assert read_file := open("/tmp/test_write.txt").read() == "content"
    print("All tests passed!")
