"""
SOLUTION: Reverse a Linked List — Iterative (Medium)
==============================
prev / curr / nxt: rescue the rest, flip the arrow, advance both.
prev ends on the new head (the old tail). O(n) time, O(1) space.
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next      # rescue the rest BEFORE overwriting
        curr.next = prev     # flip the arrow
        prev = curr          # prev advances
        curr = nxt           # curr advances via the rescue
    return prev

def build_list(values):
    dummy = Node()
    tail = dummy
    for v in values:
        tail.next = Node(v)
        tail = tail.next
    return dummy.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    assert to_list(reverse_list(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert reverse_list(None) is None
    assert to_list(reverse_list(build_list([1]))) == [1]
    assert to_list(reverse_list(build_list([1, 2]))) == [2, 1]
    print("All tests passed!")
