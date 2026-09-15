"""SOLUTION: Stack Class (Medium)"""
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

if __name__ == "__main__":
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert len(s) == 2
    assert s.pop() == 2
    assert s.peek() == 1
    try:
        s2 = Stack()
        s2.pop()
        assert False
    except IndexError:
        pass
    print("All tests passed!")
