"""
SOLUTION: Detect a Cycle — Floyd's (Medium)
==============================
slow 1 hop, fast 2 hops. Inside a loop fast gains exactly 1 node per
step, so they must meet. No meeting before fast hits None => acyclic.
Identity check (`is`) — two nodes can share a value at different spots.
"""
def has_cycle(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_cycle(values, pos):
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if nodes and 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None

if __name__ == "__main__":
    assert has_cycle(build_cycle([1, 2, 3, 4], 1)) is True
    assert has_cycle(build_cycle([1, 2], 0)) is True
    assert has_cycle(build_cycle([1, 2, 3], -1)) is False
    assert has_cycle(None) is False
    assert has_cycle(build_cycle([1], -1)) is False
    assert has_cycle(build_cycle([1], 0)) is True   # self-loop
    print("All tests passed!")
