"""SOLUTION: Read Lines Generator (Hard)"""
def read_lines(filename):
    try:
        with open(filename) as f:
            for line in f:
                yield line.rstrip("\n")
    except FileNotFoundError:
        print(f"Warning: {filename} not found")
        return

if __name__ == "__main__":
    with open("/tmp/test_lines_gen.txt", "w") as f:
        f.write("line1\nline2\nline3\n")
    lines = list(read_lines("/tmp/test_lines_gen.txt"))
    assert lines == ["line1", "line2", "line3"]
    assert list(read_lines("/nonexistent")) == []
    print("All tests passed!")
