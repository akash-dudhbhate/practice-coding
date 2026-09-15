"""SOLUTION: CountDown Iterator (Easy)"""
class CountDown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

if __name__ == "__main__":
    assert list(CountDown(3)) == [3, 2, 1]
    assert list(CountDown(0)) == []
    print("All tests passed!")
