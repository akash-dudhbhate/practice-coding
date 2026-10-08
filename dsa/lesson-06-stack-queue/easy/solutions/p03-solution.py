"""
SOLUTION: Implement a Queue With a List (Easy)
==========================================
FIFO via a list. Two variants shown:

1. pop(0) — simple but O(n) per dequeue (every element shifts).
2. head-index pointer — O(1) dequeue; we just advance a pointer and
   periodically compact when the dead prefix gets large.

The submitted class uses the head-index version — same interface,
amortized O(1) per operation.
"""
class SimpleQueue:
    def __init__(self):
        self._data = []
        self._head = 0            # logical front = _data[_head]

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        if self.is_empty():
            return None
        x = self._data[self._head]
        self._head += 1
        # compact when the dead prefix is bigger than the live part
        if self._head > 64 and self._head > len(self._data) - self._head:
            self._data = self._data[self._head:]
            self._head = 0
        return x

    def peek(self):
        return None if self.is_empty() else self._data[self._head]

    def is_empty(self):
        return self._head >= len(self._data)


# --- the naive list version, kept for comparison ---
# class SimpleQueue:
#     def __init__(self): self._data = []
#     def enqueue(self, x): self._data.append(x)
#     def dequeue(self): return self._data.pop(0) if self._data else None  # O(n)!
#     def peek(self): return self._data[0] if self._data else None
#     def is_empty(self): return not self._data

if __name__ == "__main__":
    q = SimpleQueue()
    assert q.is_empty() == True
    assert q.dequeue() is None
    assert q.peek() is None
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    assert q.peek() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty() == False
    q.enqueue(4)
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty() == True
    assert q.dequeue() is None
    print("All tests passed!")
