"""SOLUTION: Process File (Hard)"""
def process_file(path):
    try:
        with open(path, "r") as f:
            total = 0
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    total += int(line)
                except ValueError:
                    print(f"Warning: skipping non-numeric line: {line}")
            return total
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")

if __name__ == "__main__":
    with open("/tmp/test_nums.txt", "w") as f:
        f.write("10\n20\n\nabc\n30\n")
    assert process_file("/tmp/test_nums.txt") == 60
    print("All tests passed!")
