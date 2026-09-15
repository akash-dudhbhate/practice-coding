"""SOLUTION: Stack with Parametrized Tests (Hard)"""
import pytest

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

@pytest.mark.parametrize("items,expected", [
    ([1, 2, 3], 3),
    ([], None),
    (["a"], "a"),
])
def test_push_pop(items, expected):
    s = Stack()
    for item in items:
        s.push(item)
    if items:
        assert s.pop() == expected
    else:
        with pytest.raises(IndexError):
            s.pop()

def test_peek_empty():
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.peek() == 1
    s.pop()
    try:
        s.pop()
        assert False
    except IndexError:
        pass
    print("All tests passed!")
