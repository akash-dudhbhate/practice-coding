"""SOLUTION: Safe Append (Medium)"""
def safe_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

if __name__ == "__main__":
    assert safe_append(1) == [1]
    assert safe_append(2) == [2]  # not [1, 2] — new list each time
    assert safe_append(1, [0]) == [0, 1]
    print("All tests passed!")
