"""SOLUTION: Read JSON (Medium)"""
import json

def read_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

if __name__ == "__main__":
    import json as j
    with open("/tmp/test.json", "w") as f:
        j.dump({"key": "val"}, f)
    assert read_json("/tmp/test.json") == {"key": "val"}
    assert read_json("/nonexistent") is None
    with open("/tmp/bad.json", "w") as f:
        f.write("not json")
    assert read_json("/tmp/bad.json") is None
    print("All tests passed!")
