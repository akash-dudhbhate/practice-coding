"""SOLUTION: Count Lines (Medium)"""
def count_lines(path):
    try:
        with open(path, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

if __name__ == "__main__":
    with open("/tmp/test_lines.txt", "w") as f:
        f.write("line1\nline2\nline3\n")
    assert count_lines("/tmp/test_lines.txt") == 3
    assert count_lines("/nonexistent") == 0
    print("All tests passed!")
