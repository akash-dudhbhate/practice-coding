"""SOLUTION: Make Counter Closure (Hard)"""
def make_counter(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

if __name__ == "__main__":
    c = make_counter()
    assert c() == 1
    assert c() == 2
    c2 = make_counter(10)
    assert c2() == 11
    print("All tests passed!")
