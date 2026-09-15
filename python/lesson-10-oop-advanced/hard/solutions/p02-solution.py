"""SOLUTION: Stack with Composition (Hard)"""
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

if __name__ == "__main__":
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert s.size() == 2
    assert s.pop() == 2
    assert s.peek() == 1
    print("All tests passed!")
