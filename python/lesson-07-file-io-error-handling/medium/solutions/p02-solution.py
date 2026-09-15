"""SOLUTION: Append Log (Medium)"""
def append_log(path, message):
    with open(path, "a") as f:
        f.write(message + "\n")

if __name__ == "__main__":
    import os
    p = "/tmp/test_log.txt"
    if os.path.exists(p):
        os.remove(p)
    append_log(p, "First")
    append_log(p, "Second")
    with open(p) as f:
        lines = f.readlines()
    assert len(lines) == 2
    print("All tests passed!")
