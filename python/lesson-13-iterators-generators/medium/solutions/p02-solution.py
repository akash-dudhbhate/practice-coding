"""SOLUTION: Deep Flatten with yield from (Medium)"""
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

if __name__ == "__main__":
    assert list(flatten([1, [2, [3, [4]]], 5])) == [1, 2, 3, 4, 5]
    assert list(flatten([])) == []
    print("All tests passed!")
