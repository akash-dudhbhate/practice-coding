"""SOLUTION: count_up_to Generator (Easy)"""
def count_up_to(n):
    for i in range(1, n + 1):
        yield i

if __name__ == "__main__":
    assert list(count_up_to(5)) == [1, 2, 3, 4, 5]
    assert list(count_up_to(0)) == []
    print("All tests passed!")
