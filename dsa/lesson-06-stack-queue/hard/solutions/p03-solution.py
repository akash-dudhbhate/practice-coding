"""
SOLUTION: Queue Using Two Stacks (Hard)
==========================================
inbox for enqueue, outbox for dequeue. Pour inbox→outbox ONLY when
outbox is empty — the double reversal yields FIFO. Each element is
pushed+popped per stack once → O(1) amortized per operation.
"""
class TwoStackQueue:
    def __init__(self):
        self.inbox = []     # enqueue side
        self.outbox = []    # dequeue side (top = oldest)

    def _pour(self):
        while self.inbox:
            self.outbox.append(self.inbox.pop())

    def enqueue(self, x):
        self.inbox.append(x)

    def dequeue(self):
        if not self.outbox:        # pour ONLY when empty — else O(n) every time
            self._pour()
        return self.outbox.pop() if self.outbox else None

    def peek(self):
        if not self.outbox:
            self._pour()
        return self.outbox[-1] if self.outbox else None

    def empty(self):
        return not self.inbox and not self.outbox

if __name__ == "__main__":
    q = TwoStackQueue()
    assert q.empty() == True
    assert q.dequeue() is None
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    assert q.peek() == 1
    assert q.dequeue() == 1
    q.enqueue(4)                       # interleave enqueue after dequeue
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.empty() == True
    assert q.dequeue() is None
    assert q.peek() is None
    print("All tests passed!")
