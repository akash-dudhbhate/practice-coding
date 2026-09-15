"""SOLUTION: Counter Class (Easy)"""
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get(self):
        return self.count

if __name__ == "__main__":
    c = Counter()
    c.increment()
    c.increment()
    assert c.get() == 2
    print("All tests passed!")
