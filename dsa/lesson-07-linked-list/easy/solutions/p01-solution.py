"""
SOLUTION: Build a Linked List (Easy)
==============================
Dummy head + walking tail: every node attaches at tail.next, then tail
advances. Return dummy.next so the empty case works with zero special-casing.
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values: list):
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
    assert to_list(build_list([1, 2, 3])) == [1, 2, 3]
    assert to_list(build_list([])) == []
    assert to_list(build_list([7])) == [7]
    assert to_list(build_list([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
    print("All tests passed!")
